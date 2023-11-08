# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/24 17:05
@Auth ： 太阳
@File ：test.py
@IDE ：PyCharm
"""
# import cx_Oracle
# # dsn_tns = cx_Oracle.makedsn('172.30.4.181', 1521, service_name = 'bp')
# # connection = cx_Oracle.connect('YOLINK', 'Qy_yok#2022', dsn_tns)
# dsn_tns = cx_Oracle.makedsn('172.31.12.211', 1521, service_name ='yolink')
# connection = cx_Oracle.connect(user='dataquery', password='Qy_dataq#2023', dsn=dsn_tns)
# # import cx_Oracle
# #
# # # 连接Oracle数据库
# # connection = cx_Oracle.connect("dataquery/Qy_dataq#2023/jdbc:oracle:thin:@//172.31.12.211:1521/yolink")
# # connection = cx_Oracle.connect(user="dataquery",password="Qy_dataq#2023",cx_Oracle.makedsn=("jdbc:oracle:thin:@//172.31.12.211:1521/yolink"))
# # connection = cx_Oracle.connect('dataquery',"Qy_dataq#2023",dsn_tns)
# print('连接成功')
# # 创建游标对象
# cursor = connection.cursor()
#
# # 查询数据表
# cursor.execute("SELECT * FROM YOLINK.IM_USER_INFO where USER_ID=644333")
# results = cursor.fetchall()
#
# # 输出查询结果
# for row in results:
#     print(row)
#
# # 关闭游标对象和数据库连接
# cursor.close()
# connection.close()



# import os
# import sys
# # import arrow
# import cx_Oracle
# import datetime
# import calendar
# from decimal import *
# import requests
# import time
# from itertools import chain
# from log_utils.log import Bf_log
# import re
# from decimal import Decimal
# from itertools import combinations
# from functools import reduce
# from operator import itemgetter
# from itertools import groupby
# try:
#     from common.CommonFunc import CommonFunc
# except ModuleNotFoundError or ImportError:
#     from .common.CommonFunc import CommonFunc
#
# try:
#     if sys.platform.startswith("darwin"):
#         lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
#                                "instantclient_19_8")
#         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
#     elif sys.platform.startswith("win32"):
#         lib_dir=r"C:\oracle\instantclient_19_9"
#         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
# except Exception as err:
#     print("Whoops!")
#     print(err)
#     sys.exit(1)
#
#
# class OracleFunc(object):
#     ROBOT_LIBRARY_SCOPE = 'GLOBAL'
#
#     def __init__(self, oracle_info, *args, **kwargs):
#         '''
#         使用connect创建连接对象
#         connect.cursor创建游标对象，SQL语句的执行基本都在游标上进行
#         cursor.executeXXX方法执行SQL语句，cursor.fetchXXX获取查询结果等
#         调用close方法关闭游标cursor和数据库连接
#         :param mysql_info:
#         :param mongo_info:  business_order
#         :param args:
#         :param kwargs:
#         '''
#         self.connect = cx_Oracle.connect(user=oracle_info[0], password=oracle_info[1], dsn=oracle_info[2],
#                                        charset='utf8',autocommit=True)
#
#         # self.tm = Third_Merchant(mysql_info, host='http://192.168.10.11')
#         self.cursor = self.connect.cursor()
#
#     # 关闭数据库
#     def close_db(self):
#         """
#         关闭数据库
#         :return:
#         """
#         self.cursor.close()
#         self.connect.close()
#
#     def query_data(self, sql, db_name='YOLINK'):
#         """
#         数据查询
#         :param sql:
#         :param db_name:
#         :return:
#         """
#         try:
#             self.change_db(db_name)
#             self.cursor.execute(sql)
#             res = self.cursor.fetchall()
#         except cx_Oracle.Error as e:
#             print(e)
#             print(AssertionError, "查询结果为空")
#             return
#         return res
#
#     def update_data(self, sql, db_name='YOLINK'):
#         """
#         修改
#         :param sql:
#         :param db_name:
#         :return:
#         """
#         try:
#             self.change_db(db_name)
#             self.cursor.execute(sql)
#             self.connect.commit()
#         except Exception:
#             raise(AssertionError, "修改失败！")
#
#     def insert_data(self, sql, db_name='YOLINK'):
#         """
#         插入
#         :param sql:
#         :param db_name:
#         :return:
#         """
#         try:
#             self.change_db(db_name)
#             self.cursor.execute(sql)
#             self.connect.commit()
#         except Exception:
#             raise (AssertionError, "插入数据失败！")
#
#     def change_db(self, db_name):
#         try:
#             self.connect.select_db(db_name)
#         except Exception as e:
#             print(e)
#
#     def delete_all_data_of_table(self, table_name, db_name="YOLINK"):
#         """
#         删除报表中的表数据
#         :param table_name:
#         :param db_name:
#         :return:
#         """
#         table_name_dic = {"日": "biz_agent_day_record",
#                           "月": "biz_agent_month_record",
#                           "年": "biz_agent_year_record",
#                           "联赛": "league_record",
#                           "比赛": "match_record",
#                           "玩法": "handicap_record",
#                           "串关": "multip_record",
#                           "滚球": "rolling_record"}
#         self.query_data("delete from %s" % table_name_dic[table_name], db_name)
#
#
# class OracleQuery(OracleFunc):
#     ROBOT_LIBRARY_SCOPE = 'GLOBAL'
#
#     # 如果在子类中定义构造方法(等同于重写第一个直接父类的构造方法), 则必须在该方法中调用父类的构造方法
#     def __init__(self, oracle_info, *args, **kwargs):
#         self.cf = CommonFunc()
#
#         # 子类中的构造方法中,调用父类构造方法的方式有 2 种
#         super().__init__(oracle_info, *args, **kwargs)          # 使用 super() 函数
#         # MysqlFunc.__init__(self, mysql_info, mongo_info, *args, **kwargs)  # 使用未绑定方法,即在类的外部调用其中的实例方法,可以向调用普通函数那样,只不过需要额外备注类名
#
#     @staticmethod
#     def get_current_time_for_client(time_type="now", day_diff=0):
#         now = arrow.now().shift(days=+day_diff)               # 当日 + -
#         now_week = arrow.now().shift(weeks=+day_diff)         # 当周 + -
#         now_month = arrow.now().shift(months=+day_diff)       # 当月 + -
#         # now_year = arrow.now().shift(years=+day_diff)         # 当年 + -
#         if time_type == "now":
#             return now.strftime("%Y-%m-%dT%H:%M:%S+07:00")
#         elif time_type == "begin":
#             return now.strftime("%Y-%m-%d 04:00:00")
#         elif time_type == "end":
#             return now.strftime("%Y-%m-%d 03:59:59")
#         elif time_type == "start_time":
#             return now.strftime("%Y-%m-%d 00:00:00")
#         elif time_type == "end_time":
#             return now.strftime("%Y-%m-%d 23:59:59")
#         elif time_type == "ctime":
#             return now.strftime("%Y-%m-%d")
#         elif time_type == "etime":
#             return now.strftime("%Y-%m-%d")
#         elif time_type == "week":
#             return now_week.strftime("%Y-%m-%d")
#         elif time_type == "month":
#             return now_month.strftime("%Y-%m")
#         # elif time_type == "year":
#         #     return now_year.strftime("%Y")
#         elif time_type == "now_month_start":      # 当月第一天
#             year = now.year
#             month = now.month
#             now_month_start = datetime.date(year, month, 1).strftime("%Y-%m-%d")
#             return now_month_start
#         elif time_type == "now_month_end":        # 当月最后一天
#             year = now.year
#             month = now.month
#             last_day = calendar.monthrange(year, month)[1]
#             now_month_end = datetime.date(year, month, last_day).strftime("%Y-%m-%d")
#             return now_month_end
#         elif time_type == "now_month_day":        # 根据day_diff指定查询当月某一天
#             year = now.year
#             month = now.month
#             nnow_month_day = datetime.date(year, month, day=day_diff).strftime("%Y-%m-%d")
#             return nnow_month_day
#         else:
#             raise AssertionError("【ERR】传参错误")
#
#     def get_current_time(self, timezone="utc"):
#         """
#         根据时区返回当前时间,获取客户端当前时间
#         :param timezone: (default)shanghai|UTC
#         :return:
#         """
#         if timezone == "utc":
#             now = arrow.utcnow()
#         else:
#             now = arrow.now("Asia/Shanghai")
#         return now
#
#     def get_date_by_now(self, date_type="日", diff_day=-1, diff_unit=0, timezone="utc"):
#         """
#         获取当前日期前的时间，不包含小时分钟秒          ///    修改于2021.07.30   这个方法传参数年月日,diff_day参数传+n或-n 都可以查到对应的日期
#         :param date_type: 年|月|日，默认为日
#         :param diff_day:之后传正值，之前传负值        控制"日"的加减
#         :param diff_unit:之后传正值，之前传负值        控制"年/月"的加减
#         :param timezone: shanghai|UTC(default)
#         :return:
#         """
#         now = self.get_current_time(timezone).shift(days=int(diff_day))
#         if date_type in ("日", "今日"):
#             return now.shift(days=int(diff_unit) + 1).strftime("%Y-%m-%d")
#         elif date_type in ("月", "本月"):
#             return now.shift(months=int(diff_unit)).strftime("%Y-%m")
#         elif date_type == "年":
#             return now.shift(years=int(diff_unit)).strftime("%Y")
#         else:
#             raise AssertionError("类型只能为年月日，实际传参为： %s" % date_type)
#
#     def get_md_date_by_now(self, date_type="日", diff=0):
#         """
#         获取美东时区的当前日期前的时间，不包含小时分钟秒     ///    修改于2021.07.30
#         :param date_type: 年|月|日，默认为日
#         :param diff:之后传正值，之前传负值           控制美东时间"年月日"的加减
#         :return:
#         """
#         diff_day = self.get_md_diff_unit(-1)
#         return self.get_date_by_now(date_type, diff_day, int(diff), "shanghai")
#
#     def get_md_diff_unit(self, diff_unit=0):
#         """
#         获取美东日期偏移值
#         :return:
#         """
#         now = self.get_current_time("shanghai")
#         now_time = now.strftime("%H")
#         if int(now_time) < 12:
#             diff_unit -= 1
#         return diff_unit
#
#     def get_md_day_range(self, date_type="月", diff=-1, timezone="US/Eastern"):
#         """
#         获取美东时区的年、月的起始和结束日期，不含小时分钟秒      ///    修改于2021.07.30
#         :param date_type: 年|月|周，默认为月
#         :param diff:之后传正值，之前传负值           -1 代表以美东时间查询前一天, 0 代表以美东时间查询当天; 例：在8月1号柬时间早上9点查询当月的数据,实际美东时间是7月30号,所以查询的是7月的数据
#         :param timezone: (default)US/Eastern|UTC
#         :return: 该月起始及最后一天
#         """
#         diff = self.get_md_diff_unit(diff)
#         now = self.get_current_time(timezone)
#         new_date = now.shift(days=int(diff))
#         if date_type == "月":
#             month = new_date.month
#             year = new_date.year
#             max_day = calendar.monthlen(year, month)
#             start = new_date.replace(day=1).strftime("%Y-%m-%d")
#             end = new_date.replace(day=max_day).strftime("%Y-%m-%d")
#         elif date_type == "周":
#             start = new_date - datetime.timedelta(days=new_date.weekday())
#             start = start.strftime("%Y-%m-%d")
#             end = new_date + datetime.timedelta(days=6 - new_date.weekday())
#             end = end.strftime("%Y-%m-%d")
#         elif date_type == "年":
#             year = new_date.year
#             start = new_date.replace(year=year, month=1, day=1).strftime("%Y-%m-%d")
#             end = new_date.replace(year=year, month=12, day=31).strftime("%Y-%m-%d")
#         else:
#             raise AssertionError("类型只能为年月，实际传参为： %s" % date_type)
#
#         return start, end
#
#
#
#     def remove_special_symbols(self, data_str):
#         '''
#         将 'ci/'和 'ci/c1' 这两种字符串进行转换
#         :param data_str:
#         :return:
#         '''
#         result = data_str.split('/')
#         if result[1] == "":
#             result.remove(result[1])
#             result_str = ''.join(result)
#         else:
#             result_str = data_str
#
#         return result_str
#
#
#
# if __name__ == "__main__":
#
#
#     oracle_info = ['dataquery', 'Qy_dataq#2023', cx_Oracle.makedsn('172.31.12.211', 1521, service_name='yolink')]
#
#     oracle_sql = OracleQuery(oracle_info)
#     sql = oracle_sql.query_data(sql='SELECT * FROM YOLINK.IM_USER_INFO where USER_ID=644333')
#     print(sql)




