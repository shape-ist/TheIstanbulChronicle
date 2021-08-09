document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        setTimeout(function () {
            var form = document.getElementById('loading');
            if (form)
                form.classList.add("hide");
            setTimeout(function () {
                var form = document.getElementById('loading');
                if (form)
                    form.remove();
            }, 1000);
        }, 800);
    }
};
