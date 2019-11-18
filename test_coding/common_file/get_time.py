import time


# 获取当前时间
def get_now_time():
    now_time_ = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    t = int(round(time.time()*1000))
    t_ = str(t)
    # print('当前时间戳： ', t)
    # print(now_time_)
    return t_, now_time_
