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

import requests
import hashlib
import time
import random
import string
import rsa
import base64
import ast
from operator import itemgetter
import simplejson as json

API_URL = 'https://api.sdk.yangcong.com'
test_app_id = 'IXgdZ1A7CFUej2ytUbVjFJKS5ICiorw4'
test_app_key = 'ELD0DNzMYep7m6Uo1v3v'
test_uid = 'secken'
test_event_id = '1' * 40
test_auth_token = '1' * 40

DEFAULT_APP_ID = lambda x: x or test_app_id
DEFAULT_APP_KEY = lambda x: x or test_app_key
DEFAULT_UID = lambda x: x or test_uid
DEFAULT_EVENT_ID = lambda x: x or test_event_id
DEFAULT_AUTH_TOKEN = lambda x: x or test_auth_token

# 生成上传参数签名
def gen_signature(data_dict, app_key):
	'''
	generate a signature based on alphabetical order of data_dict's keys
	'''
	temp_data = sorted(data_dict.iteritems(), key=itemgetter(0))
	sig_str = ''
	for key in temp_data:
		sig_str = sig_str + key[0] + '=' + key[1]
	sig_str = sig_str + app_key
	return hashlib.sha1(sig_str).hexdigest()

# 测试sdk api的连通性
def test_service():
	r = requests.get(API_URL, timeout=10)
	if r.status_code == 200:
		print 'service work'
	else:
		print 'Oops!!! Sorrrry, service failed, retry later'

# 获取二维码链接地址及事件id
def test_qrcode_for_auth(app_id=None, app_key=None, **options):
	if len(options) > 4 or len(set(options.keys()) | set(['auth_type', 'action_type', 'action_details', 'callback'])) > 4:
		print 'param error'
		return

	params = options
	params['app_id'] = str(DEFAULT_APP_ID(app_id)).decode('utf8')
	app_key = str(DEFAULT_APP_KEY(app_key)).decode('utf8')
	params['signature'] = gen_signature(params, app_key)

	r = requests.get(API_URL+'/qrcode_for_auth', params=params, timeout=10)

	if r.status_code == 200:
		return r.text
	else:
		return None

# 获取推送验证的事件id
def test_realtime_auth(app_id=None, app_key=None, uid=None, **options):
	if len(options) > 4 or len(set(options.keys()) | set(['auth_type', 'action_type', 'action_details', 'callback'])) > 4:
		print 'param error'
		return

	params = options
	params['app_id'] = str(DEFAULT_APP_ID(app_id)).decode('utf8')
	params['uid'] = str(DEFAULT_UID(uid)).decode('utf8')
	app_key = str(DEFAULT_APP_KEY(app_key)).decode('utf8')
	params['signature'] = gen_signature(params, app_key)

	r = requests.post(API_URL+'/realtime_authorization', params=params, timeout=10)

	if r.status_code == 200:
		return r.text
	else:
		return None

# 测试查询事件结果
def test_event_result(app_id=None, app_key=None, event_id=None):
	params = {
			'app_id': str(DEFAULT_APP_ID(app_id)).decode('utf8'),
			'event_id': str(DEFAULT_EVENT_ID(event_id)).decode('utf8')
			}
	app_key = str(DEFAULT_APP_KEY(app_key)).decode('utf8')
	params['signature'] = gen_signature(params, app_key)

	r = requests.get(API_URL+'/event_result', params=params, timeout=10)

	if r.status_code == 200:
		return r.text
	else:
		return None


# 测试验证结果
def test_query_auth_token(app_id=None, app_key=None, auth_token=None):
	params = {
		'app_id': str(DEFAULT_APP_ID(app_id)).decode('utf8'),		
		'auth_token': str(DEFAULT_AUTH_TOKEN(auth_token)).decode('utf8')
	}
	app_key = str(DEFAULT_APP_KEY(app_key)).decode('utf8')
	params['signature'] = gen_signature(params, app_key)

	r = requests.get(API_URL+'/query_auth_token', params=params, timeout=10)

	if r.status_code == 200:
		return r.text
	else:
		return None





