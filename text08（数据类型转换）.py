#应用：需要字符串与数据相加
#n1 = 100
#result = "n1 = " + n1
#print(result)

#隐式类型转换，在运算时，数据类型会自动向高精度转换，即
num1 = 1.1
num2 = 20
num4 = num1 + num2
print(num4,type(num4))
#float精度高于int
num2 = num2 + 0.1
print(num2,type(num2))
#成功将num2从int转为float

#显示类
# 型转换（强制转换）
#int(x.[,base])将x转换为整数
#str（x）将x转换为字符串
#float（x）
i = 100
j = float(i)
print(i,type(i))
print(j,type(j))
k = str(i)
print(k,type(k))
print("100 is" + k)
#soooooo coooooool
#python中一切皆为对象,any float int can all be str by using str()
n1 = 200.456
print(str(n1))
print(type(n1))
#这样会报错！可以把整数的str如“100”转成int类型，小数都不行，一定要整数
#100.0str类型用int转换都会报错
#n3 = "Hello"
#print(float(n3))
#强制转换后会返回一个数据/值，强制转换后，并不会影响原变量的数据类型， eg.
i = 10
j = float(i)
print(j,type(j))
print(i,type(i))



