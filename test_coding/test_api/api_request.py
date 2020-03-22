import ast
import requests


def request_api_post_form(url, headers, data, cookies=None):
    data_ = ast.literal_eval(data)
    # response = requests.post(url, headers=ast.literal_eval(headers), data=data_, timeout=(3, 3)).text
    response = requests.post(url, headers=ast.literal_eval(headers), data=data_, cookies=cookies, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()  # 单位为秒
    # return response.text, response_time
    return response, response_time


def request_api_post_json(url, headers, data, cookies=None):
    data_ = ast.literal_eval(data)
    # response = requests.post(url, headers=ast.literal_eval(headers), json=data_, timeout=(3, 3)).text
    response = requests.post(url, headers=ast.literal_eval(headers), json=data_, cookies=cookies, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    # return response.text, response_time
    return response, response_time


def request_api_get_form(url, headers, payload, cookies=None):
    # response = requests.get(url, headers=ast.literal_eval(headers), params=payload, timeout=(3, 3)).text
    response = requests.get(url, headers=ast.literal_eval(headers), params=payload, cookies=cookies, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    # return response.text, response_time
    return response, response_time


def request_api_get_json(url, headers, payload, cookies=None):
    payload_ = ast.literal_eval(payload)
    # response = requests.get(url, headers=ast.literal_eval(headers), params=payload_, timeout=(3, 3)).text
    response = requests.get(url, headers=ast.literal_eval(headers), params=payload_, cookies=cookies, timeout=(5, 5))
    response_time = response.elapsed.total_seconds()
    # return response.text, response_time
    return response, response_time


def request_results(domain_name, addre, headers, data_type, data, request_type, Actual_results, cookies):
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
    if Actual_results == 200 or Actual_results == 404:
        if Actual_results_ in str(res[0].status_code):
            resul = 'SUCCESS'
        else:
            resul = 'FAIL'
    else:
        if Actual_results_ in res[0].text:
            resul = 'SUCCESS'
        else:
            resul = 'FAIL'
    return resul, res[0], res[1]
