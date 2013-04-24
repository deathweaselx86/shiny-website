function submitForm()
{
    Dajaxice.posts.add_comment(Dajax.process, {"form":$("#commentform").serialize(true)});
}

function commentStatus(status_msg)
{
    $("#commentstatus").append(status_msg);
    $("#commentform").slideUp();
    $("h4").slideUp();
}

$(document).ready(function() {
    $('button#showcomments').click(
        function(event) {
            event.preventDefault();
            showComments();
        });
    $("button#commentsubmit").click( function(event){ event.preventDefault(); submitForm(); showComments();} );
});

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

