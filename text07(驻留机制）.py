#字符串驻留机制
#python仅保留一份相同切不可变的字符串，不同的值被存放在字符串的驻留池中，
# python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同的字符串时，不会开辟新的空间
#而是将字符串的地址赋给新创建的变量
str1 = ("Hello")
str2 = ("Hello")
str3 = ("Hello")
print("str1's id is" , id(str1))
#a = 10 意味着a指向一个空间，空间里有10，如何区分不同的空间，就用地址区分
print("str2's id is" , id(str2))
#how to know that str1 lead to 10？ str1被翻译后会变成一个地址，根据这个地址找到10
print("str3's id is" , id(str3))
#驻留机制的出现情况
#1.字符串由26字母或数字，下划线组成
#2.字符串长度为0or1(长度0就是空格，长度1就是任意一个字符，字母符号数字都OK）
#3.字符串在编译时进行驻留，而非运行时
#以下是对3的举例
a = "abc"
b = "".join(["a","bc"])
print(a)
print(b)
#可以看见ab输出内容都一样，但是b在运行前只是空的，要运行后才知道是abc，就不一样，运行前已知
print(id(a))
print(id(b))
#4.[-5,256]的整数数字(number must be same pls)
#pycharm对1，4进行了优化，有其他字符地址也一样
num1 = -5
num2 = 5
print(id(num1))
print(id(num2))
#驻留机制节约空间，提高了效率

