var pagiState = false

function inArea(threshold = 100, current = $(window).scrollTop()) {
    return current + $(window).height() > $(document).height() - threshold
}

function canPagi() {
    return ($('#pagi-trigger').visible() && !pagiState && $('#article-list').height() > 1)
}

function appendArticle(article) {
    article.timestamp = unixTime(article.timestamp)
    cuid = generateUID()
    appended = $('#article-list-inner').append($(`<div class="article-list-item"><div id=${cuid}>`))
    $(`#${cuid}`).loadTemplate($("#article-item"), {
        ...article
    });
}

var socket = io();
var pagiStore = [{
    data: null,
    last_uid: null
}]

socket.on('message', function (msg) {
    pagiStore.push(msg)
    if (msg.data.error === undefined) {
        msg.data.forEach(function (i) {
            appendArticle(i)
        })
        pagiState = false
    }
})

function pagi() {
    pagiState = true
    if (pagiStore.at(-1).last_uid !== undefined) {
        socket.emit('pagiRequest', pagiStore.at(-1).last_uid);
    } else {
        clearInterval(pagiInterval);
    }
}

pagi()
var pagiInterval = window.setInterval(function () {
    if (canPagi()) {
        pagi()
    }
}, 500);