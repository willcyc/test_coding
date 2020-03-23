"""
待完善：
1、获取、引用cookies，项目：钢联数据
2、获取、引用session，。。。
"""
import threading
from api_config_file import config_program
import os
current_path = os.path.split(os.path.realpath(__file__))[0]
# print("current_path:", current_path)

path_ = current_path + '/api_test_cases/'
file_names = os.listdir(path_)
# del file_names[0]
for i in file_names:
    if 'txt' in i:
        file_names.remove(i)
# print("file_names:", file_names)

# 钉钉机器人

# 走几步看看
url = "https://oapi.dingtalk.com/robot/send?access_token=4c3fe1a2d54d0c51c8d6867c6104cc0e095113f48667e15012b8545043942b49"

# 测试部
# url = "https://oapi.dingtalk.com/robot/send?access_token=5df2b6b7a079aa76d89f303e80591b36a29160cef0f0a8c355f5c83f90c2e670"

# for i in file_names:
#     # 测试用例地址
#     test_case_name01 = path_ + str(i)
#     config_program(url, test_case_name01)


def many_thread():
    threads = []
    for i in file_names:
        test_case_name01 = path_ + str(i)
        t = threading.Thread(target=config_program(url, test_case_name01), args=(10,))
        threads.append(t)
    for t in threads:
        t.start()


if __name__ == '__main__':
    many_thread()
