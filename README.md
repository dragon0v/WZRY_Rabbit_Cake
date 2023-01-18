
# 【王者荣耀2023新年小兔糕活动】 从公屏自动获取小兔糕信息

## 原理

安卓模拟器ADB + 本地OCR  
OCR部分来自 [DayBreak-u/chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite/tree/onnx)  

## 环境搭建

请参考 [DayBreak-u/chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite/tree/onnx)  

## 运行

打开你的模拟器，打开王者荣耀，使游戏界面停留在综合频道；  
修改main.py中的PORT，使之和你的模拟器ADB端口对应；  
\>python main.py  
获取到满足条件的小兔糕信息后便会跳出截图，可以自行登录王者荣耀输入市集代码进行售卖。

## 声明

本代码仅供学习交流，使用此代码导致的任何后果作者概不负责。  
