// fern/models.js
// This runs after the page loads and replaces variables in code blocks

(function() {
    // Your model variables - change these in one place
    const MODELS = {
        TEXT_MODEL: "Hermes-3-Llama-3.1-70B",
        CODE_MODEL: "Qwen2.5-Coder-14B-Instruct",
        JS_MODEL: "Hermes3Llama3170B",
        GO_MODEL: "Hermes3Llama3170B",
        RUST_MODEL: "Hermes3Llama3170B",
    };

    function replaceVariablesInElement(element) {
        if (element.nodeType === Node.TEXT_NODE) {
            element.textContent = element.textContent.replace(/\{\{(\w+)\}\}/g, (match, varName) => {
                return MODELS[varName] !== undefined ? MODELS[varName] : match;
            });
        } else if (element.nodeType === Node.ELEMENT_NODE) {
            // Process all child nodes
            Array.from(element.childNodes).forEach(child => {
                replaceVariablesInElement(child);
            });
        }
    }

    function processPage() {
        // Find all code blocks and other content
        const codeBlocks = document.querySelectorAll('pre code, code');
        const contentAreas = document.querySelectorAll('article, .content, main');

        // Process code blocks
        codeBlocks.forEach(block => {
            replaceVariablesInElement(block);
        });

        // Process main content areas
        contentAreas.forEach(area => {
            replaceVariablesInElement(area);
        });
    }

    // Run on initial load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', processPage);
    } else {
        processPage();
    }

    // Also run when navigating between pages (for SPAs)
    let lastUrl = location.href;
    new MutationObserver(() => {
        const url = location.href;
        if (url !== lastUrl) {
            lastUrl = url;
            setTimeout(processPage, 100); // Small delay to let content load
        }
    }).observe(document, { subtree: true, childList: true });

})();