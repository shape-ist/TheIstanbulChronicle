function inArea(threshold = 100, current = $(window).scrollTop()){
    return current + $(window).height() > $(document).height() - threshold
}

function getPagi(props){
    return Promise.resolve($.ajax({
        url: `/api/pagi/articles/timestamp/q?${props}`
    }));
  }

var pagiState = false;
var uidIndex = null;

function triggerPagi(last_uid=null) {
    pagiState = true;
    if (last_uid == null){index = ''}
    else {index = `&i=${last_uid}`}
    getPagi(`o=desc&l=10${index}`)
    .then(data => o = data)
    .catch(error => console.log('Pagination Error:', error));
    $('#article-list').height("+=1000");
    pagiState = false;
    return o
    // get number of children in article-list
    // this will wait until the paginator runs so (theoretically) there won't be a repeated paginator function.
    // get new number of children in article-list
    // compare numbers of children in article-list, only continue if they are not equivalent.
}

function appendPagi(obj) {
    for (let i = 0; i < obj['data'].length; i++) {
        e = obj['data'][i]
        console.log(e.title)
        $("#article-list").append('<li class="article-list-item"></li>');
        $('#article-list').loadTemplate($("#template"),
        {...e});
    }
}

function runPagi(){
    if ($('#pagi-trigger').visible() && !pagiState && uidIndex !== undefined){
        pagi_obj = triggerPagi(uidIndex)
        uidIndex = pagi_obj.last_uid
        appendPagi(pagi_obj)
    }
}

document.addEventListener(
    'scroll',
    (event) => {
        runPagi()
    }, 
    { passive: true }
);