$(function () {
    $('#exampleInputEmail1').blur(function () {
        console.log('22222222');
        // 失去焦点获取输入框的内容，然后将输入框的内容发送给服务器验证
        var uname=$(this).val();
        // 向服务器发送用户名进行验证
        $.getJSON('/one/jianceuser',{'uname':uname},function (data) {
            if(data['state'] == 200){
                $('#jiance_user').css('color','#00ff00');
            }else if (data['state'] == 201){
                $('#jiance_user').css('color','#ff0000');
            }
            console.log('33333333');
            $('#jiance_user').html(data['msg']);

        })
    })
})
function check() {
    var pwd1=$('#password1').val();
    var pwd2=$('#password2').val();
    if (pwd1 == pwd2){
        $('#jiance_psd').html('两次输入的密码一致');
        $('#jiance_psd').css('color','green');
    }
    else {
        $('#jiance_psd').html('两次输入的密码不一致');
        $('#jiance_psd').css('color','red');
        return false
    }
    var newpwd=md5(pwd1);
    $('#password1').val(newpwd);
    return true
}