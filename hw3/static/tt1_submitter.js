//$.get("answer", {"message":$('messenger').val()})
function new_message(person, message){
            $("#responses").prepend("<p> <strong> "+person+": </strong>"+ message +"</p>");
}
$(function() {
    $("#submit").click(function (e) {
        var x = $("#messenger").val();
        $.get("tt1_responder", {"message": x}, 
            function(data){
                new_message("Server", data);
            }
        );
       return false;  
    });
});
