function htmlDecode(input) {
    var e = document.createElement('textarea');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function cleanAuthURL(subpage) {
    var sub = htmlDecode(subpage)
    if (sub == 'login') {
        display('login-area', 'flex')
        window.history.replaceState({}, document.title, "/" + "");
    } else if (sub == 'register') {
        display('register-area', 'flex')
        window.history.replaceState({}, document.title, "/" + "");
    }
}
