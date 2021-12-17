console.log("JS loaded")
$(function(){
    $('button').click(function(){
        var title = $('#title').val();
        var desc = $('#description').val();
        var start = $('#start').val();
        var end = $('#end').val();
        var place = $('#place').val();
        var lat = $('#lat').val();
        var long = $('#long').val();
        $.ajax({
            url : '/eventsubmit',
            type : 'POST',
            data : $('form').serialize(),
            success : function(response){
                console.log(response);
            },
            error : function(error){
                console.log(error)
            }

        });

    });

});