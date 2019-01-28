# with 语句案例

with open(r"test01.txt", 'r', encoding='utf-8') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
    # 下边语句块开始对文件f进行操作
    # 在本模块中不需要在使用close关闭文件f
