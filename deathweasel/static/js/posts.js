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

