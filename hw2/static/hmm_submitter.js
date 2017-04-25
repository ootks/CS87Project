$(function() {
    //If the send button is clicked, start generating the story
    $("#send").click(function (e) {
        e.preventDefault();
        $.get("/new_hmm_poem", function(data){
            $("#poem").prepend("<p>\n"+data+"\n</p>");
        });
    });
});
