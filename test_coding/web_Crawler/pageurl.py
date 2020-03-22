"""
需求：爬取公司某网页的所有地址、并验证这些地址是否可以被正常访问
"""

import re
import requests


def page_text(url_):
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    url = url_
    try:
        r = requests.get(url, headers=kv, timeout=2)
        if r.status_code == 200:
            pagetext = r.text
            a = 'href="' + '([^"]+)"'  # 通过截取页面标签‘href’来截取页面中的链接
            get_url = re.findall(a, pagetext)
            # print(get_url)
            return get_url
        else:
            # error_list.append(url)
            with open("err_404.txt", 'a', encoding='utf-8') as file_object:  # 状态码非200
                file_object.write(url + "\n")
    except Exception as err:
        with open("err_others.txt", 'a', encoding='utf-8') as file_object:   # 超时
            file_object.write(url + "\n")


with open('所有频道页地址.txt', encoding='utf-8') as file_object:
    for line in file_object:
        read_url = line.rstrip()
        # print("-=-=-===--======:", read_url)
        url__ = "http:/" + read_url
        res = page_text(url__)
        for i in res:
            if "http" in i:
                pass
            else:
                i = "http:" + i
            # print(i)
            res1 = page_text(i)
            for j in res1:
                if "http" in j:
                    pass
                else:
                    j = "http:" + j
                # print(i)
                page_text(j)
