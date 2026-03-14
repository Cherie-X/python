#自定义函数
#def 函数名（变量）：
# def cal02(n):
#     count=0
#     for i in range(0,n+1,1):#range数列前闭后开
#         count+=i
#
#     print(count)
#
# n=int(input("please enter no."))
#
# cal02(n)
# def get_sum(n1,n2):
#     sum=n1+n2
#     print(sum)
#     return sum
#
# n1=int(input("please enter no."))
# n2=int(input("please enter no."))
# get_sum(n1,n2)
#函数调用机制：
#在内存中，有代码区，有栈区，栈区里有不同的栈，还有数据区
#遇到不同的函数时，会开新栈，调用函数时，也会开一个新栈

##注意事项！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
# def num_count(n1,n2):
#     return n1+n2,n1-n2
# num1=10
# num2=20
# f1,f2=num_count(n2=num1,n1=num2)
# print(f"f1={f1} and f2={f2}")

# def sum(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
#     return total
# print(sum(3,5,100))
#函数作为参数传递
#返回两个数的最大数
def max(num1,num2):
    max_num=num1 if num1>num2 else num2
    return max_num

def maxnum(max,num1,num2):
    return maxnum(num1,num2)

def count_max(max,num1,num2):
    return num1+num2,max(num1,num2)

num1=int(input("please enter no."))
num2=int(input("please enter no."))
f1,f2=count_max(max,num1,num2)
print(f1)
print(f2)