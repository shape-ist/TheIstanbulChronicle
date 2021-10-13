$(document).ready(function () {
    $('#login-form').on('submit', function (event) {
        $.ajax({
            data: {
                job: "login",
                email: $('#login-email').val(),
                password: $('#login-password').val()
            },
            type: 'POST',
            url: '/',
            traditional: true
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