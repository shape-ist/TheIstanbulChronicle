$(document).ready(function () {
    $('#login-form').on('submit', function (event) {
        $.ajax({
            data: {
                job: "register",
                email: 'email',
                password: 'pass',
                name: 'name'
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