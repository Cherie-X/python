#循环从键盘输入5个数，保存到列表，并输出
# num=[0]*5
# for i in range(5):
#     num[i]=int(input("please input your score:"))
# print(num)
# books={"a","b","c"}
# books2={"c","d"}
# books_all=books.union(books2)

s_history={"ming","san","si","wu","lily","bob"}
s_politic={"ming","hua","hong","gou"}
s_english={"ming","lily","bob","davil","si"}
# stu_all1=s_history.union(s_politic)
# stu_all2=stu_all1.union(s_english)
# print(stu_all2)
# stu_only1=s_history.difference(s_politic)
# stu_only2=stu_all1.difference(s_english)
# print(stu_only2)
# stu_two=s_history.intersection(s_english)
# stu_three=stu_two.intersection(s_politic)
# print(stu_three)
print(s_history.union(s_politic,s_english))