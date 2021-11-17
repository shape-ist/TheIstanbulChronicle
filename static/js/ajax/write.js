// get all write content here and send using ajax
function articleIsValid(title,body) {
    min_length = 1
    max_length = 10
    if ((body.length > max_length) || (body.length < min_length)) {
        return false;
    }
    if (!title) {
        return false;
    }
    return true;
}

$(document).ready(function () {
    $('#write-submit-button').on('click', function (event) {
        console.log('uwu')
        title = $("#write-article-title").val();
        body = easyMDE.value(); 
        if (!articleIsValid(title, body)) {return;}
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