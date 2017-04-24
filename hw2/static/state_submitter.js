var story = $("#current_story")
var corpus = ""
var seed = ""
var size = ""

function new_sentence(message){
    story.append("<p>"+ message +"</p>");
    if(story.children().length > 3){
        story.find(":first-child").remove();
    }
}
$(function() {
    $("#send").click(function (e) {
        corpus = $("#messenger").val();
        seed = $("#Seed").val();
        size = $("#size").val();

        setInterval(start_story, 5000);
    });
});

function start_story(){
    $.getJSON("/new_sentence", {"message": corpus, "seed":seed, "n": size}, 
        function(data){
            seed = data.seed; 
            new_sentence(data.next_sentence);
        }
    );
}
