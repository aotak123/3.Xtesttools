# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

####################——————tak制作  vol.615——————####################
import hashlib

apptypeid = input("请选择哪款app：")
# 疯狂猜成语 100012
# 看图猜成语 100018
pgtype = input("请输入广告位pgtype：")
str = apptypeid + pgtype

# 创建md5对象
md5_num = hashlib.md5()
b = str.encode(encoding='utf-8')
md5_num.update(b)
str_md5 = md5_num.hexdigest()
str_md5_16 = str_md5[:16]
# print('MD5加密前为 ：' + str)
print('云控key ：' + str_md5_16)


"""
另一种写法：b‘’前缀代表的就是bytes
str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
print('MD5加密后为 ：' + str_md5)
"""
