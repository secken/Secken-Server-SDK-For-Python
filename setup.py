#coding=u8

from setuptools import setup, find_packages
setup(
	name='seckenSDK',
	version='1.0.0',
	description='an instance of secken sdk integration',
	author='Secken',
	url='http://www.secken.com',
	license='LGPL',
	packages=find_packages(),
	scripts=['seckenSDK.py'],
	py_modules=[]
)