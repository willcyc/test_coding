import os
current_path = os.path.split(os.path.realpath(__file__))[0]
print("current_path:",current_path)
from api_config_file import config_program

# 钉钉机器人

# 走几步看看
url = "https://oapi.dingtalk.com/robot/send?access_token=4c3fe1a2d54d0c51c8d6867c6104cc0e095113f48667e15012b8545043942b49"

# 测试部
# url = "https://oapi.dingtalk.com/robot/send?access_token=5df2b6b7a079aa76d89f303e80591b36a29160cef0f0a8c355f5c83f90c2e670"

# 测试用例
test_case_name01 = current_path + '/api_test_cases/mysteel_api_cases.xlsx'
config_program(url, test_case_name01)
