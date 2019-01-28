# read 是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)
