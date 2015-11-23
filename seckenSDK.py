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


import requests, hashlib, time, random, string, rsa, base64, ast
from operator import itemgetter
import simplejson as json

class SeckenSDK(object):
	'''
	SeckenSDK类显示如何集成secken sdk服务
	'''
	def __init__(self, app_id, app_key, uid):
		self.url = 'https://api.sdk.yangcong.com'
		self.app_id = app_id.decode('utf-8')
		self.app_key = app_key.decode('utf-8')
		self.uid = uid.decode('utf-8')
		self.event_id = None

	def __get_signature(self, data):
		temp_data = sorted(data.iteritems(), key=itemgetter(0))
		sig_str = ''
		for key in temp_data:
			sig_str = sig_str + key[0] + '=' + key[1]
		sig_str = sig_str + self.app_key
		return hashlib.sha1(sig_str).hexdigest()
 
 	# 测试sdk api的连通性
	def testIndex(self):
		r = requests.get(self.url, timeout=10)
		if r.status_code == 200:
			print r.text

	# 获取二维码链接的地址及事件id
	def testQrcode4Auth(self, **params):
		if len(params) >= 0 and len(params) <= 4:
			for key in params:
				if key not in ['auth_type', 'action_type', 'action_details', 'callback']:
					print 'params error'
					return None
			params['app_id'] = self.app_id
			params['signature'] = self.__get_signature(params)
			r = requests.get(self.url+'/qrcode_for_auth', params=params, timeout=10)
			if r.status_code == 200:
				result = ast.literal_eval(r.text)
				if result['status'] == 200:
					self.event_id = result['event_id']
					return self.event_id, result['qrcode_url']
				else:
					return None
			else:
				return None

	# 获取推送验证的事件id
	def testRealAuth(self, **params):
		if len(params) >= 0 and len(params) <= 4:
			for key in params:
				if key not in ['auth_type', 'action_type', 'action_details', 'callback']:
					return 'params error'

			params['app_id'] = self.app_id
			params['uid'] = self.uid
			params['signature'] = self.__get_signature(params)
			r = requests.post(self.url+'/realtime_authorization', params=params, timeout=10)
			if r.status_code == 200:
				result = ast.literal_eval(r.text)
				if result['status'] == 200:
					self.event_id = result['event_id']
					return self.event_id
				else:
					return None
			else:
				return None

	# 测试授权验证的结果
	def testQueryAuthToken(self, auth_token):
		params = {'app_id': app_id, 'auth_token': auth_token}
		params['signature'] = self.__get_signature(params)
		r = requests.get(self.url+'/query_auth_token', params=params, timeout=10)
		if r.status_code == 200:
			return r.text

	# 测试事件结果
	def testEventResult(self):
		if not self.event_id:
			print 'event_id not exists'
			return None
		params = {'app_id': self.app_id, 'event_id': self.event_id}
		params['signature'] = self.__get_signature(params)
		r = requests.get(self.url+'/event_result', params=params, timeout=10)
		if r.status_code == 200:
			return r.text

if __name__ == '__main__':
	app_id = 'IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4'
	app_key = 'ELD0DNzMYep7m6Uo1v3v'
	uid = 'secken'

	obj = SeckenSDK(app_id, app_key, uid)

	obj.testIndex()
	print repr(obj.testQrcode4Auth())
	print obj.testRealAuth()
	print obj.testEventResult()
	print obj.testQueryAuthToken('asdasdasd')





