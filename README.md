
# 【王者荣耀2023新年小兔糕活动】 从公屏自动获取小兔糕信息

## 原理

安卓模拟器ADB + 本地OCR  
在模拟器里运行王者荣耀，每隔一定周期对游戏画面截图，通过OCR识别其中的文字来判断是否有达到一定数量的小兔糕代码  
> OCR部分来自 [DayBreak-u/chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite/tree/onnx)  

## 环境搭建

请参考 [DayBreak-u/chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite/tree/onnx)  

## 运行

打开安卓模拟器，打开王者荣耀，使游戏界面停留在综合频道；  
查看你的模拟器ADB端口，模拟器的ADB端口通常可以在高级设置里找到；  
\>python main.py  [-h] [-p PORT] [-s SLEEP] [-t TARGET]
默认条件下会找模拟器的5555端口，每5秒找一次当前公屏里900及以上的小兔糕
获取到满足条件的小兔糕信息后便会跳出截图，可以自行登录王者荣耀输入市集代码进行售卖。

## 声明

本代码仅供学习交流，使用此代码导致的任何后果作者概不负责。  
