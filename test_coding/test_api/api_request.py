import ast
import requests


def request_api_post_form(url, headers, data):
    data_ = ast.literal_eval(data)
    # response = requests.post(url, headers=ast.literal_eval(headers), data=data_, timeout=(3, 3)).text
    response = requests.post(url, headers=ast.literal_eval(headers), data=data_, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    return response.text, response_time


def request_api_post_json(url, headers, data):
    data_ = ast.literal_eval(data)
    # response = requests.post(url, headers=ast.literal_eval(headers), json=data_, timeout=(3, 3)).text
    response = requests.post(url, headers=ast.literal_eval(headers), json=data_, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    return response.text, response_time


def request_api_get_form(url, headers, payload):
    # response = requests.get(url, headers=ast.literal_eval(headers), params=payload, timeout=(3, 3)).text
    response = requests.get(url, headers=ast.literal_eval(headers), params=payload, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    return response.text, response_time


def request_api_get_json(url, headers, payload):
    payload_ = ast.literal_eval(payload)
    # response = requests.get(url, headers=ast.literal_eval(headers), params=payload_, timeout=(3, 3)).text
    response = requests.get(url, headers=ast.literal_eval(headers), params=payload_, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    return response.text, response_time


def request_results(domain_name, addre, headers, data_type, data, request_type, Actual_results):
    steelphone_domain_name = str(domain_name)
    url = steelphone_domain_name + addre
    # print("url:", url)
    if data_type == "form" and request_type == "post":
        res = request_api_post_form(url, headers, data)
    elif data_type == "json" and request_type == "post":
        res = request_api_post_json(url, headers, data)
    elif data_type == "form" and request_type == "get":
        res = request_api_get_form(url, headers, data)
    elif data_type == "json" and request_type == "get":
        res = request_api_get_json(url, headers, data)
    else:
        print("请检查接口请求方式！！！")
    # print(res)
    # print("++++++:", res[0])
    Actual_results_ = str(Actual_results)
    if Actual_results_ in res[0]:
        resul = 'SUCCESS'
    else:
        resul = 'FAIL'
    return resul, res[0], res[1]
