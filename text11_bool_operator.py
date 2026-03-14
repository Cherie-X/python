#and是布尔“与”
#x and y 如果x为False则返回x的值，否则返回y的值
#if x and y is 数字，则0为False，非零为True
a = 50<30
b = 30>20
print(a and b)
#or,是布尔或，如果x是TRue（非零值），则返回x的值，否则返回y的值
#not 布尔“非”，如果x为True 则返回False，否则返回“True”
print(a or b)
print(not a)
print(not(a or b))
score = 70
if (score>=60 and score<80):#我的脑子转不过来了
    print("score is greater than 60")
#——————————————————————————————————————————————————————————
a = 1
b = 99
print(a and b)#输出99
print((a > b)and b)#输出False
print((a < b)and b)#输出99
