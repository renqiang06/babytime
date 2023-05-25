# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% 标题

import requests
import os
import time

url = "https://cn.bing.com/"
response = requests.get(url)
try:
    if response.text.find("background-image:url(")>0:
        start_index = response.text.find("background-image:url(") + len("background-image:url(")
        end_index = response.text.find(".mp4") + len(".mp4")

        video_url = response.text[start_index:end_index] + ".mp4"

        response = requests.get(video_url)
        with open(os.path.join("img", "video.mp4"), "wb") as f:
            f.write(response.content)
    else:
        with open("py.log", "a", encoding= 'utf-8') as f:
            f.write(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()) + ':' +"没有视频\n")
except Exception as e:
    with open("py.log", "a", encoding= 'utf-8') as f:
        f.write(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()) + ':' +e)