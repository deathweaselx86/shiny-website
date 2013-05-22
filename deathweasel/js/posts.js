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
            showPostComments();
        });
    $("button#commentsubmit").click( function(event){ event.preventDefault(); submitForm(); showPostComments();} );
});


function showPostComments()
{
    showComments("posts");
}

