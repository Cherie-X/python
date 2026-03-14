#字典dict_a={key:value,key:value...}
#根据key取出value的方法：dict_a[key]
from multiprocessing.spawn import set_executable

# fam_member={"mom":{"sex":"female","name":"dorothy","tel":"13632330332"},"me":{"sex":"female","name":"cherie","tel":"13042093161"}}
# print(fam_member)
# print(fam_member["mom"]["name"])
def search(my_list,find_value):

    for item in my_list:
        if item == find_value:
            print("congratulations!")
            break
            return item

item=str(input("enter item:"))
my_list=["1","2","3","4","5","6","7","8","9"]
search(my_list,item)
