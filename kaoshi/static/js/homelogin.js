$(function () {
    $('.shouc').click(function () {
        console.log('123123')
        var movieid=$(this).attr('movieid');
        console.log('123')
        var b =$(this);
        $.getJSON('/one/wodesc',{'movieid':movieid},function (data) {
            // /home/huangbosen/Xiangmu/lianxi6
            if(data['msg'] == 'ok'){
               $(b).next('#tishi').html('收藏成功');
               $(b).next('#tishi').css('color','#000000');
                console.log(data['msg']);
            }else if (data['msg'] == 'no'){
                $(b).next('#tishi').html('请勿重复收藏');
                $(b).next('#tishi').css('color','#ff0000');
                console.log(data['msg']);
            }


        })

    })

})