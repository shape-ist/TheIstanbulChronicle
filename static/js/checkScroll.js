function isScrolledToTop() {

    if (window.scrollY > 100) {
        document.getElementById("header").style.boxShadow = "var(--bs)";
        document.getElementById("header").style.background = "var(--bg-alt)";
    }
    else {
        document.getElementById("header").style.boxShadow = "unset";
        document.getElementById("header").style.background = "var(--bg)";
    }
    setTimeout(isScrolledToTop, 50);
}

isScrolledToTop();