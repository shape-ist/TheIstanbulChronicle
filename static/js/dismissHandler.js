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


function displayDismiss(trigger, el, displayMethod) {
    elJq = '#' + el
    if ($(elJq).attr('data-event-click') !== 'true') {
        $(elJq).attr('data-event-click', 'true');
        document.addEventListener('mouseup', function (e) {
            var container = document.getElementById(el);
            if (!container.contains(e.target)
                && !document.getElementById(trigger).contains(e.target)) {
                $(elJq).hide()
            }
        });
    }
    if ($(elJq).is(':visible')) {
        $(elJq).hide()
    } else {
        display(el, displayMethod)
    }
}