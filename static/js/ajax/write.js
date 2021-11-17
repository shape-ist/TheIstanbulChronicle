// get all write content here and send using ajax
function bodyIsValid(body) {
    min_length = 0
    max_length = 9999999
    if ((body.length > max_length) || (body.length < min_length)) {
        return false;
    }
    return true;
}

$(document).ready(function () {
    console.log("ready");
    $('#submit-button').on('click', function (event) {
        title = $("#write-article-title").val();
        body = $(".CodeMirror-lines").text().replace("x\xa0","");
        console.log(title);
        if (!bodyIsValid(body)) {return;}
        $.ajax({
            data: {
                title: title,
                body: body
            },
            type: 'POST',
            url: '/write/submit',
            traditional: true
        }).done(function (data) {
            if (data.error) {
                alert(data.error)
            } else {
                location.href = "/"
            }
        });
        event.preventDefault();
    });
});