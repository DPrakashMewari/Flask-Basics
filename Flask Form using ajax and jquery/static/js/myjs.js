console.log("JS loaded")
$(function(){
    $('button').click(function(){
        var user = $('#inputUsername').val();
        var pass = $('#inputPassword').val();
        $.ajax({
            url : '/signup',
            type : 'POST',
            data : $('form').serialize(),
            success : function(response){
                console.log(response);
            },
            error : function(error){
                console.log(error)
            }

        })

    })

})