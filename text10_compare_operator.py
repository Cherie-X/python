#==判断值是否相等
#！=判断是否不等于
#<>=<=
#is判断两个变量引用对象是否为同一个
#is not 判断两个引用对象是否不同
#结果为True or False

a = "cherie"
b = "cherie"
if a is b:
    print("a is b")
else:
    print("a is not b")

a = 10
b = 30
print(a is b)#这样输出的结果就是T或F
# press win +r , press cmd open the 交互模式python，输入python
#比较运算符组成的表达式，叫做比较表达式