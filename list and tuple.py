# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:37:57 2018

@author: douyh
"""

'''*************************chapter 2: list and tuple***********************'''
print('---------------This is for chapter 2 list and tuple-------------------')
'''
python中内建6种序列，列表和元祖是最常用的两种
python中的容器又包括了序列，映射，集合等
'''
###How to create a list###
print('How to create a list?')
a = [1, 2, 3]
b = list('hello')#list参数为迭代器，如dict.value的返回值
print(a,b)
'''
比较简单的通用序列操作
索引、分片、相加、乘法
成员资格使用in进行检查
长度(len),最小值(min),最大值(max)
'''
#no.1
'''
方法：append
对象：列表
作用：在列表末尾追加新的1个对象
原地操作：是
'''
print('1.append')
a = [1, 2, 3]
a.append([4, 5, 6])
print(a)#print[1, 2, 3, [4, 5, 6]]
#no.2
'''
方法：count
对象：列表
作用：统计某个元素在列表中出现的次数
原地操作：否
'''
print('2.count')
a = [1, 1, 1, 2, 3]
print(a.count(1))#3
#no.3
'''
方法：extend
对象：列表
作用：extend方法可以在列表的末尾一次性追加另一个序列中的多个值，可以用新的列表扩展原
    有的列表
原地操作：是
'''
print('3.extend')
a = [1, 2, 3]
print(a.extend([4, 5, 6]))#None
print(a)
#+操作会返回一个全新的列表而不是原地操作
print(a + [7, 8, 9])
print(a)
#使用分片操作可以达到同样的效果
a[len(a):] = [0]
print(a)
#no.4
'''
方法：index
对象：列表
作用：index方法从列表中找出某个值第一个匹配项的索引位置，如果没有找到会产生异常
原地操作：否
'''
print('4.index')
a = [1, 2, 3]
print(a[a.index(2)])
#no.5
'''
方法：insert
对象：列表
作用：insert方法用于将对象插入到列表中
原地操作：是
'''
print('5.insert')
a = [1, 2, 3]
a.insert(2, 'hello')#在a[2]之前插入
print(a)
#这里同样可以用分片赋值
a[3:3] = ['world']#如果不加方括号，会把world分开成多个字母
print(a)
#no.6
'''
方法：pop
对象：列表
作用：pop方法会移除列表中的一个元素，默认是最后一个，并且返回该元素的值
    可以使用pop和append两个方法来实现FIFO和Stack
原地操作：是，这是唯一一个有返回值的原地操作，除非被移除的项是None.其他原地操作
        返回都是None
'''
print('6.pop')
a = [1, 2, 3]
print(a.pop())
print(a)
print(a.pop(0))#这里可以指定移除的索引。
print(a)
#no.7
'''
方法：remove
对象：列表
作用：remove方法用于移除列表中某个值的第一个匹配项
原地操作：是
'''
print('7.remove')
a = [1, 2, 3]
a.remove(2)
print(a)
#no.8
'''
方法：reverse
对象：列表
作用：reverse方法将列表中的元素反向存放
原地操作：是
'''
print('8.reverse')
a = [1, 2, 3]
a.reverse()
print(a)
#可以使用一个函数reversed来操作，但是reversed返回一个迭代器
print(list(reversed(a)))
#no.9
'''
方法：sort
对象：列表
作用：sort方法用于在原位置对列表进行排序。默认是升序排列。
原地操作：是
'''
a = [2, 4, 1, 3]
a.sort()
print(a)
a.sort(reverse = True)#升序排列
print(a)
b = a[:]#注意这里不是直接绑定而是复制，因此对b进行修改不会影响a
b.sort()
print(a,b)
#此外还可以用另外一个函数sorted来实现，而该函数可以应用于任何序列，但是却总是返回
#一个列表
c = 'python'
print(sorted(c))
#sort方法中key参数提供了一个在排序过程中使用的函数
#如果要根据元素的长度进行排序，那么可以用len作为键函数
d = ['12', '123', '1234']
d.sort(key = len, reverse = True)
print(d)

'''
元组也是一种序列，但是元组不能修改。
'''
###How to create a tuple###
print('How to create a tuple?')
a = (1,2,3)#括号不是必须的
b = 'a',#只有一个元素必须要加逗号
c = 3 * b
print(a,b,c)
'''
tuple函数
作用：以一个序列作为输入，返回一个元组
'''
print('The fuction: tuple')
a = [1, 2, 3]
b = list('hello')
print(tuple(a))
print(tuple(b))














