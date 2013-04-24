function submitForm()
{
    Dajaxice.posts.add_comment(Dajax.process, {"form":$("#commentform").serialize(true)});
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

// This really can be made into one function that operates on
// posts and artwork.
function showComments()
{
    var button = $("button#showcomments");
    var id = $("#id_post").attr("value");
    var link = "/posts/comments/" + id;
    var element = "section#comments";
    $(element).empty(); 
    $.ajax({url: link,}).done(
            function(html){
                $(element).append(html);});
    button.hide();
}

/*
$(document).ready(function(){

    $("#commentform").validate({
        submitHandler: 
            function(form){
                var pk = $("div#pk").attr('name');
                var formValues = $(form).serialize();
                $.post("/posts/comments/add/" + pk +"/",
                      formValues,
                      function()
                      {
                          $("section.addcomment").empty();
                          $("section.addcomment").attr("<h2>Thanks!</h2>");
                          $("section.addcomment").hide('fast');
                      });
        }
    });
    $("#id_title").rules("add", {
        required: true,
        maxlength: 250});
    $("#id_author").rules("add", {
        required: true,
        maxlength: 200});
    $("#id_body").rules("add", {
        required: true,
        maxlength: 500});
});
*/
