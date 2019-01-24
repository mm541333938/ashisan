# datetime 模块
# 提供日期和时间的运算和表示
# import datetime
# dt = datetime.date(2019, 1, 24)
# print(dt)
# print(dt.day)
# print(dt.year)
# print(dt.month)
# # datetime.time 提供一个理想和的时间，居于hour, minute,sec microsec等内
# # datetime.datetime:提供日期跟时间的组合
# # datetime.timedelta 提供一个时间差，时间长度
#
# from datetime import datetime
# import time
# dt = datetime(2019,1,24)
# print(dt.today())
# print(dt.now())
# print(dt.fromtimestamp(time.time()))
#
# from datetime import datetime, timedelta
# t1 = datetime.now()
# print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td = timedelta(hours=1)
# # 当前时间加上时间间隔后，把得到的时间格式化输出
# print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit - 时间测量工具
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)
