function headerState() {
    if (window.scrollY > 100) {
        document.getElementById("header").style.boxShadow = "var(--bs)";
    } else {
        document.getElementById("header").style.boxShadow = "unset";
    }
}

document.addEventListener('scroll', function (e) {
    lastKnownScrollPosition = window.scrollY;
    headerState()
});

(function () {
    headerState();
})();
