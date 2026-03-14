def recursion(n):
    if n>2:
        recursion(n-1)
    else:
        print(n)

n=int(input("n="))
recursion(n)
#斐波那契数列求通项
def recursion_fei(n):
    if n==1 or n==2:
        return 1
    else:
        return recursion_fei(n-1)+recursion_fei(n-2)
print(recursion_fei(3))
#猴子吃桃子
def monkey(n):
    day1=1
    if n==1:
        return 1
    else:
        return (monkey(n-1)+1)*2

print(monkey(3))
#河内塔
#有多个盘，同意看成两个部分：最下面的一个盘和上面的所有盘
