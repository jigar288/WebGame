var word_list = ["cat"];
var word = "cat";
var spaces = word.length;
var i = 0;
var string1 = "";
while(i < spaces){
  string1 += "__ ";
  i++;
}


function myFunction(event){
  var x = event.target.value;
  var res = $("#correctguess").html().concat(x);
  var rightwrong = word.indexOf(x.toLocaleLowerCase());
  if(rightwrong >= 0){
    var guess = $("#correctguess").html();
    var final = guess.substring(0, rightwrong*3) + " " + x + " " + guess.substring((rightwrong+1) *3,  guess.length);
    $("#correctguess").html(final);
  }
 }


$(document).ready(function(){
  var word_list = ["cat"]
  var word = "cat"
  var spaces = word.length;
  var i = 0;

  while(i < spaces){
  $("#correctguess").append("__ ");
    i++;
  }

  $("button").click(myFunction);

}
)
