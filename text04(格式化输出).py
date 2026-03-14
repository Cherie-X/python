#格式化输出
#1.%的方式，好处是可以保留自定义位小数.nf就是保留n位小数
n1 = 100.000000002
n2 = 520.1314
print("%.2f"%(n1/n2))
#format函数
var1 = 200
var2 = 300
var3 = 400
print("分别为{}  {}  {}".format(var1,var2,var3))
#f-string
num1 = 100
num2 = 520.13
print(f"num1 is {num1},num2 is {num2}")

#比较运算符
#结果为True或False
