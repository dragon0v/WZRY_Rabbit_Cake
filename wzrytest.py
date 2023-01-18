from model import OcrHandle
import cv2
import numpy as np
import re
from time import time

# 装opencv的时候总是失败，后来通过安装旧版本成功不报错

def detect(input_img='test2.jpg'):
    # 返回获取到的小兔糕数量列表
    handler = OcrHandle()
    img = cv2.imread(input_img, cv2.IMREAD_COLOR)
    print(img)
    t1 = time()
    result = handler.text_predict(img, 480)
    print('spend time %.3f'%(time() - t1))
    # print(result)
    text = ""
    for r in result:
        text += r[1][4:]
    print(text)
    
    pattern = re.compile("今天(\d+)块")
    res = re.findall(pattern, text)
    res = list(map(int,res))
    print(res)
    return res


if __name__ == '__main__':
    detect()