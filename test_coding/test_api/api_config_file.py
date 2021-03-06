import sys
import ast
import gc
import pandas as pd
from api_request import request_results
from os.path import dirname, abspath
current_path = dirname(dirname(abspath(__file__)))
sys.path.append(current_path)
from common_file import sendDD
from common_file import my_logger
from common_file import get_time
from common_file import get_params
from common_file import read_csv


def config_program(url, file_path):

    file_name = file_path.split('/')[-1].split('.')[0]
    # 日志
    sys.stdout = my_logger.Logger(current_path + '/test_api/logs/' + file_name + '.log')
    print(file_name + "run time" + get_time.get_now_time()[1] + "==================")

    # 参数调用
    parameters_list = {}
    data = {"interface_name": [], "headers": [], "domain_name": [], "addre": [], "data_type": [], "data": [], "request_type": [], "Actual_results": [], "response": [], "response_time": [], "result": []}
    # 测试用例文件
    # file_path = './api_test_cases/mysteel_api_cases.xlsx'
    for i in read_csv.read_csv_file(file_path):
        try:
            # 引用保存的参数
            reference_name = ['reference_parameter', 'reference_header']
            for name_ in reference_name:
                if len(i[name_]) == 0:
                    pass
                else:
                    list_words = i[name_].split(',')
                    for k in list_words:
                        if len(k) == 0:
                            pass
                        else:
                            if name_ == 'reference_parameter':
                                if len(i['data']) > 2:
                                    data_ = i['data'].split(k)
                                    i['data'] = data_[0] + str(parameters_list[k]) + data_[1]
                                    # print("+++++++++:", i['data'])
                                else:
                                    addre_ = i['addre'].split(k)
                                    i['addre'] = addre_[0] + str(parameters_list[k]) + addre_[1]
                            elif name_ == 'reference_header':
                                header_ = i['headers'].split(k)
                                i['headers'] = header_[0] + str(parameters_list[k]) + header_[1]
                            # elif name_ == 'cookies':
                            #     if len(i['cookies']) > 0:
                            #         i['cookies'] = ast.literal_eval(str(parameters_list[k]))
                            #     else:
                            #         i['cookies'] = None
                            #     print("cookies==================:", i['cookies'])
            # 发送请求
            try:
                response_result = request_results(i['domain_name'], i['addre'], i['headers'], i['data_type'], i['data'], i['request_type'], i['Actual_results'])

                # 将结果写入字典
                for j in ("interface_name", "headers", "domain_name", "addre", "data_type", "data", "request_type", "Actual_results"):
                    data[j].append(i[j])
                data["result"].append(response_result[0])
                data["response_time"].append(response_result[2])
                if i["Actual_results"] == 200 or i["Actual_results"] == 404:  # 断言响应码
                    data["response"].append(str(response_result[1].status_code))
                else:
                    data["response"].append(response_result[1].text)  # 断言响应文本
            except Exception as err:
                for j in ("interface_name", "headers", "domain_name", "addre", "data_type", "data", "request_type", "Actual_results"):
                    data[j].append(i[j])
                data["result"].append("FAIL")
                data["response_time"].append("5")
                data["response"].append(str(err))
                # print(err)

            # 获取并保存要使用的参数
            if len(i['extract_word']) == 0:
                pass
            else:
                list_words_ = i['extract_word'].split(',')
                j = 0
                for kw in list_words_:
                    if len(kw) == 0:
                        pass
                    elif kw != 'cookies':
                        a = get_params.select_param(kw, response_result[1].text)
                    # elif kw == 'cookies':
                    #     a = response_result[1].cookies.get_dict()
                    parameters_list[i['interface_name'] + '_' + str(j)] = str(a)
                    j += 1

                # print("++++++++++:", parameters_list)

                # 引用当前时间的时间戳
                parameters_list["current_time"] = get_time.get_now_time()[0]

        except Exception as err:
            print("请检查 " + i['interface_name'] + "接口: " + i['addre'])
            print(err)
            sendDD.new_req(url, "### 请查看" + file_name + "接口运行日志, " + str(err), file_name + "接口日志预警")
            raise err

    # 生成Excel报告名称
    report_name_xls = file_name + '_report-' + str(get_time.get_now_time()[1]) + '.xlsx'  # 组装Execl命名
    report_path = current_path + "/test_api/report/" + report_name_xls

    # 写入Excel报告
    df = pd.DataFrame(data)
    df.to_excel(report_path, sheet_name="报告", index=False, header=True)

    # 发送钉钉提醒
    num_ = 0
    for li in data["result"]:
        if 'FAIL' == li:
            sendDD.new_req(url, "### 请查看接口测试报告,确认接口返回情况" + "\n" + file_name + ": " + data["interface_name"][num_] + "\n" + ",接口返回信息为： " + data["response"][num_], "接口响应预警")
        else:
            pass
        num_ += 1

    if 'FAIL' not in data["result"]:
        sendDD.new_req(url, "### " + file_name + "接口测试通过！！！", file_name + "接口测试全部通过！！！")

    # print("0:", data)
    # 删除内存中的变量
    del data
    gc.collect()
