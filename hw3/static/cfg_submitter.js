$(function() {
    //If the send button is clicked, start generating the story
    $("#submit").click(function (e) {
        e.preventDefault();
        var x = $("#messenger").val();
        $.get("/new_cfg", {"cfg":x}, function(data){
            $("#responses").prepend("<p>\n"+data+"\n</p>");
        });
    });
});
