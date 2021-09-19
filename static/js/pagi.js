jQuery(function ($) {
    $('#pagi-article-list').on('scroll', function () {
        if ($(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {
            alert('end reached');
        }
    })
});