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
$(document).ready(function() {
    var artCommentLink = $("a.artcomment")[0];
    if (artCommentLink) {    
        $('a.artcomment').click(
            function(event) {
            event.preventDefault();
            var id = $(this).attr('id');
             var link = "/artwork/comments/" + id;
             var element = "div#comments";
            $(element).empty(); 
             $.ajax({
                url: link,
             }).done(function(html){
                 $(element).append(html);
                    });
            $('a.artcomment').hide();
            });}
});


