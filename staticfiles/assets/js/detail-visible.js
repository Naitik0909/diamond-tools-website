

var my_loc = $(location).attr('href');
var counter = 2;
var main_path = "";
for (var i=my_loc.length;i>0;i--){
  counter--;
  if (counter == 0){
    main_path = my_loc[i-1];
    break;
  }
}

if (main_path == "2"){
  $('#table-for-gangsaw').css("display", "inherit");
}

else if (main_path == "1"){
  $("#table-for-multiblade").css("display", "inherit");
}

else if(main_path == "3" || main_path == "4" || main_path == "5"){
  $('.others-description').css("display", "inherit");
}
