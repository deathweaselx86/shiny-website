$(document).ready(function() {
    $("button").button(); 
    $('button#showcomments').click(
        function(event) {
            event.preventDefault();
            showComments();
        });
    $("button#commentsubmit").click( function(event){ event.preventDefault(); submitForm();} )
});

