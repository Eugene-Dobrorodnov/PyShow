$(document).ready(function() {
    $('form#create_comment_form input[type="submit"]').click(function(){
        var item_id   = $.trim($(this).parent('form').find('input[name = "item"]').val());
        var body_text = $.trim($(this).parent('form').find('textarea[name = "body"]').val());
        var action    = $(this).parent('form').attr('action')

        if( !item_id && !body_text && !action){
            return false
        }

        $.ajax({
            async:false,
            type:"POST",
            url:action,
            data:{
                item      : item_id,
                body      : body_text,
            },
            cache:false,
            success:function(data){
                var data = jQuery.parseJSON(data);
                console.log(data)
                if(data.status == 'ok'){

                    if( $('#comments_list span.comment_empty').length > 0  ){
                        $('#comments_list span.comment_empty').remove();
                    }

                    $('#comments_list').prepend('\n\
                    <div class="comment_box">\n\
                        <p>'+ body_text +'</p>\n\
                    </div>\n\
                    ');

                    $('form#create_comment_form textarea[name = "body"]').val('');;
                }

                if(data.status == 'error'){

                }
            },
            error:function(){
                alert('Что-то не так!')
            }
        });

        return false;
    });
});