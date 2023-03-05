import cv2
import numpy as np


# 展示结果
def show(name):
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 计算两个图片距离
def main():
    otemp = 'qq_block.jpg'
    oblk = 'qq_bg.jpg'
    # Image_PreProcessing(otemp, 278, 108.11)
    # Image_PreProcessing(oblk, 38.61, 38.61)
    target = cv2.imread(otemp, 0)
    # 这里需要进行重新设置图片的大小，可以通过浏览器捕获到大小
    target = cv2.resize(target, (56, 56))
    template = cv2.imread(oblk, 0)
    # 这里也进行了设置
    template = cv2.resize(template, (280, 163))
    w, h = target.shape[::-1]
    temp = 'temp.jpg'
    targ = 'targ.jpg'
    cv2.imwrite(temp, template)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    template = cv2.imread(temp)
    # 这里进行主要的计算
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    # 展示圈出来的区域
    cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
    show(template)

    return y