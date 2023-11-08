# -*- coding: utf-8 -*-
"""
@Time ： 2023/10/21 14:48
@Auth ： 太阳
@File ：tideviceTools.py
@IDE ：PyCharm
"""

import os


#________________________________________tidevice基础封装______________________________________________
class Package_name(object):

    def __init__(self,device_id,name_list=None):
        self.device_id=device_id
        self.name_list=name_list


    def __call__(self, *args, **kwargs):
        '''列出设备的三方包名列表'''
        bb=os.popen('tidevice -u '+self.device_id+' applist').readlines()
        self.name_list=[ i[:i.find(' '):] for i in bb]
        return self.name_list


    def  is_no_package3_name(self,packeage_name):
        '''判断手机是否安装了xx包名'''
        return  True if  packeage_name  in self.name_list else False


    def  device_info(self):
        '''获取设备信息_dict格式'''
        bb=os.popen('tidevice -u '+self.device_id+' info').readlines()
        self.name_list=([''.join([i for i in price.replace("  ",'').split('\n')]) for price in bb])
        self.name_list.pop()
        json_a={}
        for i in self.name_list:
            aa=((i[:i.find(':'):]))
            bb=(i[i.find(':')+1:].lstrip())
            json_a[aa] = bb
        return json_a




if __name__=='__main__':
    test=Package_name('9592617d97b1d558ad4ced4a31cd0442762ffc05')
    print('以列表方式列出包名',test())

    print('判断设备是否安装xx包',test.is_no_package3_name('com.tencent.xin'))
    print('设备基础信息:',test.device_info())