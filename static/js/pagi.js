var pagiState = false

function inArea(threshold = 100, current = $(window).scrollTop()) {
    return current + $(window).height() > $(document).height() - threshold
}

function canPagi() {
    return ($('#pagi-trigger').visible() && !pagiState && $('#article-list').height() > 1)
}

function displayAppended(content, cuid, callback) {
    $(`#${cuid}`).loadTemplate($("#article-item"), {
        ...content
    })
    callback()
}

function appendArticle(article, clamp_threshold = 6) {
    article.timestamp = unixTime(article.timestamp)
    article.url = `/article/${article.uid}`
    article.writer_url = `/profile/${article.writer.uid}`
    cuid = generateUID()
    appended = $('#article-list-inner').append($(`<div class="article-list-item"><div id=${cuid}>`))
    displayAppended(article, cuid, function(){
        $clamp(document.getElementById(cuid)
        .getElementsByClassName('clamp-article-preview')[0],
        {clamp: clamp_threshold});
    })
}

var socket = io();
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

function waitForFirstRender(elementPath, callBack) {
    window.setTimeout(function () {
        if ($(elementPath).children().length) {
            callBack(elementPath, $(elementPath));
        } else {
            waitForFirstRender(elementPath, callBack);
        }
    }, 500)
}

function triggerPagi() {
    pagi()
    waitForFirstRender('#article-list-inner', function () {
        $('#pagi-trigger').css('bottom', Math.round($('#article-list-inner').height() / 2));
    })
    var pagiInterval = window.setInterval(function () {
        if (canPagi()) {
            pagi()
        }
    }, 500);
}

var pagiStore = []

document.addEventListener('DOMContentLoaded', function () {
    pagiStore.push({
        data: [],
        last_uid: document.getElementById('highlights').getAttribute('data-highlights-end')
    })
    triggerPagi()
})