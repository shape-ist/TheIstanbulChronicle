function inArea(threshold = 400){
    return $(window).scrollTop() + $(window).height() > $(document).height() - threshold
}

function triggerPagi() {
    if (inArea()){
        console.log("call paginator function here")
        // get number of children in article-list
        // this will wait until the paginator runs so (theoretically) there won't be a repeated paginator function.
        // get new number of children in article-list
        // compare numbers of children in article-list, only continue if they are not equivalent.
    }
}

var intervalId = window.setInterval(function(){
    triggerPagi()
}, 500);