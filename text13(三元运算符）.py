a=10
b = 20
max = a if a>=b else b
print(max)

a = 10
b = 20
c = 30
'''1.先进行排序，最大值就是最后一个
   2.a与b先比较，b与c再比较，最后再再比较'''
max1 = a if a>=b else b
max2 = b if b>=c else c
max = max1 if max1>=max2 else max2
print(max)
'''用一条语句完成'''
max = (a if a>b else b) if (a if a>b else b)>c else c
print(max)


'''运算符优先级
高  (加了括号的）
1   普通加减，算术运算符+-=/%//@* **
1   位运算符（比较运算符）
1   逻辑运算符
1   赋值运算符
低'''
