function new_message(person, message){
            $("#responses").prepend("<p> <strong> "+person+": </strong>"+ message +"</p>");
}
$(function() {
    $("#messenger").keypress(function (e) {
        var key = e.which;
        if(key == 13)  // the enter key code
        {
            var x = $("#messenger").val();
            new_message("You", x);
            $.get("/get_response", {"msg": x}, 
                function(data){
                    new_message("Server", data);
                }
            );
           return false;  
        }
    });
});
