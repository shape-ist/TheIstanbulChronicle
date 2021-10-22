function finishLoad() {
    setTimeout(function () {
        var form = document.getElementById('loading');
        if (form)
            form.classList.add("hide");
        setTimeout(function () {
            var form = document.getElementById('loading');
            if (form)
                form.remove();
        }, 700);
    }, 500);
}

window.onload = function () {
    finishLoad();
}