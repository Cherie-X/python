num1=100
num2=200
 #把num1>num2的结果赋给result
result = num1>num2
print("result=", result)
#result的数据类型
print("result的类型是", type(result))
print(type(1<2))
print(1>2)
#true=1 False=0
b1=True
b2=False
print(b1+10)
#=表示赋值，==表示判断语句，例如1==0，表示判断1是否等于0
if b1==1:
    print("hello")
    #在python中，0单独出现被视为假值（无法输出），不为0的任何数被视为真值，即可以输出
if 0:
    print("hello")
if 10:
    print("woww")
#字符串也作为非0数，如if "Caleb is here":
    print("Hello Cherie.I love you")
#使用引号‘’或“”包括起来，创建字符串
str1 = 'Caleb said"Hi babe"'
str2 = "Caleb said'Hi babe'"
#python不支持单字符类型，单字在Python中作为一个字符串使用
#三引号是万能的，当长句子里有（）或其他符号时只能用三引号（三单or三双）缩进等格式也会保留
content = '''kitty is the most 
clever species in the world(not including human)'''
print(content)
#转义符也想原封不动输出？尝试加r
#转义符包括 /n换行符号，在要换行的句子前加 /r回车符号

str4 = r"hello/n world"
print(str4)






















