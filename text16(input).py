#实例
'''要求可以从控制台接收用户信息'''
name = input("plese press your name:")
age = input("plese press your age:")
score = input("plese press your score:")
print("name:",name)
print("age:",age)
print("score:",score)
#在控制台输入的是str类型,如需进行运算，需进行类型转换
print(10 + int(score))
#也可以在接收时转成int
age2 = int(input("plese press your age:"))
print(12+age2)
print(type(age2))#int