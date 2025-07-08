//alert 获取信息
// alert("register.js")
function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function(event){
        //获取对象得到对应的文本内容
        //$this：代表的是当前按钮的jquery对象
        var $this = $(this)
        //阻止默认事件
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            url: '/author/captcha/email?email='+email,
            method:'GET',
            success: function(result){
                var code = result['code'];
                if(code ==200){
                    //设置一个倒计时
                    var countdown = 10;
                    //开始倒计时之前，取消在此期间的点击功能
                    $this.off("click");
                    //实时更新倒计时，1000毫秒
                    var timer = setInterval(function(){
                        $this.text(countdown)
                        countdown -= 1
                        //倒计时结束后执行
                        if(countdown <=0){
                            //清掉定时器
                            clearInterval(timer);
                            //将按钮的文字重新修改回来
                            $this.text("获取验证码");
                            //重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    },1000);
                    alert('邮箱验证码发送成功！')
                }else{
                    alert(result['message']);
                }
            },
            fail: function(error){
                console.log(error);
            }
        })
    });
}

//整个网页加载完毕之后在执行的
$(function(){
    bindEmailCaptchaClick();
});