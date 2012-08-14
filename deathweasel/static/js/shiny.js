$(document).ready(function() {
    $('a.commentlink').click(
        function() {
         var id = $(this).attr('id');
         var link = "/artwork/comments/" + id;
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


