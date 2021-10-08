function setTextSmall() {
    $('#article-body').css('font-size', '1em');
    localStorage.setItem('articleSizePreference', 'S');
}

function setTextMedium() {
    $('#article-body').css('font-size', '1.25em');
    localStorage.setItem('articleSizePreference', 'M');
}

function setTextBig() {
    $('#article-body').css('font-size', '1.5em');
    localStorage.setItem('articleSizePreference', 'L');
}

document.onreadystatechange = function () {
    if (localStorage.getItem('articleSizePreference') === 'S') {
        setTextSmall();
    }
    else if (localStorage.getItem('articleSizePreference') === 'M') {
        setTextMedium();
    }
    else if (localStorage.getItem('articleSizePreference') === 'L') {
        setTextBig();
    }
};