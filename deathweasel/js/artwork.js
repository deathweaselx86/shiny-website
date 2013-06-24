function submitForm()
{
    Dajaxice.artwork.add_comment(Dajax.process, {"form":$("#commentform").serialize(true)});
}

function commentStatus(status_msg)
{
    $("#commentstatus").append(status_msg);
    $("#commentform").slideUp();
    $("h4").slideUp();
}

// This is used to load comments on the artwork details
// page.
$(document).ready(function() {
    $('button#showcomments').click(
        function(event) {
            event.preventDefault();
            showArtComments();
        });
    $("button#commentsubmit").click( 
        function(event){ 
            event.preventDefault(); submitForm(); showArtComments();
        } );

});

function showArtComments()
{
    showComments("artwork");
}


