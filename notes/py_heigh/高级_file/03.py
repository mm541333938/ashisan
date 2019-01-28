# list能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)
