// For snakbar message instead of using an alert box
function mySnakbar(msg) {
    var x = document.getElementById("snackbar");
    x.innerHTML = "";
    x.innerHTML += msg;
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  }