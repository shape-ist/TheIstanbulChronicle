function hide(el) {
    el.classList.add('opacity-animation');
    el.parentElement.style.display = "none";
};

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('login-content-container');
    if (!container.contains(e.target)) {
        hide(container)
    }
});

document.addEventListener('mouseup', function (e) {
    var container = document.getElementById('register-content-container');
    if (!container.contains(e.target)) {
        hide(container)
    }
});
