import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB/'
FILE = 'README'
# 客户端链接远程主机HOST
try:
    f = ftplib.FTP()
    f.set_debuglevel(2)
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connected to host {0}".format(HOST))

# 客户端输入用户名和密码

try:
    f.login()
except Exception as e:
    print(e)
    exit()
print("*** Login")

# 客户端和服务器进行各种文件传输和信息查询操作
try:
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("*** Changed dir to {0}".format(DIR))

try:
    f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()

f.quit()
