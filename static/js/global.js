function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
  }  

function display(id, method, overflowLock=null) {
    if (overflowLock == true) {
      document.getElementsByTagName("body")[0].style.overflow = "hidden";
    }
    document.getElementById(id).style.opacity = 1;
    document.getElementById(id).style.display = method;
}


// TODO: check if this works, we want to prevent form resubmission as seen in login/register and profile edit page
if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}