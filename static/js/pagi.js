$(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
        alert("near bottom!");
    }
 });