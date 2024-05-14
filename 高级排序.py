
'''
快速排序

'''
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp:
            right -= 1


