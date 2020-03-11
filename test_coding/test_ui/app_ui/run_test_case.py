# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest
from BeautifulReport import BeautifulReport
from common import send_mail
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
# print("123:", BASE_PATH)
sys.path.append(BASE_PATH)
from app_config import mysteel_app_name

# 时间戳
float_time = time.time()
local = time.localtime(float_time)
otherStyleTime = time.strftime("%Y%m%d%H%M%S", local)
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
# 用例存放位置
casepath = os.path.join(curpath, "test_mysteel_cases")
# 测试报告存放位置
log_path = os.path.join(curpath, "report\\html")
# 测试报告名称
filename = otherStyleTime
# 邮件名称
description = mysteel_app_name.get('report_name')
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "*.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(casepath, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=str(description) + str(filename), description=description, log_path=log_path)
    # 发送邮件
    send_mail.Send_Mail(description, log_path)
