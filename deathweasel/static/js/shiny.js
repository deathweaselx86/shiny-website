$(document).ready(function(){
    alert("Test");
});

$(document).ready(function() {
    $('.commentlink a').bind('click', function(id) {
            var link = "posts/comments/" + id;
            $('#this.id div').load(link);
            alert("Load comments for post " + id );
            return false;
        });
    });
