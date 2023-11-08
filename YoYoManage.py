# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 15:36
# @Author  : taiyang
# @FileName: YoYoManage
# @Software: PyCharm

# from __future__ import annotations
# import cx_Oracle
import requests
import time
# import arrow
# import os
# import sys
# sys.path.append(os.getcwd())
from config.base_dir import *
from tools.yamlControl import Yaml_data
from OracleFunc import OracleFunc


class yoyoManage(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, oracle_info):
        self.url = 'https://yolinkcs.quanyou.com.cn'
        self.sql = OracleFunc(oracle_info)
        self.session = requests.session()
        self.yaml = Yaml_data()

    def bf_request(self, method, url, head=None, data=None, *args, **kwargs):
        '''
        请求方法
        :param method:
        :param url:
        :param head:
        :param data:
        :param args:
        :param kwargs:
        :return:
        '''
        method = method.lower()
        if method == 'get':
            for loop in range(1,4):
                try:
                    b_request = requests.get(url=url, headers=head, params=data, timeout=600)
                    if b_request.status_code != 200:
                        raise AssertionError(f'请求超时:{loop}次,{b_request.json()}')
                    else:
                        return b_request
                except ConnectionError:
                    time.sleep(2)
                    continue
                except Exception as e:
                    raise AssertionError(f'当前接口接口调用失败，请求检查接口,失败信息：{e}')

        elif method == 'post':
            for loop in range(1,4):
                try:
                    b_request = requests.post(url=url, headers=head, json=data, timeout=600)
                    if b_request.status_code != 200:
                        raise AssertionError(f'请求超时:{loop}次,{b_request.json()}')
                    else:
                        return b_request
                except ConnectionError:
                    time.sleep(2)
                    continue
                except Exception as e:
                    raise AssertionError(f'当前接口接口调用失败，请求检查接口,失败信息：{e}')

    def login_background(self, uname, password, appcode, *args, **kwargs):
        '''
        登录后台
        :param uname:
        :param password:
        :param appcode:
        :param args:
        :param kwargs:
        :return:
        '''
        url = self.url + '/gw/qu-platform-auth-api/auth/tokenWithAD'
        head = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Length": "78",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        data = {"userName": uname, "password": password, "appCode": appcode}
        # print(data)
        # print(url)
        for loop in range(4):
            try:
                rsp = self.session.post(url, headers=head, json=data).json()
                if rsp['message'] == '域账号或密码错误！':
                    print("登录失败,原因：" + rsp['message'])
                elif rsp['message'] != "success":
                    raise AssertionError("登录失败,原因：" + rsp["message"])
                else:
                    self.Authorization = rsp['data']['token']
                    return self.Authorization

            except ConnectionError:
                time.sleep(2)
                continue

    # def get_client_user_token(self, request_method='get', request_url=ip_address + '/creditUser/getUserAmount', request_body={}):
    #     '''
    #     使用token通过调接口判断token是否过期，若过期则获取新的token
    #     :param request_method:
    #     :param request_url:
    #     :param request_body:
    #     :return:
    #     '''
    #     try:
    #         tokenList = self.yaml.read_yaml_file(yaml_file=client_token_url)
    #         token_list = []
    #         for item in tokenList:
    #             token_list.append(item['token'])
    #
    #         for token in token_list:
    #             head = {"Accept-Encoding": "gzip, deflate",
    #                 "Accept-Language": "zh-CN,zh;q=0.9",
    #                 "Connection": "keep-alive",
    #                 "accessCode": token,
    #                 "lang": "ZH",
    #                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    #             self.bf_request(method=request_method, url=request_url,head=head, data=request_body).json()
    #         print(f"token未过期,直接取yaml文件的token：{token_list}")
    #
    #         return token_list
    #     except:
    #         # token过期,清除文件后重新获取token并写入yaml文件
    #         Yaml_data().clear_yaml_file(yaml_file=client_token_url)
    #
    #         user_list = self.yaml.read_yaml_file(yaml_file=client_user_url)
    #         for username in user_list:
    #             token_str = self.login_background(uname='huangchaoyang3', password='12345678a.', appcode='yoyo-manager')
    #             Yaml_data().write_yaml_file(yaml_file=client_token_url, data=[{'token': f'{token_str}'}])
    #
    #         # 再读取yaml文件中的token
    #         new_list = Yaml_data().read_yaml_file(yaml_file=client_token_url)
    #         token_list = []
    #         for item in new_list:
    #             token_list.append(item['token'])
    #
    #         print(f'赔率已过期,获取新token列表:{token_list}')
    #
    #         return token_list


    def user_manager(self, nickName="",employeeNo="",workStatus='',orgId=1, pageNum=1, pageSize=30, *args, **kwargs):
        '''
        人员管理查询
        :param nickName:
        :param employeeNo:
        :param workStatus:
        :param orgId:
        :param pageNum:
        :param pageSize:
        :param args:
        :param kwargs:
        :return:
        '''
        token = self.login_background(uname='huangchaoyang3', password='12345678a.', appcode='yoyo-manager')
        url = self.url + '/gw/yoyo-manager/user/pageList'
        head = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Length": "78",
            "Authorization": token,
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        data = {"pageNum":pageNum,"pageSize":pageSize,"workStatus":workStatus,
                "orgId":orgId,"nickName":nickName,"employeeNo":employeeNo}
        rsp = self.session.post(url, headers=head, json=data).json()
        # print(rsp)
        if rsp['message'] != 'success':
            raise AssertionError("接口查询失败,原因：" + rsp["message"])
        elif rsp['data']['list'] == []:
            print('查询接口为空')
        else:
            user_list = rsp['data']['list']
            # print(user_list)
            user_info = []
            for userInfo in user_list:
                if 'workJobs' not in userInfo:
                    workJobs = ""
                else:
                    workJobs = userInfo['workJobs']
                imOrgId = userInfo['imOrgId']
                sql_str = f"select FULL_PATH from YOLINK.IM_ORGANIZATION where ORG_ID='{imOrgId}'"
                result =self.sql.query_data(sql=sql_str, db_name='YOLINK')
                imorgPath = result[0][0]
                user_info.append({'nickName':userInfo['nickName'],'employeeNo':userInfo['employeeNo'],'orgPath':userInfo['orgPath'],'workJobs':workJobs,
                                  'workStatus':userInfo['workStatus'],'disabled':userInfo['employeeNo'],'isOpenVideo':userInfo['employeeNo'],'isOpenVoice':userInfo['isOpenVoice'],
                                  'maxTime':userInfo['maxTime'],'usedTime':userInfo['usedTime'],'fullPathList':userInfo['fullPathList'],'imorgPath':imorgPath})
            return user_info




if __name__ == "__main__":



    # dataBase_configure = CommonFunc().get_dataBase_environment_config()
    # mysql_info = dataBase_configure[0]
    # mongo_info = dataBase_configure[1]
    # configure = Yaml_data().get_yaml_data(fileDir=config_url, isAll=True)
    # environment = configure[0]['environment']
    # print(f'--- 当前系统环境为：{environment} ---')

    oracle_info = ('dataquery', 'Qy_dataq#2023', '172.31.12.211/yolink', 'UTF-8')
    yoyo = yoyoManage(oracle_info)            # 创建对象

    # token= yoyo.login_background(uname='huangchaoyang3', password='12345678a.', appcode='yoyo-manager')
    token= yoyo.user_manager(nickName="黄朝阳",employeeNo="",workStatus='')