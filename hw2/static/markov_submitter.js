var story = "";
var corpus = "";
var seed = "";
var size = "";

$(function() {
    //If the send button is clicked, start generating the story
    $("#send").click(function (e) {
        e.preventDefault();
        story = $("#current_story");
        corpus = $("#messenger").val();
        seed = $("#seed").val();
        size = $("#size").val();

        start_story();
        setInterval(start_story, 5000);
    });
});

/*
 * Appends a new sentence to the page
 */
function new_sentence(message){
    //Append the next sentence to the current story
    story.find(":last-child").css("font-weight", "normal");
    story.append("<p>"+ message +"</p>");
    while(story.children().length > 3){
        story.find(":first-child").remove();
    }
    story.find(":last-child").css("font-weight", "bold");
}

/*
 * Gets the next sentence in the story, appends that to the page, and updates the seed.
 */
function start_story(){
    $.getJSON("/new_sentence", {"message": corpus, "seed":seed, "n": size}, 
        function(data){
            console.log(data);
            seed = data['seed']; 
            new_sentence(data['next_sentence']);
        }
    );
}
