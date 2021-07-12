$('.nav-button').hover(function(){
  $(this).css("color", "#F58F84");

});

$('.nav-button').mouseleave(function(){
  $(this).css("color", "black");
});

$('#enquire-button').hover(function(){
  $(this).css("color", "white");
  $(this).css("background-color", "#472743")
});

$('#enquire-button').mouseleave(function(){
  $(this).css("color", "black");
  $(this).css("background-color", "inherit")
});

$('.nav-button').on('click', function(){
  var button_name = $(this).text();
  var counter = 0;
  for(var i=0;i<button_name.length;i++){
    if(button_name[i] == 'q'){
      counter++;
      break;
    }
  }
  if (counter == 1){
    $('.slicknav_icon-bar').click();
  }

});
