
$( document ).ready(function() {
  var deleteBtns = document.getElementsByClassName("deleteBtn");

  if(deleteBtns){
    for (var i = 0; i<deleteBtns.length; i++) {
      var button = deleteBtns[i];
      deleteBtns[i].onclick = function clicked(){
        $.get(
          "delete/"+this.getAttribute("data-activity-id"),
          function(data, status) {
            location.reload();
          }
        )
      }
    }
  }
});