# import arrow
import datetime
import calendar
import cx_Oracle
# from common.CommonFunc import CommonFunc

class OracleFunc(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, oracle_info, *args, **kwargs):
        '''
        使用connect创建连接对象
        connect.cursor创建游标对象，SQL语句的执行基本都在游标上进行
        cursor.executeXXX方法执行SQL语句，cursor.fetchXXX获取查询结果等
        调用close方法关闭游标cursor和数据库连接
        :param mysql_info:
        :param mongo_info:  business_order
        :param args:
        :param kwargs:
        '''
        self.connect = cx_Oracle.connect(user=oracle_info[0], password=oracle_info[1], dsn=oracle_info[2],encoding="UTF-8")
        self.cursor = self.connect.cursor()

    # 关闭数据库
    def close_db(self):
        """
        关闭数据库
        :return:
        """
        self.cursor.close()
        self.connect.close()

    def query_data(self, sql, db_name='YOLINK'):
        """
        数据查询
        :param sql:
        :param db_name:
        :return:
        """
        try:
            self.change_db(db_name)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except cx_Oracle.Error as e:
            print(e)
            print(AssertionError, "查询结果为空")
            return
        return res

    def update_data(self, sql, db_name='YOLINK'):
        """
        修改
        :param sql:
        :param db_name:
        :return:
        """
        try:
            self.change_db(db_name)
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception:
            raise(AssertionError, "修改失败！")

    def insert_data(self, sql, db_name='YOLINK'):
        """
        插入
        :param sql:
        :param db_name:
        :return:
        """
        try:
            self.change_db(db_name)
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception:
            raise (AssertionError, "插入数据失败！")

    def change_db(self, db_name):
        try:
            self.connect.select_db(db_name)
        except Exception as e:
            return e

