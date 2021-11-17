function submitArticle() {
    let title = $("#write-article-title").val()
    $.ajax({
        data: {
            title: title,
            body: easyMDE.value(),
            cover: $("#write-article-image").val().trim()
        },
        type: 'POST',
    }).done(function (data) {
        if (data.error) {
            console.log(data.error)
        } else {
            location.href = `/write/success?t=${title}`
        }
    });
}


function validateWrite() {
    let body = easyMDE.value()
    let title = $("#write-article-title").val()
    let minLen = 2000
    let maxLen = 30000
    if ((body.length >= maxLen) || (body.length <= minLen)) {
        return false;
    }
    if ((title.length >= 60) || (title.length <= 5)) {
        return false;
    }
    return true;
}

function disableWriteSubmit() {
    console.log('disable')
    $('#write-submit-button').css('pointer-events', 'none');
    $('#write-submit-button').css('opacity', '.5');
}

function enableWriteSubmit() {
    console.log('enable')
    $('#write-submit-button').css('pointer-events', 'unset');
    $('#write-submit-button').css('opacity', '1');
}


setInterval(function () {
    if (validateWrite() == false) {
        disableWriteSubmit()
    } else {
        enableWriteSubmit()
    }
}, 500)