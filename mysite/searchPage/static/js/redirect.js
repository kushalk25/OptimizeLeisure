
$( document ).ready(function() {
  var resultsBtn = document.getElementById("resultsBtn");
  if (resultsBtn) {
    console.log("results button found")
    resultsBtn.onclick = function clicked(){
      console.log ("results button clicked")
      window.location.replace("results");
    }
  } else {
    console.log("no results button")
  }

  var homeBtn = document.getElementById("homeBtn");
  if (homeBtn) {
    console.log("home button found")
    homeBtn.onclick = function clicked(){
      console.log("home button clicked")
      window.location.replace("/searchPage");
    }
  } else {
    console.log("no home button")
  }

});