class OracleQuery(OracleFunc):

    # 如果在子类中定义构造方法(等同于重写第一个直接父类的构造方法), 则必须在该方法中调用父类的构造方法
    def __init__(self, oracle_info, *args, **kwargs):
        super().__init__(oracle_info, *args, **kwargs)
        # self.cf = CommonFunc()

    @staticmethod
    def get_current_time_for_client(time_type="now", day_diff=0):
        now = arrow.now().shift(days=+day_diff)               # 当日 + -
        now_week = arrow.now().shift(weeks=+day_diff)         # 当周 + -
        now_month = arrow.now().shift(months=+day_diff)       # 当月 + -
        # now_year = arrow.now().shift(years=+day_diff)         # 当年 + -
        if time_type == "now":
            return now.strftime("%Y-%m-%dT%H:%M:%S+07:00")
        elif time_type == "begin":
            return now.strftime("%Y-%m-%d 04:00:00")
        elif time_type == "end":
            return now.strftime("%Y-%m-%d 03:59:59")
        elif time_type == "start_time":
            return now.strftime("%Y-%m-%d 00:00:00")
        elif time_type == "end_time":
            return now.strftime("%Y-%m-%d 23:59:59")
        elif time_type == "ctime":
            return now.strftime("%Y-%m-%d")
        elif time_type == "etime":
            return now.strftime("%Y-%m-%d")
        elif time_type == "week":
            return now_week.strftime("%Y-%m-%d")
        elif time_type == "month":
            return now_month.strftime("%Y-%m")
        # elif time_type == "year":
        #     return now_year.strftime("%Y")
        elif time_type == "now_month_start":      # 当月第一天
            year = now.year
            month = now.month
            now_month_start = datetime.date(year, month, 1).strftime("%Y-%m-%d")
            return now_month_start
        elif time_type == "now_month_end":        # 当月最后一天
            year = now.year
            month = now.month
            last_day = calendar.monthrange(year, month)[1]
            now_month_end = datetime.date(year, month, last_day).strftime("%Y-%m-%d")
            return now_month_end
        elif time_type == "now_month_day":        # 根据day_diff指定查询当月某一天
            year = now.year
            month = now.month
            nnow_month_day = datetime.date(year, month, day=day_diff).strftime("%Y-%m-%d")
            return nnow_month_day
        else:
            raise AssertionError("【ERR】传参错误")

    def get_current_time(self, timezone="utc"):
        """
        根据时区返回当前时间,获取客户端当前时间
        :param timezone: (default)shanghai|UTC
        :return:
        """
        if timezone == "utc":
            now = arrow.utcnow()
        else:
            now = arrow.now("Asia/Shanghai")
        return now

    def get_date_by_now(self, date_type="日", diff_day=-1, diff_unit=0, timezone="utc"):
        """
        获取当前日期前的时间，不包含小时分钟秒
        :param date_type: 年|月|日，默认为日
        :param diff_day:之后传正值，之前传负值        控制"日"的加减
        :param diff_unit:之后传正值，之前传负值        控制"年/月"的加减
        :param timezone: shanghai|UTC(default)
        :return:
        """
        now = self.get_current_time(timezone).shift(days=int(diff_day))
        if date_type in ("日", "今日"):
            return now.shift(days=int(diff_unit) + 1).strftime("%Y-%m-%d")
        elif date_type in ("月", "本月"):
            return now.shift(months=int(diff_unit)).strftime("%Y-%m")
        elif date_type == "年":
            return now.shift(years=int(diff_unit)).strftime("%Y")
        else:
            raise AssertionError("类型只能为年月日，实际传参为： %s" % date_type)

    def get_md_date_by_now(self, date_type="日", diff=0):
        """
        获取美东时区的当前日期前的时间，不包含小时分钟秒     ///    修改于2021.07.30
        :param date_type: 年|月|日，默认为日
        :param diff:之后传正值，之前传负值           控制美东时间"年月日"的加减
        :return:
        """
        diff_day = self.get_md_diff_unit(-1)
        return self.get_date_by_now(date_type, diff_day, int(diff), "shanghai")

    def get_md_diff_unit(self, diff_unit=0):
        """
        获取美东日期偏移值
        :return:
        """
        now = self.get_current_time("shanghai")
        now_time = now.strftime("%H")
        if int(now_time) < 12:
            diff_unit -= 1
        return diff_unit

    def get_md_day_range(self, date_type="月", diff=-1, timezone="US/Eastern"):
        """
        获取美东时区的年、月的起始和结束日期，不含小时分钟秒      ///    修改于2021.07.30
        :param date_type: 年|月|周，默认为月
        :param diff:之后传正值，之前传负值           -1 代表以美东时间查询前一天, 0 代表以美东时间查询当天; 例：在8月1号柬时间早上9点查询当月的数据,实际美东时间是7月30号,所以查询的是7月的数据
        :param timezone: (default)US/Eastern|UTC
        :return: 该月起始及最后一天
        """
        diff = self.get_md_diff_unit(diff)
        now = self.get_current_time(timezone)
        new_date = now.shift(days=int(diff))
        if date_type == "月":
            month = new_date.month
            year = new_date.year
            max_day = calendar.monthlen(year, month)
            start = new_date.replace(day=1).strftime("%Y-%m-%d")
            end = new_date.replace(day=max_day).strftime("%Y-%m-%d")
        elif date_type == "周":
            start = new_date - datetime.timedelta(days=new_date.weekday())
            start = start.strftime("%Y-%m-%d")
            end = new_date + datetime.timedelta(days=6 - new_date.weekday())
            end = end.strftime("%Y-%m-%d")
        elif date_type == "年":
            year = new_date.year
            start = new_date.replace(year=year, month=1, day=1).strftime("%Y-%m-%d")
            end = new_date.replace(year=year, month=12, day=31).strftime("%Y-%m-%d")
        else:
            raise AssertionError("类型只能为年月，实际传参为： %s" % date_type)

        return start, end



    def remove_special_symbols(self, data_str):
        '''
        将 'ci/'和 'ci/c1' 这两种字符串进行转换
        :param data_str:
        :return:
        '''
        result = data_str.split('/')
        if result[1] == "":
            result.remove(result[1])
            result_str = ''.join(result)
        else:
            result_str = data_str

        return result_str

