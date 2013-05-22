$(document).ready(function() {
    $("button").button(); 
});

function addNewComment(json)
{
    var commentObj = $.parseJSON(json);
    console.log(json);
    console.log(commentObj);
}

function showComments(type)
{
    if (type == "posts"){
        var inputId = "#id_post"; }
    else if (type == "artwork"){
        var inputId = "#id_artwork" }
    else {
        throw "Invalid comment type: " + type
    }
    
    var button = $("button#showcomments");
    var itemId = $(inputId).attr("value");
    var link = "/" + type+ "/comments/" + itemId;
    var element = "section#comments";
    $(element).empty(); 
    $.ajax({url: link,}).done(
            function(html){
                $(element).append(html);});
    button.hide();
}

