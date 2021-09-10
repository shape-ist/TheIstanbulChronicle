var easyMDE = new EasyMDE({
    autofocus: true,
    indentWithTabs: false,
    minHeight: "480px",
    maxHeight: "480px",
    placeholder: "Type your article here",
    promptURLs: true,
    promptTexts: {
        image: "Enter URL for image for URL:",
        link: "Enter a URL:",
    },
    renderingConfig: {
        singleLineBreaks: false,
        codeSyntaxHighlighting: true,
    },
    showIcons: ["code", "table"],
    tabSize: 4,
    autosave: {
        enabled: true,
        uniqueId: "write-mde-autosave",
        delay: 1000,
        submit_delay: 5000,
        text: "Autosaved at  "
    },
});