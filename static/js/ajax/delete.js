$(document).ready(function () {
    $('#delete-btn').on('submit', function (event) {
        $.ajax({
            data: {
                id: window.location.href.split("/")[-1],
            },
            type: 'POST',
            url: '/delete',
        }).done(function (data) {
            if (data.error) {
                alert(data.error)
            } else {
                alert(data)
            }
        });
        event.preventDefault();
    });
});