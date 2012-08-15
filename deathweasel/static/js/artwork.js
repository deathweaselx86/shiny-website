$(document).ready(function() {
    $('a.artcomment').click(
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
        $('a#'+id).hide();
             }

        );
    });

$(document).ready(function() {
    $("a.artmodifycomment").click(
        function() {
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



