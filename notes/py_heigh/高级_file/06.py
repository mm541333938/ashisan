# tell 函数
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()
# 以下结果说明
# tell 返回数字的单位是byte
# read 是以字符为单位的
