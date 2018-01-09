function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function () {
    $("#login").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username": user, "password": pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type: "post",
            url: "/login",
            data: pd,
            cache: false,
            success: function (data) {
                if (data != "welcome!")
                    alert(data)
                else
                    window.location.href = "/user?user=" + user

            },
            error: function () {
                alert("error!");
            },
        });
    });


    $("#regist").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username": user, "password": pwd};
        $.ajax({
            type: "post",
            url: "/regist",
            data: pd,
            cache: false,
            success: function (data) {
                alert(data)
            },
            error: function () {
                alert("error!");
            },
        });
    });
})