if __name__ == "__main__":


    oracle_info = ['dataquery', 'Qy_dataq#2023', cx_Oracle.makedsn('172.31.12.211', 1521, service_name='yolink')]

    oracle_sql = OracleQuery(oracle_info)
    sql = oracle_sql.query_data(sql='SELECT * FROM YOLINK.IM_USER_INFO where USER_ID=644333')
    print(sql)
    print(sql)









# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 15:36
# @Author  : taiyang
# @FileName: YoYoManage
# @Software: PyCharm

# from __future__ import annotations
# import cx_Oracle
# import requests
# import time
# import arrow
# import os
# import sys
# sys.path.append(os.getcwd())
from config.base_dir import *
from tools.yamlControl import Yaml_data

try:
    from OracleFunc import OracleFunc
    from common.CommonFunc import CommonFunc
except ModuleNotFoundError or ImportError:
    from .OracleFunc import OracleFunc
    from .common.CommonFunc import CommonFunc


class yoyoManage(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, oracle_info):
        # self.session = requests.session()
        self.url = 'http://yolinkcs.quanyou.com.cn/'
        self.sql = OracleFunc(oracle_info)
        # self.cm = CommonFunc()
        # self.ya = Yaml_data()

    # @staticmethod              # 静态方法, 也就是加上@staticmethod装饰器
    # def get_current_time_for_client(time_type="now", day_diff=0):
    #     now = arrow.now().shift(days=+day_diff)
    #     if time_type == "now":
    #         return now.strftime("%Y-%m-%d")
    #     elif time_type == "begin":
    #         return now.strftime("%Y-%m-%d")
    #     elif time_type == "end":
    #         return now.strftime("%Y-%m-%d")
    #     elif time_type == "day":
    #         return now.strftime("%Y-%m-%d")
    #     elif time_type == "month":
    #         return now.strftime("%Y-%m")
    #     elif time_type == "year":
    #         return now.strftime("%Y")
    #     elif time_type == "time":
    #         return now.strftime("%Y-%m-%d 00:00:00")
    #     elif time_type == "etime":
    #         return now.strftime("%Y-%m-%d 23:59:59")
    #     else:
    #         raise AssertionError("【ERR】传参错误")
    #
    # # @staticmethod       # 静态方法, 也就是加上@staticmethod装饰器
    # def get_current_time(self, timezone="utc"):
    #     """
    #     根据时区返回当前时间,获取客户端当前时间
    #     :param timezone: (default)shanghai|UTC
    #     :return:
    #     """
    #     if timezone == "utc":
    #         now = arrow.utcnow()
    #     else:
    #         now = arrow.now("Asia/Shanghai")
    #     return now
    #
    # def get_date_by_now(self, date_type="日", diff_day=-1, diff_unit=0, timezone="utc"):
    #     """
    #     获取当前日期前的时间，不包含小时分钟秒          ///    修改于2021.07.30     这个方法传参数年月（不包含日）,diff_day参数传+n或-n 才可以查到对应的日期
    #     :param date_type: 年|月|日，默认为日
    #     :param diff_day:之后传正值，之前传负值        控制"日"的加减
    #     :param diff_unit:之后传正值，之前传负值        控制"年/月"的加减
    #     :param timezone: shanghai|UTC(default)
    #     :return:
    #     """
    #     now = self.get_current_time(timezone).shift(days=int(diff_day))
    #     if date_type in ("日", "今日"):
    #         return now.strftime("%Y-%m-%d")
    #     elif date_type in ("月", "本月"):
    #         return now.shift(months=int(diff_unit)).strftime("%Y-%m")
    #     elif date_type == "年":
    #         return now.shift(years=int(diff_unit)).strftime("%Y")
    #     else:
    #         raise AssertionError("类型只能为年月日，实际传参为： %s" % date_type)
    #
    # def get_md_date_by_now(self, date_type="日", diff=0):
    #     """
    #     获取美东时区的当前日期前的时间，不包含小时分钟秒     ///    修改于2021.07.30
    #     :param date_type: 年|月|日，默认为日
    #     :param diff:之后传正值，之前传负值           控制美东时间"年月日"的加减
    #     :return:
    #     """
    #     diff_day = self.get_md_diff_unit(-1)
    #     return self.get_date_by_now(date_type, diff_day, int(diff), "shanghai")
    #
    # def get_md_diff_unit(self, diff_unit=0):
    #     """
    #     获取美东日期偏移值
    #     :return:
    #     """
    #     now = self.get_current_time("shanghai")
    #     now_time = now.strftime("%H")
    #     if int(now_time) < 12:
    #         diff_unit -= 1
    #     return diff_unit

    # def rsa_encrypt(self,data):
    #     '''
    #     rsa加密（encrypt）
    #     :param data:
    #     :return:
    #     '''
    #     msg = data.encode('utf-8')
    #     self.pub_key = "-----BEGIN PUBLIC KEY-----\nMFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAL1XuLmIZttk13hmAGVuXiKSfQggfVck" \
    #               "p+iNr9jBIxkmBBfmygJ9D5A7lhUbhBEY1SqyGNIHI1DsNLfxfRvW2EcCAwEAAQ==\n-----END PUBLIC KEY-----"
    #     rsa_key = RSA.importKey(self.pub_key)
    #     cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    #     cipher_text = base64.b64encode(cipher.encrypt(msg)).decode("utf-8")
    #
    #     return cipher_text

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
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        data = {"userName": uname, "password": password, "appCode": appcode}
        print(data)
        for loop in range(1):
            try:
                rsp = self.session.post(url, headers=head, json=data)
                if rsp.json()['message'] == '用户名或密码错误!':
                    print('登录失败,用户名或密码错误,登录失败')
                elif rsp.json()['message'] != "OK":
                    raise AssertionError("登录失败,原因：" + rsp.json()["message"])
                else:
                    self.Authorization = rsp.json()['data']['token']
                    # print(self.Authorization)
                return self.Authorization

            except ConnectionError:
                time.sleep(2)
                continue






if __name__ == "__main__":



    # dataBase_configure = CommonFunc().get_dataBase_environment_config()
    # mysql_info = dataBase_configure[0]
    # mongo_info = dataBase_configure[1]
    # configure = Yaml_data().get_yaml_data(fileDir=config_url, isAll=True)
    # environment = configure[0]['environment']
    # print(f'--- 当前系统环境为：{environment} ---')

    oracle_info = ('dataquery', 'Qy_dataq#2023', '172.31.12.211/yolink', 'UTF-8')
    yoyo = yoyoManage(oracle_info)            # 创建对象

    token= yoyo.login_background(uname='uhuangchaoyang2', password='12345678', appcode='yoyo-manager')