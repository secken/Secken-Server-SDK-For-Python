$(function () {
	var isPass = false;

	function verify(eid) {
		var obj = {
			eid: eid
		}

		//var obj = {
		//	eid: eid,
		//	Action: "CheckYcAuthResult"
		//}
		//obj.t = (new Date()).getTime();
		$.getJSON("http://0.0.0.0:8080/event", obj, function (result) {
			if (!isPass) {
				if (result.status != "200") {
					if (result.status == "603") {
						stateChange("二维码过期,请<span class='hightLightSpan'>刷新</span>页面后重试")
							bindRefresh();
						isPass = true;
					} else if (result.status == "201" ) {
						stateChange("正在等待用户验证");
					} else if (result.status != "602") {
						stateChange("系统服务错误！");
						isPass = true;
					}
					if (!isPass) {
						setTimeout(verify(eid), 20000);
					}
				} else {
					isPass = true;
					window.location.href = "/push.html";
				}
			}
		});
	};

	stateChange("Is Loading QrCode...");
	//var obj = {
	//	Action: "GetYcAuthQrCode"
	//}
	//obj.t = (new Date()).getTime();
	var obj = {}
	$.getJSON("http://0.0.0.0:8080/qrcode", obj, function (result) {
		if (result.status == "200") {
			eid = result.event_id;
			$("#qr_img").attr("src", result.qrcode_url);
			hideState();
			verify(eid);
		} else if (result.code == "-1") {
			stateChange("获取失败!");
		}
	});

	Window.verifyOneClick = function () {
		var obj = {
			Action: "GetYcAuthOneClick"
		}
		obj.t = (new Date()).getTime();
		$.getJSON("/YcAuth.ashx", obj, function (result) {
			if (result.code == "0") {
				eid = result.event_id;
				hideState();
				verify(eid);
			} else if (result.code == "-1") {
				stateChange("获取失败!");
			}
		});
	}

	function bindRefresh() {
		$(".hightLightSpan").bind("click", function () {
			window.location.reload();
		});
	}
})

function stateChange(tip) {
	$(".qrCodeOverdue").html(tip);
	$(".qrCodeOverdue").show();
}

function hideState() {
	$(".qrCodeOverdue").hide();
}
