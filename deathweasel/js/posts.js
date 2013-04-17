$(document).ready(function() {
    $('a.postcomment').click(
        function() {
         var id = $(this).attr('id');
         var link = "/posts/comments/" + id;
         var element = 'a#'+id+'+ div';
         $(element).empty(); 
                $.ajax({
                    url: link,
                 }).done(function(html){
                     $(element).append(html);
                        });
                
             }

        );
    });

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
