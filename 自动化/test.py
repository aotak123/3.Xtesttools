# # coding=utf-8
import requests
import json
import time
import response

# for i in range(5):
#     print(i)
# else:
#     print("第", i, "次")
#######################################################################################

#Python 函数允许同时全部或部分使用固定参数、默认参数、单值（一颗星）可变参数、键值对（两颗星）可变参数，使用时必须按照前述顺序书写
# def do_something(name, age, gender='男', *args, **kwds):
#     print('姓名：%s，年龄：%d，性别：%s'%(name, age, gender))
#     print(args)
#     print(kwds)
#
# do_something('xufive', 50, '男', 175, 75, math=99, english=90)
#######################################################################################

#求列表各元素的平方
# a = [1, 2, 3, 4, 5]
# result = [i*i for i in a]
# print(result)

###########
# a = [1,2,3]
# for item in map(lambda x:x*x, a):
#     print(item, end=' ') # 间隔符号更改为空格

#######################################################################################

#索引
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = ['a', 'b']
# a[1:9] = b    # 索引从0计算   索引4到索引8（不包括8）
# print(a)
#######################################################################################

#断言
# def i_want_to_sleep(delay):
#     assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
#     print('开始睡觉')
#     time.sleep(delay)
#     print('睡醒了')
# i_want_to_sleep(2)