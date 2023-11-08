# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 21:52
# @Author  : liyang
# @FileName: conftest
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2022/06/14 12:21
# @Author  : liyang
# @FileName: conftest.py
# @Software: PyCharm

import pytest
from tools.yamlControl import Yaml_data
from config.base_dir import *

configure = Yaml_data().get_yaml_data(fileDir=config_url, isAll=True)
environment = configure[0]['environment']

# 自动化测试止执行前 -- 环境初始化操作
@pytest.fixture(scope="session",autouse=True)        #function（测试函数级别），class（测试类级别），module（测试模块“.py”级别），session（多个文件级别）。默认是function级别
def start_running():
    print(f'--- 马上开始执行自动化测试, 当前环境为：{environment} ---')
    yield   # 通过yield来唤醒teardown执行
    print('\n---自动化测试完成,开始处理本次测试数据---')


# 自动化测试止执行后 -- 数据清除操作


# fixture固件
@pytest.fixture(scope="session",autouse=False)
def connetion_mysql():
    print(f'--- 马上开始执行自动化测试, 当前环境为：{environment} ---')
    yield   # 通过yield来唤醒teardown执行
    print('\n---自动化测试完成,开始处理本次测试数据---')

# 在测试用例中手动调用 connetion_mysql 该方法

@pytest.fixture(scope="session",autouse=False,params=["mysql","redis"])    # params 用法
def connetion_mysql(request):        # request 固定参数
    print(f'--- 马上开始执行自动化测试, 当前环境为：{environment} ---')
    yield request.param  # 通过yield固定返回 request.param
    print('\n---自动化测试完成,开始处理本次测试数据---')


def test_case1(self, connetion_mysql):
    url = ""
    data = ""
    return None


@pytest.fixture(scope="session",autouse=False,name='cm')   # name 夹具别名
def connetion_mysql():     # 夹具
    print(f'--- 马上开始执行自动化测试, 当前环境为：{environment} ---')
    yield   # 通过yield来唤醒teardown执行
    print('\n---自动化测试完成,开始处理本次测试数据---')

def test_case2(self, cm):   # name 夹具取了别名后，只能用别名不能用原来的名称
    url = ""
    data = ""
    return None