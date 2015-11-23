seckenSDK
==============

洋葱私有云api主要提供二维码及推送验证等功能，主要用于触发移动端的身份验证。所有洋葱私有云api的服务都是以https接口形式提供。目前洋葱私有云api主要包含两大类接口，触发事件接口和事件查询接口。触发事件接口包含二维码授权(qrcode_for_auth)和推送验证(realtime_authorization)。事件查询接口包含事件结果查询(event_result)和验证结果查询(query_auth_token)。

## 安装

洋葱私有云api demo的安装非常容易。请在[洋葱github](https://www.yangcong.com)下载文件，然后执行下面命令。

```
python setup.py install
```

## 快速开始

为了能使客户最快程度上使用和集成洋葱服务，洋葱专门提供给用户测试帐号：

* app_id: IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4
* app_key: ELD0DNzMYep7m6Uo1v3v
* uid: secken

```
from seckenSDK import SeckenSDK

# 初始化洋葱私有云api demo
s = SeckenSDK(app_id, app_key, uid)

# 测试洋葱私有云api服务是否开启
s.testIndex()
```
```
# 返回二维码链接地址并返回该事件id
s.testQrcode4Auth(auth_type=1, action_type=u'登录验证'，action_details=u'某某服务的登录')
```
qrcode_for_auth接口包含两个必传参数，app_id, signature。app_id是应用id, signature指的是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。可选参数包含auth_type(验证类型，1-一键确定，3-人脸，4-声纹)，action_type(动作类型)，action_details(动作详情)，callback(回调url链接)。

|    状态码   | 		状态详情 		  |
|:----------:|:-----------------:|
|  200       |       成功         |
|  400       |       上传参数错误  |
|  403       |       签名错误                |
|  404       |       应用不存在                |
|  407       |       请求超时                |
|  500       |       系统错误                |
|  609       |       ip地址被禁                |


```
# 返回推送验证的事件id
s.testRealAuth()
```

realtime_authorization接口包含两个必传参数，app_id, uid, signature。app_id是应用id, uid是指用户名, signature指的是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。可选参数包含auth_type(验证类型，1-一键确定，3-人脸，4-声纹)，action_type(动作类型)，action_details(动作详情)，callback(回调url链接)。

|    状态码   | 		状态详情 		  |
|:----------:|:-----------------:|
|  200       |       成功         |
|  400       |       上传参数错误  |
|  403       |       签名错误                |
|  404       |       应用不存在                |
|  407       |       请求超时                |
|  500       |       系统错误                |
|  605       |       无验证类型                |
|  607       |       该用户不存在                |
|  609       |       ip地址被禁                |


```
# 查询事件处理结果，采用轮询办法
s.testEventResult()
```
event_result接口包含三个必传参数，app_id，event_id和signature。app_id是应用id, event_id是事件和signature是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。

|    状态码   | 		状态详情 		  |
|:----------:|:-----------------:|
|  200       |       成功         |
|  201       |       事件已被处理                |
|  400       |       上传参数错误  |
|  403       |       签名错误                |
|  404       |       应用不存在                |
|  407       |       请求超时                |
|  500       |       系统错误                |
|  601       |       用户拒绝                |
|  602       |       用户还未操作                |
|  604       |       事件不存在                |
|  606       |       callback已被设置                |
|  609       |       ip地址被禁                |


```
# 查询授权验证的结果，auth_token由移动端人脸声纹验证成功后提供
s.testQueryAuthToken(auth_token)
```

query_auth_token接口包含三个必传参数，app_id, auth_token和signature。app_id是应用id，auth_token是验证token，一般由移动端人脸验证和声纹验证成功时候返回，signature是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。

|    状态码   | 		状态详情 		  |
|:----------:|:-----------------:|
|  200       |       成功         |
|  400       |       上传参数错误  |
|  403       |       签名错误                |
|  404       |       应用不存在                |
|  407       |       请求超时                |
|  500       |       系统错误                |
|  608       |       验证token不存在           |
|  609       |       ip地址被禁                |






