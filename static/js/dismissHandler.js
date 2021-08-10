function hide(el) {
    el.classList.add('opacity-animation');
    el.parentElement.style.display = "none";
};

document.addEventListener('mousedown', function (e) {
    var container = document.getElementById('login-popup');
    if (!container.contains(e.target)) {
        hide(container)
    }
});

// TODO: implement a class-based for-loop version for a multi-use version