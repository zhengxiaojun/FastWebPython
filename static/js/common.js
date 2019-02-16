function sendpost() {
    // var code = document.getElementById("code").value;
    var code = editor.getValue();
    $.ajax({
        url: "index",
        type: 'post',
        dataType: 'html',
        data: {"code": code},
        beforeSend: function () {
            $("#run").attr({disabled: "disabled"});
            loaddiv = '<div id="pload" style="position:fixed;top:30%;z-index:1200;background:url(/static/img/loading2.gif) top center no-repeat;width:100%;height:140px;margin:auto auto;" aria-hidden="true"></div>'
            $("body").append(loaddiv);
        },
        complete: function () {
            $("#run").removeAttr("disabled");
            $("#pload").remove();
        },
        success: function callbackFun(data) {
            data = JSON.parse(data);
            $('#status').html(data["status"]);
            $('#output').html(data["output"]);
            $('#version').html(data["version"]);
        },
        error: function callbackErr() {
            document.getElementById("output").value = "未知错误.";
        }
    });

}