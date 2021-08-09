document.addEventListener('mouseup', function(e) {
    var container = document.getElementById('login-popup');
    if (!container.contains(e.target)) {
        container.parentElement.style.display = 'none';
    }
});

// TODO: implement a class-based for-loop version for a multi-use version