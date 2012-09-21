$(document).ready(function() {
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
             }

        );
    });

// Use this to delete comments on the modification screen.
// Kind of broken right now.
$(document).ready(function() {
    $("a.artmodifycomment").click(
        function(event) {
         event.preventDefault();
         var key = $(this).attr('id');
         var link = "/artwork/comments/deletable/" + key;
         var element = 'a.artmodifycomment+'+ 'div';
         $(element).empty(); 
                $.ajax({
                    url: link,
                 }).done(function(html){
                     $(element).append(html);
                        });
        $("a.artmodifycomment").hide();
             }

        );
    });

// Hurray for jquery.validate
$(document).ready(function(){

    $("#commentform").validate({
        submitHandler: 
            function(form){
                var pk = $("div#pk").attr('name');
                var formValues = $(form).serialize();
                $.post("/artwork/comments/add/" + pk +"/",
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

