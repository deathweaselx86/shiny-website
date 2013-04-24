function submitForm()
{
    Dajaxice.artwork.add_comment(Dajax.process, {"form":$("#commentform").serialize(true)});
}

function commentStatus(status_msg)
{
    $("#commentstatus").append(status_msg);
    $("#commentform").slideUp();
    $("h4").slideUp();
    $("#commentform").remove();
}

// This is used to load comments on the artwork details
// page.


function showComments()
{
    var button = $("button#showcomments");
    var id = $("#id_artwork").attr("value");
    var link = "/artwork/comments/" + id;
    var element = "section#comments";
    $(element).empty(); 
    $.ajax({url: link,}).done(
            function(html){
                $(element).append(html);});
    button.hide();
}


