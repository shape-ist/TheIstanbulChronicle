function headerState() {
    if (window.scrollY > 100) {
        document.getElementById("header").style.boxShadow = "var(--bs)";
        document.getElementById("header").style.background = "var(--bg-alt)";
    }
    else {
        document.getElementById("header").style.boxShadow = "unset";
        document.getElementById("header").style.background = "var(--bg)";
    }
}

document.addEventListener('scroll', function(e) {
    lastKnownScrollPosition = window.scrollY;
        headerState()
    });

(function () {
    headerState();
})();
