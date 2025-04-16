        /**
 * Code-Execution - Ermöglicht die Ausführung von Python-Code in der rechten Spalte
 */

document.addEventListener('DOMContentLoaded', function() {
    // Warte auf PyScript-Initialisierung
    document.addEventListener('py-ready', function() {
        console.log('PyScript ist bereit für Code-Ausführung');
        initializeCodeExecution();
    });

    // Fallback, falls das py-ready Event nicht ausgelöst wird
    setTimeout(function() {
        if (!window.codeExecutionInitialized) {
            console.log('PyScript Timeout - Initialisiere Code-Ausführung');
            initializeCodeExecution();
        }
    }, 3000);
});

// Flag zur Vermeidung doppelter Initialisierung
window.codeExecutionInitialized = false;

/**
 * Initialisiert die Code-Ausführungsfunktionalität
 */
function initializeCodeExecution() {
    if (window.codeExecutionInitialized) return;
    window.codeExecutionInitialized = true;

    // Finde alle Code-Blöcke und füge Run-Buttons hinzu
    addRunButtonsToCodeBlocks();
    
    // Erstelle ein verstecktes py-repl Element für die Ausführung
    createHiddenPyRepl();
}

/**
 * Fügt allen Code-Blöcken Run-Buttons hinzu
 */
function addRunButtonsToCodeBlocks() {
    // Finde alle Code-Blöcke
    const codeBlocks = document.querySelectorAll('.code-block');
    
    codeBlocks.forEach(function(block, index) {
        // Finde den Code-Inhalt
        const codeElement = block.querySelector('pre code');
        if (!codeElement) return;
        
        const code = codeElement.textContent;
        
        // Erstelle den Run-Button
        const runButton = document.createElement('button');
        runButton.textContent = 'In Konsole ausführen';
        runButton.className = 'run-button';
        runButton.dataset.code = code;
        runButton.dataset.index = index;
        
        // Füge Event-Listener hinzu
        runButton.addEventListener('click', function() {
            executeCodeInConsole(code);
        });
        
        // Füge den Button zum Code-Block hinzu
        const codeExample = block.querySelector('.code-example');
        if (codeExample) {
            codeExample.appendChild(runButton);
        }
    });
    
    // Finde auch alle py-repl Elemente außerhalb von Code-Blöcken
    const pyReplElements = document.querySelectorAll('py-repl:not(.code-block py-repl)');
    
    pyReplElements.forEach(function(pyRepl, index) {
        // Erstelle den Run-Button
        const runButton = document.createElement('button');
        runButton.textContent = 'In Konsole ausführen';
        runButton.className = 'run-button';
        runButton.dataset.replId = pyRepl.id;
        runButton.dataset.index = `repl-${index}`;
        
        // Füge Event-Listener hinzu
        runButton.addEventListener('click', function() {
            const code = pyRepl.textContent;
            executeCodeInConsole(code);
        });
        
        // Füge den Button nach dem py-repl Element ein
        pyRepl.parentNode.insertBefore(runButton, pyRepl.nextSibling);
    });
}

/**
 * Erstellt ein verstecktes py-repl Element für die Ausführung
 */
function createHiddenPyRepl() {
    // Erstelle ein verstecktes py-repl Element
    const hiddenPyRepl = document.createElement('py-repl');
    hiddenPyRepl.id = 'hidden-py-repl';
    hiddenPyRepl.style.display = 'none';
    
    // Füge es zum Body hinzu
    document.body.appendChild(hiddenPyRepl);
}

/**
 * Führt den Code in der Konsole aus
 * @param {string} code - Der auszuführende Python-Code
 */
function executeCodeInConsole(code) {
    // Finde das Konsolen-Output-Element
    const consoleOutput = document.getElementById('console-output');
    if (!consoleOutput) return;
    
    // Setze den Code in das versteckte py-repl Element
    const hiddenPyRepl = document.getElementById('hidden-py-repl');
    if (!hiddenPyRepl) return;
    
    // Erstelle ein neues py-script Element für die Ausführung
    const pyScript = document.createElement('py-script');
    const scriptId = 'py-script-' + Date.now();
    pyScript.id = scriptId;
    
    // Füge eine Funktion hinzu, um die Ausgabe zu erfassen
    const wrappedCode = `
import sys
from io import StringIO

# Umleiten von stdout
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

try:
    # Ausführen des Codes
${code.split('\n').map(line => '    ' + line).join('\n')}
except Exception as e:
    print(f"Fehler: {e}")
finally:
    # Zurücksetzen von stdout und Ausgabe
    output = mystdout.getvalue()
    sys.stdout = old_stdout
    
# Element für die Ausgabe finden
from js import document
console_output = document.getElementById('console-output')
if console_output:
    # Ausgabe anzeigen
    console_output.innerHTML = f"<pre>{output}</pre>"
`;
    
    pyScript.textContent = wrappedCode;
    
    // Entferne vorherige py-script Elemente
    const oldScripts = document.querySelectorAll('py-script[id^="py-script-"]');
    oldScripts.forEach(script => script.remove());
    
    // Füge das neue py-script Element hinzu
    document.body.appendChild(pyScript);
    
    // Zeige "Wird ausgeführt..." in der Konsole an
    consoleOutput.innerHTML = "<p>Wird ausgeführt...</p>";
}