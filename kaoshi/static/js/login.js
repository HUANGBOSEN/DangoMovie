function check() {
    var password=$('#two').val();
    var newpwd=md5(password);
    $('#two').val(newpwd);
    return true;

}