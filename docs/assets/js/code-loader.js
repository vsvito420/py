/**
 * Code-Loader - Lädt Python-Dateien aus den Modulordnern und zeigt sie auf der Website an
 */

document.addEventListener('DOMContentLoaded', function() {
    // Alle Code-Loader-Elemente finden
    const loaderElements = document.querySelectorAll('.code-loader');
    
    loaderElements.forEach(function(element) {
        const filePath = element.getAttribute('data-file');
        const targetElement = element;
        
        if (filePath) {
            loadPythonFile(filePath, targetElement);
        }
    });
});

/**
 * Lädt eine Python-Datei und zeigt sie im angegebenen Element an
 * @param {string} filePath - Pfad zur Python-Datei
 * @param {HTMLElement} targetElement - Element, in dem der Code angezeigt werden soll
 */
function loadPythonFile(filePath, targetElement) {
    // Korrigierter Pfad: Die Dateien befinden sich jetzt im Verzeichnis /py/anleitungen/
    fetch(`/py/anleitungen/${filePath}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Fehler beim Laden der Datei: ${response.status}`);
            }
            return response.text();
        })
        .then(content => {
            // Python-Datei in HTML umwandeln
            const htmlContent = convertPythonToHTML(content, filePath);
            targetElement.innerHTML = htmlContent;
            
            // PyScript-Elemente initialisieren
            initializePyScriptElements(targetElement);
        })
        .catch(error => {
            targetElement.innerHTML = `<div class="error">Fehler beim Laden der Datei: ${error.message}</div>`;
            console.error('Fehler beim Laden der Python-Datei:', error);
        });
}

/**
 * Wandelt Python-Code in HTML mit interaktiven Elementen um
 * @param {string} content - Inhalt der Python-Datei
 * @param {string} filePath - Pfad zur Python-Datei
 * @returns {string} HTML-Darstellung des Python-Codes
 */
function convertPythonToHTML(content, filePath) {
    // Dateiname extrahieren
    const fileName = filePath.split('/').pop();
    
    // Kommentare und Codeblöcke identifizieren
    const sections = extractSections(content);
    
    let html = `<h2>${fileName}</h2>`;
    
    // Abschnitte in HTML umwandeln
    sections.forEach((section, index) => {
        if (section.type === 'comment') {
            // Kommentare als Erklärungstext darstellen
            html += `<div class="explanation">${formatComment(section.content)}</div>`;
        } else if (section.type === 'code') {
            // Code als interaktiven Block darstellen
            html += `
            <div class="code-block">
                <div class="code-example">
                    <pre><code class="language-python">${escapeHTML(section.content)}</code></pre>
                </div>
                <div class="interactive-code">
                    <py-repl id="code-${index}">${section.content}</py-repl>
                </div>
            </div>`;
        }
    });
    
    return html;
}

/**
 * Extrahiert Kommentar- und Code-Abschnitte aus Python-Code
 * @param {string} content - Python-Code
 * @returns {Array} Array von Abschnitten mit Typ und Inhalt
 */
function extractSections(content) {
    const lines = content.split('\n');
    const sections = [];
    
    let currentSection = { type: null, content: '' };
    let inMultilineComment = false;
    
    lines.forEach(line => {
        const trimmedLine = line.trim();
        
        // Multiline-Kommentare erkennen
        if (trimmedLine.startsWith('"""') || trimmedLine.startsWith("'''")) {
            inMultilineComment = !inMultilineComment;
            
            // Wenn ein neuer Multiline-Kommentar beginnt
            if (inMultilineComment) {
                if (currentSection.type === 'code' && currentSection.content.trim()) {
                    sections.push({...currentSection});
                }
                currentSection = { type: 'comment', content: trimmedLine + '\n' };
            } 
            // Wenn ein Multiline-Kommentar endet
            else {
                currentSection.content += trimmedLine + '\n';
                sections.push({...currentSection});
                currentSection = { type: 'code', content: '' };
            }
            return;
        }
        
        // Innerhalb eines Multiline-Kommentars
        if (inMultilineComment) {
            currentSection.content += line + '\n';
            return;
        }
        
        // Einzeilige Kommentare
        if (trimmedLine.startsWith('#')) {
            // Wenn vorher Code war, speichern
            if (currentSection.type === 'code' && currentSection.content.trim()) {
                sections.push({...currentSection});
                currentSection = { type: 'comment', content: line + '\n' };
            } 
            // Wenn bereits ein Kommentar war, anhängen
            else if (currentSection.type === 'comment') {
                currentSection.content += line + '\n';
            } 
            // Neuer Kommentar
            else {
                currentSection = { type: 'comment', content: line + '\n' };
            }
        } 
        // Code-Zeilen
        else {
            // Wenn vorher ein Kommentar war, speichern
            if (currentSection.type === 'comment' && currentSection.content.trim()) {
                sections.push({...currentSection});
                currentSection = { type: 'code', content: line + '\n' };
            } 
            // Wenn bereits Code war, anhängen
            else if (currentSection.type === 'code') {
                currentSection.content += line + '\n';
            } 
            // Neuer Code
            else {
                currentSection = { type: 'code', content: line + '\n' };
            }
        }
    });
    
    // Letzten Abschnitt hinzufügen
    if (currentSection.content.trim()) {
        sections.push(currentSection);
    }
    
    return sections;
}

/**
 * Formatiert Kommentare für die HTML-Darstellung
 * @param {string} comment - Kommentartext
 * @returns {string} Formatierter HTML-Text
 */
function formatComment(comment) {
    // Entferne Kommentarzeichen
    let text = comment.replace(/^#\s*/gm, '');
    text = text.replace(/^"""\s*(.*?)\s*"""$/s, '$1');
    text = text.replace(/^'''\s*(.*?)\s*'''$/s, '$1');
    
    // Markdown-ähnliche Formatierung
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    // Überschriften
    text = text.replace(/^=====(.*?)=====$/gm, '<h3>$1</h3>');
    
    // Absätze
    const paragraphs = text.split('\n\n');
    return paragraphs.map(p => `<p>${p.replace(/\n/g, ' ')}</p>`).join('');
}

/**
 * Initialisiert PyScript-Elemente in einem Container
 * @param {HTMLElement} container - Container mit PyScript-Elementen
 */
function initializePyScriptElements(container) {
    // PyScript-Elemente initialisieren (falls nötig)
    if (window.pyScriptInitialized) {
        const pyReplElements = container.querySelectorAll('py-repl');
        pyReplElements.forEach(element => {
            // Hier könnte zusätzliche Initialisierung erfolgen
            element.setAttribute('auto-generate', 'true');
        });
    }
}

/**
 * Hilfsfunktion zum Escapen von HTML-Zeichen
 * @param {string} text - Zu escapender Text
 * @returns {string} Escapeter Text
 */
function escapeHTML(text) {
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}