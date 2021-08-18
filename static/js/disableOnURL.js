(function() {
    var parts = window.location.href.split('/');
    var lastSegment = parts.pop() || parts.pop();
    console.log(lastSegment);
    if (lastSegment = 'about'){
        console.log(document.getElementById('about-header'))
        // document.getElementById('about-header').style.pointerEvents = 'none';
    }
})();

// broken, getElementById returns null.