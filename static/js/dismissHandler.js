function hide(el) {
    el.classList.add('opacity-animation');
    el.parentElement.style.display = "none";
};

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('login-popup');
    if (!container.contains(e.target)) {
        hide(container)
    }
});

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('register-popup');
    if (!container.contains(e.target)) {
        hide(container)
    }
});
