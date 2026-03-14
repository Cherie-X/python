#+ application
name = "Cherie"
score = 145
print(score + 90)
print("100" + "93")
print(f"score的类型是{type("太厉害了")}")
print(f"my name is {name}")
print(f"my score is {score}")
#次方的表达 2**3 代表2的三次方
m3 = 2**5
print(m3)
#进制 十进制，十六进制加前缀0x，八进制前缀0o,二进制0b
#1byte字节=8bit位 字节数随数字增大而增大，以4为倍数增加
#科学计数法形式。eg 5.12e+2 5.12乘十的二次方 5.12E-2表示5.12除以10的二次方
#只对浮点数有效，整形术加0也可以变成浮点数
n3 = 3.0e2
print(f"three {n3}")
#对于浮点数的计算，会出现精度缺失的情况，这时候需要导入decimal类
from decimal import Decimal
print(Decimal("8.1")/Decimal("3"))
#太牛啦老师