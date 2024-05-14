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
        #添加一个标记，如果一趟没有交换，则有序
        exchang = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]= li[j+1],li[j]
                exchang=True
        print(li)
        if not exchang:
            return

li = [9,6,7,4,8,3,1,2,5]
# print(li)
# bubble_sort(li)
# print(li)
#




'''
选择排序
缺点：

'''
def select_sort_simple(lis):
    li_new = []
    for i in range(len(li)):
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)

    return li_new
print(select_sort_simple(li) )
'''
该函数是一个选择排序算法的实现。它通过遍历列表，
每次找到剩余部分中的最小值，并与当前位置的元素交换位置
。通过多次遍历和交换，将列表按照从小到大的顺序排序。在每次交换位置后，
函数会打印当前排序完成的部分列表。'''

def select_sort(li):
    for i in range(len(li)-1):
        min_index = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_index]:
                min_index = j


def insert_sort(li):
    """
    使用插入排序算法对列表进行升序排序。

    参数:
    li -- 待排序的列表，包含任意可比较类型的元素。

    返回值:
    无返回值，原列表将就地排序。
    """
    # 遍历列表中的每个元素，从第二个元素开始
    for i in range(1, len(li)):
        # 将当前元素暂存，以便比较和插入
        tmp = li[i]
        # 找到插入位置，从当前元素的前一个元素开始向前比较
        j = i - 1
        # 当前元素相对于已排序部分的位置未确定，持续向前移动直到找到正确位置
        while j >= 0 and li[j] < tmp:
            li[j + 1] = li[j]
            j -= 1
        # 插入元素到正确位置
        li[j + 1] = tmp

insert_sort(li)
print(li)



