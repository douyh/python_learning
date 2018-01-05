# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:12:27 2018

@author: douyh
"""

'''*****************************chapter 3: string***************************'''
print('--------------------This is for chapter 3 string----------------------')
#no.1
'''
方法：find
对象：字符串
作用：find方法可以再一个较长的字符串中查找子串，它返回子串所在位置的最左端索引。
    如果没有找到则返回-1
原地操作：
'''
print('1.find')
a = 'python'
print(a.find('py'),a.find('s'))
#也可以用in来检查成员资格，但是返回是True or False
print('py' in a)
#还可以设定查找的范围
print(a.find('p', 1, 5))#可以只指定开始的地方
#no.2
'''
方法：join
对象：字符串
作用：join方法是split方法的逆方法，用来连接序列中的字符串元素
原地操作：否
'''
print('2.join')
a = [1, 2]
b = ['1', '2']
c = '&'
try:
    print('This is a:' + c.join(a))#这里会引起TypeError
except TypeError:
    print('This is b:' + c.join(b))
else:
    pass
#no.3
'''
方法：lower
对象：字符串
作用：返回字符串的小写字母版
原地操作:是
'''
print('3.lower')
print('HellO'.lower())
#no.4
'''
方法：replace
对象：字符串
作用：replace方法产生将某字符串中所有匹配项均被替换之后得到的字符串
原地操作：是
'''
print('4.replace')
print('HellOO'.replace('O','o'))
#no.5
'''
方法：split
对象：字符串
作用：是join方法的逆方法，用来将字符串分割成序列，如果不提供任何分隔符，程序会把所有
    空格作为分隔符（空格，制表符，换行等）
原地操作:是
'''
print('5.split')
a = '1~2~3~~~4~~5'
print(a.split('~'))
#no.6
'''
方法：strip
对象：字符串
作用：strip方法返回去除两侧（不包括内部）的空格的字符串。去除的字符可以指定。
原地操作：是
'''
print('6.strip')
a = ('~~~!!!~~hello;;;~~!!')
print(a.strip('~;!'))
