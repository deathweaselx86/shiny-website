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

    $("a#smallimagelink").click(
        function(event){
            event.preventDefault();
            var imageElement = $(".artimage").clone().removeClass();
            console.log(imageElement);
            $("#imagemodel").append(imageElement);
            console.log($("#imagemodal").append(imageElement));
            $("#imagemodal").dialog({modal: true,
                                    width: 1200,
                                    height: 1200});
        });

});

function showArtComments()
{
    showComments("artwork");
}


