document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
        console.log("dom ready.");
        setTimeout(function () {
            document.getElementById("loading").classList.add("hide");
            setTimeout(function () {
                document.getElementById("loading").remove();
            }, 1000)
        }, 800)
    }
};