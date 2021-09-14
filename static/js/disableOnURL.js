function classOnURL(slug, elementID, className) {
    const windowSlug = window.location.pathname;
    const jqElement = `#${elementID}`
    if (windowSlug == slug) {
        $(jqElement).ready(function () {
            $(jqElement).addClass(className);
        });

    }
}

(function () {
    classOnURL('/about', 'header-about', 'about-us-active')
})();