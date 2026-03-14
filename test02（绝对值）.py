#求绝对值abs
from collections.abc import async_generator
from operator import truediv

print("-100的绝对值is",abs(-100))
#变量三要素：变量的名称，变量的值，变量的值的类型
a = 1
b = False
print("b is" , b , "type b is" , type(b))
#内存=memory
print(a,b)
name = "Cherie"
age = 18
print("personal information:%s %s" %(name,age))
# %的应用 %.2f意思是保留两位小数，2换成1就是保留一位
#format函数
print("personal information:{} {}".format(name,age))
#f-strings
print(f"personal information:{name} {age}")
