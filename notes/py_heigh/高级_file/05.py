# seek 案例
# 打开文件后，从第5个字节出开始读取

with open(r'test01.txt', 'r', encoding='utf-8') as f:

    # seek移动单位是字节
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)
# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 没赌一次，休息一秒钟

# 让程序暂停， 可以使用time下的sleep函数
import time

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # read 参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read()
