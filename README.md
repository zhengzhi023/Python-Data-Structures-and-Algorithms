# python 数据结构何算法入门

程序 = 数据结构+ 算法

算法有 时间复杂度  空间非咋读


###
git 提交命令
在命令行上创建新的存储库
echo "# Python-Data-Structures-and-Algorithms" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zhengzhi023/Python-Data-Structures-and-Algorithms.git
    git push -u origin main

或从命令行推送现有存储库
git remote add origin https://github.com/zhengzhi023/Python-Data-Structures-and-Algorithms.git
git branch -M main
git push -u origin main
## 时间复杂度



**时间复杂度：**用来估计算法运行时间的一个式子（单位）

一般来说，时间复杂度高的算法比复杂度低的算法慢

常见的时间复杂度（按效率排序）

 	O(1)<O(longn)<O(n)<O(nlogn)<O(n^2)<O(n^2logn)<O(n^3)

复杂问题的时间复杂度

 	O(n!) O(2n^n)O(n^n)....

print("hello world ")                 O(1)



for i in range (n):

​	print("Hello world")             O(n)



for i in range(n):                          O(n^2)

​	for j in range(n):

​		print("Hello World")





# 空间复杂度



空间复杂度：用来评估算法内存占用的大小的式子

空间复杂度的表示方式与时间复杂度完全一样

  算法使用了几个变量：O(1) 1是个单位

  算法使用了长度为n的一位连列表：O(n)

  算法使用了m行n列的二维列表：O(mn)

“ 空间换算时间”







# 列表查找

## 查找

查找：在一数据元素中，通过一定的方法找出给定的关键字相同的数据元素的过程

列表查找（线性表查找）：从列表中查找指定的元素

输入：列表、待查找元素

输出：元素下标（未找到的元素时一般返回None或-1）

内置列表查找函数：index（）

## 顺序查找

顺序查找：也叫线性查找，从列表第一个元素开始，顺序进行搜索，周到找到元素或者搜索到列表最后一个元素为止

## 二分查找

二分查找：又叫折半查找，从有序的列表的初始候选区 li[0:n] 开始，

通过对待查找的值与候选区中间的比较，可以使候选区减少一半
