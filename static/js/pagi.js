function inArea(threshold = 400){
    return $(window).scrollTop() + $(window).height() > $(document).height() - threshold
}

function triggerPagi() {
    if (inArea()){
        console.log("call paginator function here")
    }
}

var intervalId = window.setInterval(function(){
    triggerPagi()
}, 500);