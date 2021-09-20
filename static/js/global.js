function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
  }  

function display(id, method) {
    document.getElementById(id).style.display = method
}