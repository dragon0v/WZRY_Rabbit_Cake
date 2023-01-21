# -*- coding: utf-8 -*-
# @Time    : 2023/1/18
# @Author  : github.com/dragon0v

# ADB 参考
# https://blog.csdn.net/u011254376/article/details/123155244
# https://blog.csdn.net/qq_39189509/article/details/89321052


import  os
import subprocess
import time
import argparse

from model import OcrHandle
from wzrytest import detect

def ADB_connect(port):
    if str(ADB("devices")).count('device')!=2:
        # 避免重复连接
        ADB("connect 127.0.0.1:%d"%port)
        print("连接成功")
    print("已连接设备")
    
def ADB(cmd):
    result = subprocess.Popen('adb\\adb.exe '+cmd,shell=True,stdout=subprocess.PIPE)
    out, err = result.communicate()
    # return out.replace(b'\r\r\n', b'\n') #Android6及以下
    return out.replace(b'\r\n', b'\n') #Android7及以上

def main(sleep=5, target=900):
    while 1:
        # ctrl-c 结束程序
        ADB("shell /system/bin/screencap -p /sdcard/wzrytemp.png")  #截取屏幕
        ADB("pull /sdcard/wzrytemp.png wzry_img/wzrytemp.png")  # 将截图保存到电脑

        wzry_img = r"wzry_img\wzrytemp.png"
        res = detect(wzry_img)
        if res and max(res) >= target:
            os.startfile(wzry_img)
        
        time.sleep(sleep)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.description='port:模拟器的ADB调试端口, sleep:获取周期, target:目标小兔糕最低数量'
    parser.add_argument("-p", "--port", help="模拟器的ADB调试端口，默认5555", dest="PORT", type=int, default="5555")
    parser.add_argument("-s", "--sleep", help="获取周期，默认5秒", dest="SLEEP", type=int, default="5")
    parser.add_argument("-t", "--target", help="目标小兔糕最低数量，默认900", dest="TARGET", type=int, default="900")
    args = parser.parse_args()
    
    PORT = args.PORT  # 模拟器的ADB调试端口
    SLEEP = args.SLEEP  # 获取周期
    TARGET = args.TARGET  # 目标小兔糕最低数量

    ADB_connect(PORT)

    main(SLEEP, TARGET)