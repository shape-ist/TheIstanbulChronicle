$(document).ready(function () {
    $('#register-form').on('submit', function (event) {
        $.ajax({
            data: {
                job: "register",
                email: $('#register-email').val(),
                password: $('#register-password').val(),
                name: $("#register-name").val()
            },
            type: 'POST',
            url: '/',
            traditional: true,
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