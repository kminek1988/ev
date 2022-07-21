$(".text").click(function(){
    $( ".element" ).removeClass( "active" )
    $(this).parent( ".element" ).addClass('active');;
  });