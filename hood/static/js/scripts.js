$(document).ready(function(){
    $('#postform').submit(function(event){
      event.preventDefault()
      var formData = $(this).serialize();
    $.ajax({
      url:$(this).attr("data-url"),
      type:'POST',
      data:formData,
      dataType:'json',
      success: function(data){
        //  clear the form.
        console('success')
        $("#postform").trigger('reset');
        alert(data.success);
      },
      error: function(message){
          alert('ERROR')
      }
    })// END of Ajax method
    }) // End of submit event
  
  }) // End of document ready function
