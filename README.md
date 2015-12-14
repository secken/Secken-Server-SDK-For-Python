
# Secken Private Cloud Server SDK For Python v1.0.0

## 简介（Description）
Secken.Private.ServerSdk是Secken官方提供了一套用于和洋葱验证服务交互的SDK组件，通过使用它，您可以简化集成Secken服务的流程并降低开发成本。

密码就要大声说出来，开启无密时代，让密码下岗

洋葱是一个基于云和用户生物特征的身份验证服务。网站通过集成洋葱，可以快速实现二维码登录，或在支付、授权等关键业务环节使用指纹、声纹或人脸识别功能，从而彻底抛弃传统的账号密码体系。对个人用户而言，访问集成洋葱服务的网站将无需注册和记住账号密码，直接使用生物特征验证提高了交易安全性，无需担心账号被盗。洋葱还兼容Google验证体系，支持国内外多家网站的登录令牌统一管理。

【联系我们】

官网：https://www.yangcong.com

微信：yangcongAPP

微信群：http://t.cn/RLGDwMJ

QQ群：475510094

微博：http://weibo.com/secken

帮助：https://www.yangcong.com/help

合作：010-64772882 / market@secken.com

支持：support@secken.com

帮助文档：https://www.yangcong.com/help

项目地址：https://github.com/secken/Secken-Server-SDK-For-Python

洋葱SDK产品服务端SDK主要包含四个方法：
* 获取二维码的方法（GetYangAuthQrCode），用于获取二维码内容和实现绑定。
* 请求推送验证的方法（AskYangAuthPush），用于发起对用户的推送验证操作。
* 查询事件结果的方法（CheckYangAuthResult），用于查询二维码登录或者推送验证的结果。
* 复验验证结果的方法（CheckYangAuthToken），用于复验移动端SDK验证的结果。

## 安装使用（Install & Get Started）

洋葱私有云api demo的安装非常容易。请在[洋葱github](https://github.com/secken/Secken-Server-SDK-For-Python)下载文件，然后执行下面命令。

```
python setup.py install
```

## 更新发布（Update & Release Notes）

```
当前版本 v1.0.0
```

## 要求和配置（Require & Config）

当前适用版本python2.7

需要安装的依赖包

```
pip install requests --upgrade
```

## 获取二维码内容并发起验证事件（Get YangAuth QrCode）

链接地址：https://api.sdk.yangcong.com/qrcode_for_auth

qrcode_for_auth接口包含两个必传参数，app_id, signature。app_id是应用id, signature指的是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。可选参数包含auth_type(验证类型，1-一键确定，3-人脸，4-声纹)，action_type(动作类型)，action_details(动作详情)，callback(回调url链接)。

```
qrcode_for_auth(app_id='IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4', app_key='ELD0DNzMYep7m6Uo1v3v')
```

返回错误码信息

|    状态码   | 		状态详情 		  |
|:----------:|:-----------------:|
|  200       |       成功         |
|  400       |       上传参数错误  |
|  403       |       签名错误                |
|  404       |       应用不存在                |
|  407       |       请求超时                |
|  500       |       系统错误                |
|  609       |       ip地址被禁                |

## 查询验证事件的结果（Check YangAuth Result）

链接地址：https://api.sdk.yangcong.com/event_result

event_result接口包含三个必传参数，app_id，event_id和signature。app_id是应用id, event_id是事件和signature是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。

```
event_result(app_id='IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4', app_key='ELD0DNzMYep7m6Uo1v3v', \
            event_id='b17561423e972fba779be8a15b281eb57073f841')
```

返回错误码信息

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

## 发起推送验证事件（Ask YangAuth Push）

链接地址：https://api.sdk.yangcong.com/realtime_authorization

realtime_authorization接口包含两个必传参数，app_id, uid, signature。app_id是应用id, uid是指用户名, signature指的是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。可选参数包含auth_type(验证类型，1-一键确定，3-人脸，4-声纹)，action_type(动作类型)，action_details(动作详情)，callback(回调url链接)。

```
realtime_auth(app_id='IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4', app_key='ELD0DNzMYep7m6Uo1v3v', uid='user1')
```

返回错误码信息

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

## 复验验证结果的方法（Check YangAuth Token）

链接地址：https://api.sdk.yangcong.com/query_auth_token

query_auth_token接口包含三个必传参数，app_id, auth_token和signature。app_id是应用id，auth_token是验证token，一般由移动端人脸验证和声纹验证成功时候返回，signature是用户所有上传数据的签名。签名规则如seckenSDK.py的__get_signature()方法所示，按照键的字母顺序拼接成字符串，然后进行签名。

```
query_auth_token(app_id='IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4', app_key='ELD0DNzMYep7m6Uo1v3v', \
				auth_token='aee9ca0bbc9fb1711afcdc42cd83fb53616d317e')
```

返回错误码信息

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




