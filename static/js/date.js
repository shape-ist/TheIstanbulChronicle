function currentDate() {
    return new Date().toJSON().slice(0, 10).replace(/-/g, '/')
}

function displayCurrentDate(el) {
    return $(`#${el}`).html(currentDate())
}