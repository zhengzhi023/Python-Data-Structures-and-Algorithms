
'''
快速排序

'''
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left <right and li[right] >= tmp:    #从右边找比tmp小的数
            right -= 1          #往左走一步
        li[left] = li[right]   #把右边的值移到左边空位上
        while left < right and li[left] <= tmp:    #从左边找比tmp大的数
            left += 1
        li[right] = li[left]    #把左边的值移到右边空位上
    li[left] = tmp
    return left

def quick_sort(li, left, right):    #快速排序
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)
#
# li = [3, 4, 5, 1, 2, 6, 7, 8, 9]
# quick_sort(li, 0, len(li)-1)
# print(li)

'''
堆排序前传-二叉树
树是一种数据结构，它通过连接节点创建的。
树是一种可以递归定义的数据结构。
树是由n个节点组成的结构。
如果n=0,那这是一颗空树
如果n>0，那存在1个节点这个节点成为树的根节点，他节点可以分为m个集合，每个集合都是一颗子树。

什么是堆

堆是一种特殊构造的完全二叉树，常用于实现优先队列。它分为大顶堆和小顶堆两种：
大顶堆：每个父节点的值大于等于其子节点的值。
小顶堆：每个父节点的值小于等于其子节点的值。
堆以数组形式存储，便于快速访问和调整以维持堆序。主要操作包括插入元素、删除元素（通常是最值）和调整堆结构，
支持高效的数据管理和排序算法，如堆排序和优先级调度。
'''
'''
堆排序过程
建立一个堆
1.将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
2.交换堆顶和末尾元素，此时末尾元素就是最大值。
3.重新调整结构，使其满足堆定义，然后继续交换堆顶和当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。

'''

def sift(li ,low,high):
    '''
    :param li: 列表
    :param low: 堆的对顶位置
    :param high:  堆得最后一个元素的位置
    :return:
    '''
    i = low #最开始指向根节点
    j = 2*i+1 #j开始是左孩子
    tmp = li[low] #把堆顶存起来 



