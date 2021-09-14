$(document).ready(function () {
    $('#login-form').on('submit', function (event) {
        $.ajax({
            data: {
                email: $('login-email').val(),
                password: $('login-password').val()
            },
            type: 'POST',
            url: '/'
        }).done(function (data) {

            if (data.error) {
                alert(data.error)
            } else {
                alert(data.email)
            }

        });
        event.preventDefault();
    });
});