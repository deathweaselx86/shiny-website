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
            showComments();
        });
    $("button#commentsubmit").click( 
        function(event){ 
            event.preventDefault(); submitForm(); showComments();
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


