# -*- coding: utf-8 -*-这个可以支持中文注释
"""
Created on Wed Jan  3 15:58:01 2018

@author: douyh
"""

'''*************************chapter 4: dictionary***************************'''
print('---------------This is for chapter 4 dictionary----------------------')
###How to create a dict###
a={'A':'a','B':'b',1:1}
b=dict(A='a',B=2,C=1)#等号前面不能用数字。虽然等号之前没有用引号，但是也是字符串
print(a,'\n',b)
#no.1
'''
方法：clear
对象：字典
作用：清除字典中的所有项，与{}不同的是{}是直接改变绑定关系，对关联的字典不会有影响
原地操作：是
'''
print('1.clear')
a={'A':'a','B':'b'}
b=a
a.clear()#会修改b
#a={}#不会修改b
print(a)
print(b)
#no.2
'''
方法：copy
对象：字典
作用：浅复制
原地操作：替换不是，增删是
'''
print('2.copy')
from copy import deepcopy
a={}
a={'A':['a','A'],'B':'b','C':'c'}
b=a.copy()
c=deepcopy(a)#deepcopy
b['A'].remove('a')
print(a,'\n',b,'\n',c)
#no.3
'''
方法：fromkeys
对象：字典
作用：fromkeys方法是使用给定的键创建新的字典，每个键都对应了默认的值None
原地操作：有返回值
'''
print('3.fromkeys')
print(dict.fromkeys(['name','age']))
print(dict.fromkeys(['name','age'],'uknown'))#可以修改默认值
#no.4
'''
方法：get
对象：字典
作用：get方法是一个更宽松的访问字典的方法，如果试图访问字典中不存在的项时，没有任何
    异常，而得到了None值，还可以定义自定义的值替换None
原地操作：
'''
print('4.get')
d={}
print(d.get('A'),d.get('a','no'))
#no.5
'''
方法：has_key,在Py3.0中已经没有了
对象：字典
作用：
原地操作：
'''
print('5.has_key')
#no.6
'''
方法：items和iteritems
对象：字典
作用：items方法将字典所有的项以列表的形式返回，列表中每一个项都表示为‘对’的形式，但
    并没有特定的次序；而iteritems作用相同，只是返回迭代器而非列表,并更高效
原地操作：否
'''
print('6.items and iteritems')
a={'A':'a','B':'b'}
print(a.items())
#print(list(a.iteritems()))#py3中iteritems报错
#no.7
'''
方法：keys 和 iterkeys
对象：字典
作用：keys方法将字典中的键以列表形式返回，而后者则返回针对键的迭代器
原地操作：
'''
print('7.key')
a={'A':'a','B':'b'}
print(a.keys())#没有iterkeys in py3
#no.8
'''
方法：pop
对象：字典
作用：pop方法用来获取给定键的值，然后将这个键-值对从字典中移除，注意一定要有输入。
    一次只能取出一个来
原地操作：是，且有返回。
'''
print('8.pop')
a={'A':'a','B':'b','C':'c'}
a.pop('A','B')#只能取出'a'
print(a)
#no.9
'''
方法：popitem
对象：字典
作用：随机弹出一个项，相对pop更高效，因为不用首先获取键的列表，字典中是没有顺序的
原地操作：
'''
print('9.popitem')
a={'A':'a','B':'b','C':'c'}
a.popitem()#随机弹出，但好像每次都是弹出了'c'，但是字典中是没有顺序的。
print(a)
#no.10
'''
方法：setdefault
对象：字典
作用：一部分类似于get，能够获得与给定键相关联的值；而如果没有给定的键，则设定相应的值
原地操作：是
'''
print('10.setdefault')
a.clear()
a={'A':'a','B':'b'}
print(a.setdefault('A','c'))
print(a.setdefault('C','c'))
#no.11
'''
方法：update
对象：字典
作用：利用一个字典项更新另外一个字典，提供的字典项会被添加到旧的字典中，如果有相同的
    则进行覆盖。
原地操作：是
'''
print('11.update')
a.clear()
a={'A':'a','B':'b'}
b={'A':'aa','C':'c'}
a.update(b)
print(a)
#no.12
'''
方法：values和itervalues
对象：字典
作用：以列表的形式返回字典中的值，后者返回迭代器####结果与书上好像不太一样
原地操作：否
'''
print('12.values')
a.clear()
a={'A':'a','B':'b'}
print(a.values())
print(list(a.values()))#没有itervalues，而这里需要list，注意与key的区别。
#要加list应该是返回的迭代器？




