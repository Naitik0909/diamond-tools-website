function checkQuery(){
  var query = document.forms["query-form"]["actual-query"].value;
  if (query.length >= 10000){

    alert('Please enter a query in less than 10000 letters.');
    return false;
  }
  else {
    document.getElementById('new-form').submit();
    return true;
  }
}




function validateForm(){
  var new_value = document.forms["query-form"]["email-phone"].value;
  var flag = 0;

  for (var i=0;i<new_value.length;i++){
    if (new_value[i] == '@' || new_value[i] == '.'){
        flag++;
    }
  }
  if (flag>0){       // Email entered
    checkQuery();
  }
  else{              // Phone number entered
    if (new_value.length == 10){
      checkQuery();
    }
    else{
      alert("Please enter a valid Email address/Phone number");
      return false;
    }
  }


}
