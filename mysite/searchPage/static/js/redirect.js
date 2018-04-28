
$( document ).ready(function() {
  var submitBtn = document.getElementById("submitBtn");
  if (submitBtn) {

    submitBtn.onclick = function clicked(){
    	console.log("button clicked");
      window.location.replace("results");
    /*	var text = document.getElementById("box").value;
    	var paragraph = document.getElementById("demo");

    	paragraph.innerHTML = "";

    	var starting = 0;
    	var i;
    	for(var i = 0; i<text.length; i++){
    		var iteration = document.createElement("p");
    		for(var j = 0; j<text.length; j++){
    			iteration.innerHTML += text.charAt(starting);
    			starting = (starting+1) % text.length;
    		}
    		starting = (starting+1) % text.length;
    		paragraph.appendChild(iteration);
    		paragraph.appendChild(document.createElement("p"));

    	} */
    }
  } else {
    console.log("no submit buttn")
  }

      console.log("this script was included");
});
