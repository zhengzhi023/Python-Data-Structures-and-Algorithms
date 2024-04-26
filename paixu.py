# #排序 将一组“”无序“”的的记录序列调整为“”有序“”的记录序列

# 列表排序：就是吧一组无序的列表变成有序的列表

"""
  输入:列表
  输出:有序列表
  升序:降序
  内置排序函数 sort()

排序lowB 三人组 冒泡排序 选择排序 插入排序
排序NB 三人组   快速排序  堆排序 归并排序
其他排序 希尔排序 计数排序  基数排序
"""
import random

"""
冒泡排序
列表每两个相邻的数，如果前面比后面大则交换这两个数
一趟排序完成后，则无须区减少一个数，有序区增加一个属=数
代码关键：躺、无序区范围
"""


def bubble_sort(li):
    for i in range(len(li)-1): #第i趟
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]= li[j+1],li[j]
        print(li)

li = [9,6,7,4,8,3,1,2,5]
print(li)
bubble_sort(li)
print(li)