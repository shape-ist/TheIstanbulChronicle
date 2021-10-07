function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

function display(id, method, overflowLock = null) {
    if (overflowLock == true) {
        document.getElementsByTagName("body")[0].style.overflow = "hidden";
    }
    document.getElementById(id).style.opacity = 1;
    document.getElementById(id).style.display = method;
}

function unixTime(t) {
    var date = new Date(t * 1000);
    var options = {year: 'numeric', month: 'short', day: 'numeric'};
    return (date.toLocaleDateString("en-US", options));
}

function generateUID() {
    return '_' + Math.random().toString(36).substr(2, 9);
}


// TODO: check if this works, we want to prevent form resubmission as seen in login/register and profile edit page
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}