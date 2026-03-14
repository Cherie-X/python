#for循环
'''for<变量>in<序列>'''
#输出10句hello world
nums = [1,2,3,4,5]
print(nums,type(nums))
'''每次循环时将nums中的数赋给i'''
for i in nums:
    print("hello world",i)

#一些驻留机制
nums = [1,2,3,4,5]
#相当于nums指向一个空间，空间中有五个地址，地址对应编号为01234，地址分别指向12345
print(nums,id(nums),nums[0],id(nums[0]))
print(id(1))
#num[0]和1在同一个地址，因为指向同一个数
'''range(start,stop,step)前闭后开
start是开始值，默认为0
stop是结束值
step是步长，不写默认为1'''
#生成【12345】
nums = range(1,6,1)
print(list(nums))
'''查看时记得加list'''
#生成【012345】
r2 = range(0,6)
print(list(r2))
#生成13579
r3 = range(1,11,2)
print(list(r3))
#输出十个Caleb
for i in range(10):
    print("Caleb")


'''special'''
for i in range(10):
    print("Hello")
else:
    print("end")
#正常来说，当for循环结束后，会执行else的内容
'''BUT 如果在第一个print的位置有break语句，就会提前终止for循环，也不会执行else语句'''

for i in range(50):
    print(i)
    if i ==2:
        break
else:
    print("end")

#homework
languages = ['python','java','javascript']
for x in languages:
    print(x)
    #依次取出罢了

