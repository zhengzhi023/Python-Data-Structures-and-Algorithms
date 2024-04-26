# 1 顺序查找

def linear_seach(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


# 2 二分查找
# 二分查找的前提是在有序列表中执行
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区的有值
        mid = (left + right) / 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid] < val  待查找区在min右侧
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search(li, 3)
