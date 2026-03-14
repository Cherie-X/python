#这是注释
print('Hello World!')
# ctrl加斜杠是快捷键
#注释是给程序员看的，不是给机器看的，不会被解释
# 注释不能嵌套，养成书写注释好习惯（whywhywhy）
# 三个单引号也是注释，但前面不能加东西
# 关键字 ['False', 'None', 'True', 'and', 'as'
# , 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
# 35(toooooooo much TAT)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#定义标识符，取名只有英文数字下划线能用，且数字不能开头
#python 严格区分大小写
#将Maria存储到name里，未来可在name里找到它
#变量名=变量值（有数据就有变量，变量是存储数据的）
name ='maria'
#整形数据，整数的意思int，我写的这个不是
num1 = 999
print(f'type(num1)={type(num1)}')
#bool型，只有两个结果，true or false
is_visited=True
print(f'is_visited={is_visited},type(is_visited)={type(is_visited)}')
#copy快捷键ctrl加d
#多行数据书写用三引号
