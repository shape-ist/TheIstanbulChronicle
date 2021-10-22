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
    displayAppended(article, cuid, function () {
        $clamp(document.getElementById(cuid)
            .getElementsByClassName('clamp-article-preview')[0], {
                clamp: clamp_threshold
            });
    })
}

var socket = io.connect(window.location.host);
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

function getFallbackBatch(props) {
    return Promise.resolve($.ajax({
        url: `/api/pagi/articles/timestamp/q?${props}`
    }));
}

async function pagiFallback(x, limit = 50) {
    let fallbackUIDIndex = [x]
    try {

        if (limit % 5 != 0) {
            throw new Error('pagiFallback: Enter a multiple of 5')
        }
        sliceLen = (limit / 5)
        for (const i of Array(sliceLen).keys()) {
            var articleBatch = await getFallbackBatch(`o=desc&l=5&i=${fallbackUIDIndex[fallbackUIDIndex.length - 1]}`)
            fallbackUIDIndex.push(articleBatch.last_uid)
            articleBatch.data.forEach(function (i) {
                appendArticle(i)
            })
        }
    }
    finally {
        console.log('pagiFallback done')
    }
}

var pagiStore = []
document.addEventListener('DOMContentLoaded', function () {
    var highlightEndArticle = document.getElementById('highlights').getAttribute('data-highlights-end')
    pagiStore.push({
        data: [],
        last_uid: highlightEndArticle
    })
    try {
        throw new Error('pagiFallback')
        // triggerPagi()
    } catch {
        pagiFallback(highlightEndArticle, limit = 40)
    }
})