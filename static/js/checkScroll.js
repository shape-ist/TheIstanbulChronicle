function headerState() {
    const header = $('#header');
    const scaleFactor = '.8';
    if (window.scrollY > 100) {
        header.css('box-shadow', 'var(--bs-s)');
        $('#logo-wrapper').css('font-size', `${scaleFactor}em`);
        $('#title').css('margin', '18px auto 16px auto');
        $('#logo-beta').css('opacity', '0');
        $('#ftcl').css('display', 'none');
    } else {
        header.css('box-shadow', '');
        $('#logo-wrapper').css('font-size', '');
        $('#title').css('margin', '');
        $('#header-rightmost').css('transform', '');
        $('#logo-beta').css('opacity', '');
        $('#ftcl').css('display', '');
    }
}

(function () {
    headerState();
    document.addEventListener('scroll', function (e) {
        lastKnownScrollPosition = window.scrollY;
        headerState()
    });
})();
