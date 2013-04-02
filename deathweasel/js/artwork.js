function submitForm()
{
        Dajaxice.artwork.add_comment(Dajax.process, {'form':$("commentform").serialize(true)});
}


function handleFile(event) {
    var fileInput = event.currentTarget.files;
    console.log(fileInput);
    if (fileInput.length === 1){
        var file = fileInput[0];
        var output = "<br/>File attributes: <br/>";
        output += "name: " + file.name + "<br/>";
        output += "type: " + file.type + "<br/>";
        output += "size: " + (file.size/1024).toFixed(2) + "KB <br/>";
        output += "last modified: " + file.lastModifiedDate;
        $("#fileAttrs").html(output);    
    }
    else
    {
        $("#fileAttrs").text("Files interface is not supported by your browser.");
    }
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

// Use this to delete comments on the modification screen.
// Kind of broken right now.
$(document).ready(function() {
    var modifyCommentLink = $("a.artmodifycomment")[0];
    if (modifyCommentLink)
    {
        modifyCommentLink.click(
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
    }
    });

// This is used to validate comments on the comment forms.
// Hurray for jquery.validate
$(document).ready(function(){
//   $("#id_image").change({'file':'fileHandle'}, handleFile);

    var commentForm = $("#commentform")[0];
    if (commentForm){
        commentForm.validate({
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
    }
});

function validateCommentForm() {
    //$("#id_image").change({'file':'fileHandle'}, handleFile);
    var commentForm = $("#commentform")[0];
    if (commentForm){
        commentForm.validate({
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
    }
});


