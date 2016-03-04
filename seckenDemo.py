# coding=u8
# Copyright 2014-2015 Secken, Inc.  All Rights Reserved.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# NOTICE:  All information contained herein is, and remains
# the property of Secken, Inc. and its suppliers, if any.
# The intellectual and technical concepts contained
# herein are proprietary to Secken, Inc. and its suppliers
# and may be covered by China and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Secken, Inc..
#
# 注意：此处包含的所有信息，均属于Secken, Inc.及其供应商的私有财产。
# 此处包含的所有知识、专利均属于Secken, Inc.及其供应商，属于商业秘密，
# 并受到中国和其他国家的法律保护。这些信息及本声明，除非事先得到
# Secken, Inc.的书面授权，否则严禁复制或传播。
#
# @author     Chen Yiping
# @version    1.0.0
#
# 此文件为临时文件，主要内容在seckenSDK.py中


import web

urls = (
	'/qrcode',	'Qrcode',
	'/push',	'Push',
	'/event',	'GetEvent'
)

render = web.template.render('templates')


class Push:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		result = test_realtime_auth()
		return result

class Qrcode:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		result = test_qrcode_for_auth()
		return result

class GetEvent:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		event_id = web.input().get('eid', '')
		result = test_event_result(event_id=event_id)
		return result

app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()
