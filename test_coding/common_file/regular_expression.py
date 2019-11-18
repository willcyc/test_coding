# -*- coding:utf-8 -*-
import re


# 正则表达式提取器
def select_param(left_, b):
    e = str(left_) + '([^"]+)"'
    n = re.findall(e, b)
    return n[0]
