# write 案例
# a代表追加方式打开
with open(r'test01.txt', 'a', encoding='utf-8') as f:
    # 注意字符串内含有换行符
    f.write("\n 生活不仅有眼前的苟且, \n 还有远方的苟且")
    f.writelines("我是writeline")

# 可以直接写入行， 用writeline