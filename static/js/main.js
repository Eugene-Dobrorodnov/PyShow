function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

$(document).ready(function() {
    //говеное модальное окно
    $('a[name=modal]').click(function(e) {
        e.preventDefault();
        var id = $(this).attr('href');
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
        $('#mask').css({'width':maskWidth,'height':maskHeight});
        $('#mask').fadeIn(1000);
        $('#mask').fadeTo("slow",0.8);
        var winH = $(window).height();
        var winW = $(window).width();
        $(id).css('top',  winH/2-$(id).height()/2);
        $(id).css('left', winW/2-$(id).width()/2);
        $(id).fadeIn(2000);
    });
    $('.window .close').click(function (e) {
    e.preventDefault();
        $('#mask, .window').hide();
    });
    $('#mask').click(function () {
        $(this).hide();
        $('.window').hide();
    });

    //Аутентификация пользователя
    $('#login_form input[type="submit"]').click(function(){
        var user_name = $.trim($(this).parent('form').find('input[name="username"]').val());
        var password  = $.trim($(this).parent('form').find('input[name="password"]').val());
        var action    = $(this).parent('form').attr('action')

        if(!user_name && !password){
            $('#login_form input[name="username"]').addClass('error');
            $('#login_form input[name="password"]').addClass('error');
            return false;
        }

        $.ajax({
            async:false,
            type:"POST",
            url:action,
            data:{
                username : user_name,
                password : password
            },
            cache:false,
            success:function(data){
                var data = jQuery.parseJSON(data);

                if(data.status == 'ok'){
                    window.location = window.location.href;
                }

                if(data.status == 'error'){
                    $('#login_form input[name="username"]').addClass('error');
                    $('#login_form input[name="password"]').addClass('error');
                }
            }
        });
        return false;
    });

    //Регистрация пользователя
    $('#registration_form input[type="submit"]').click(function(){
        var user_name  = $.trim($(this).parent('form').find('input[name="username"]').val());
        var password1  = $.trim($(this).parent('form').find('input[name="password1"]').val());
        var password2  = $.trim($(this).parent('form').find('input[name="password2"]').val());
        var action     = $(this).parent('form').attr('action')

        if(!user_name && !password1 && !password2){
            $('#registration_form input[name="username"]').addClass('error');
            $('#registration_form input[name="password1"]').addClass('error');
            $('#registration_form input[name="password2"]').addClass('error');
            return false;
        }

        if(password1 != password2){
            $('#registration_form input[name="password1"]').val('')
            $('#registration_form input[name="password2"]').val('')
            $('#registration_form input[name="password1"]').attr("placeholder", "The two password fields didn't match.")
            $('#registration_form input[name="password2"]').attr("placeholder", "The two password fields didn't match.")
            $('#registration_form input[name="password1"]').addClass('error');
            $('#registration_form input[name="password2"]').addClass('error');
            return false;
        }

        $.ajax({
            async:false,
            type:"POST",
            url:action,
            data:{
                username  : user_name,
                password1 : password1,
                password2 : password2,
            },
            cache:false,
            success:function(data){
                var data = jQuery.parseJSON(data);

                if(data.status == 'ok'){
                    window.location = window.location.href;
                }

                if(data.status == 'error'){
                    $.each(data.errors, function(i, value){
                        $('#registration_form input[name="'+i+'"]').addClass('error');
                        $('#registration_form input[name="'+i+'"]').val('')
                        $('#registration_form input[name="'+i+'"]').attr("placeholder", value);
                        if(i == 'password2'){
                            $('#registration_form input[name="password1"]').attr("placeholder", value);
                            $('#registration_form input[name="password1"]').val('');
                        }

                    });
                }
            }
        });
        return false;
    });
});