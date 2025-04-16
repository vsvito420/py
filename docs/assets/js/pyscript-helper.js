/**
 * PyScript Helper - Wandelt Markdown-Codeblöcke in interaktive PyScript-Beispiele um
 */

document.addEventListener('DOMContentLoaded', function() {
    // Warte auf PyScript-Initialisierung
    document.addEventListener('py-ready', function() {
        console.log('PyScript ist bereit');
        initializePyScriptBlocks();
    });

    // Fallback, falls das py-ready Event nicht ausgelöst wird
    setTimeout(function() {
        if (!window.pyScriptInitialized) {
            console.log('PyScript Timeout - Initialisiere Blöcke');
            initializePyScriptBlocks();
        }
    }, 3000);
});

// Flag zur Vermeidung doppelter Initialisierung
window.pyScriptInitialized = false;

/**
 * Initialisiert alle PyScript-Blöcke auf der Seite
 */
function initializePyScriptBlocks() {
    if (window.pyScriptInitialized) return;
    window.pyScriptInitialized = true;

    // Finde alle pyscript-example Divs und wandle sie in interaktive Beispiele um
    convertPyScriptBlocks('pyscript-example', 'example');
    
    // Finde alle pyscript-exercise Divs und wandle sie in interaktive Übungen um
    convertPyScriptBlocks('pyscript-exercise', 'exercise');
}

/**
 * Wandelt Codeblöcke in interaktive PyScript-Beispiele um
 * @param {string} className - Die CSS-Klasse der zu konvertierenden Blöcke
 * @param {string} prefix - Präfix für die ID der py-repl Elemente
 */
function convertPyScriptBlocks(className, prefix) {
    const blocks = document.querySelectorAll('.' + className);
    
    blocks.forEach(function(block, index) {
        // Extrahiere den Python-Code aus dem pre>code Block
        const codeBlock = block.querySelector('pre code');
        if (!codeBlock) return;
        
        // Extrahiere den Code und bewahre die Formatierung
        let code = codeBlock.textContent;
        
        // Entferne nur führende/nachfolgende Leerzeilen, aber bewahre Einrückungen
        code = code.replace(/^\s*\n/, '').replace(/\n\s*$/, '');
        
        // Erstelle eine eindeutige ID für das py-repl Element
        const id = `${prefix}-${index}`;
        
        // Erstelle das py-repl Element
        const pyRepl = document.createElement('py-repl');
        pyRepl.id = id;
        
        // Setze den Code mit korrekter Formatierung
        pyRepl.textContent = code;
        
        // Stelle sicher, dass die Formatierung erhalten bleibt
        pyRepl.style.whiteSpace = 'pre';
        pyRepl.setAttribute('auto-generate', 'true');
        
        // Extrahiere den Titel, falls vorhanden
        const title = block.querySelector('h4');
        const titleText = title ? title.textContent : '';
        
        // Erstelle ein neues div für das interaktive Beispiel
        const newBlock = document.createElement('div');
        newBlock.className = className;
        
        // Füge den Titel hinzu, falls vorhanden
        if (titleText) {
            const newTitle = document.createElement('h4');
            newTitle.textContent = titleText;
            newBlock.appendChild(newTitle);
        }
        
        // Füge die Beschreibung hinzu, falls vorhanden (für Übungen)
        const description = block.querySelector('p');
        if (description) {
            const newDescription = document.createElement('p');
            newDescription.innerHTML = description.innerHTML;
            newBlock.appendChild(newDescription);
        }
        
        // Füge das py-repl Element hinzu
        newBlock.appendChild(pyRepl);
        
        // Ersetze den ursprünglichen Block durch den neuen Block
        block.parentNode.replaceChild(newBlock, block);
    });
}

/**
 * Hilfsfunktion zum Hinzufügen von Buttons für Beispiele
 * @param {string} id - Die ID des py-repl Elements
 * @param {string} code - Der Python-Code
 */
function addRunButton(id, code) {
    const button = document.createElement('button');
    button.textContent = 'Ausführen';
    button.className = 'run-button';
    button.onclick = function() {
        // Führe den Code aus
        const pyRepl = document.getElementById(id);
        if (pyRepl) {
            pyRepl.evaluate();
        }
    };
    
    // Füge den Button nach dem py-repl Element ein
    const pyRepl = document.getElementById(id);
    if (pyRepl) {
        pyRepl.parentNode.insertBefore(button, pyRepl.nextSibling);
    }
}