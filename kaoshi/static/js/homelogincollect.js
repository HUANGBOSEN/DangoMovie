$(function () {
    $('.delshouc').click(function () {
        console.log('123');
        var movieid = $(this).attr('movieid');
        var del=$(this);
        $.getJSON('/one/delwodesc', {'movieid': movieid}, function (data) {
            if (data['msg'] == 'ok') {
                del.parents('li').remove();
            }

        })

    })

})