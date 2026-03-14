#=最简单的
#+=复合加法运算符 c+=a     c=c+a
#-= *= /= %= **= //=同理
num1=100
num1+=100
print(num1)
i=200
i-=100
print(i)
#ab两个值进行交换
a=10
b=20
'''先定义一个中间变量
temp=a
a = b
b = temp'''
print(a)
print(b)
'''after'''
temp = a
a = b
b = temp
print(a)
print(b)
'''在python中有个更为简便的方法'''
a,b = b,a
print(a)
print(b)
