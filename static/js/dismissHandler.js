function hide(el) {
    el.parentElement.style.display = "none";
};

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('login-content-container');
    if (!container.contains(e.target)) {
        hide(container)
        $('body').css({'overflow': 'visible'});
    }
});

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('register-content-container');
    if (!container.contains(e.target)) {
        hide(container)
        $('body').css({'overflow': 'visible'});
    }
});