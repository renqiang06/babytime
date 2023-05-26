# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% 标题

import requests
import os
import time

url = "https://cn.bing.com/"
# url ="https://ntp.msn.cn/edge/ntp?locale=zh-cn&dsp=0&sp=Google"
# url = "https://ntp.msn.cn/edge/ntp?locale=zh-CN&title=新建标签页&dsp=1&sp=必应&prerender=1"
response = requests.get(url)
try:
    if response.text.find("background-image:url(")>0:
        # //*[@id="backgroundImage"]/video
        start_index = response.text.find("https://prod-streaming-video-msn-com") + len("https://prod-streaming-video-msn-com")
        end_index = response.text.find(".mp4") + len(".mp4")

        video_url = response.text[start_index:end_index] + ".mp4"

        response = requests.get(video_url)
        with open(os.path.join(os.getcwd(),"img\\video.mp4"), "wb") as f:
            f.write(response.content)
    else:
        with open(os.path.join(os.getcwd(),"py.log"), "a", encoding= 'utf-8') as f:
            f.write(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()) + ':' +"没有视频\n")
except Exception as e:
    with open(os.path.join(os.getcwd(),"py.log"), "a", encoding= 'utf-8') as f:
        f.write(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()) + ':' +e)