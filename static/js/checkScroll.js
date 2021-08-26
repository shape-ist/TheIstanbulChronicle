function isScrolledToTop() {

    if (window.scrollY > 100) {
        document.getElementById("header").style.boxShadow = "var(--bs)";
    }
    else {
        document.getElementById("header").style.boxShadow = "unset";
    }
    setTimeout(isScrolledToTop, 500);
}

isScrolledToTop();