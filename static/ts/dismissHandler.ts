var ignoreClickOnMeElement = document.getElementById('someElementID');

document.addEventListener('click', function(event) {
    var isClickInsideElement = ignoreClickOnMeElement.contains(event.target);
    if (!isClickInsideElement) {
        //Do something click is outside specified element
    }
});z