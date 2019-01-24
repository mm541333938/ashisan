# 常用模块
- calendar
- time 
- datetime
- timeit
- os
- shutil
- zip
- math
- string

# calendar
import calendar
cal = calendar.calendar(2019)
print(type(cal))
print(cal)


# isleap:判断是否是闰年
# leapdays:获取指定年份之间的闰年的个数
calendar.month(2019,1)
# monthrange(年, 月) 获取一个月的周几开始和天数
# return 元组（周几开始，总天数） 0~6表示周一到周日
calendar.monthrange(2019,3)

# monthcalendar(年，月) 返回一个月每天的矩阵列表
# return 二级列表
# 注意:矩阵中没有天数用0表示
calendar.monthcalendar(2019,1)

# prcal: 直接打印日历
calendar.prcal(2019)
# prmonth(年, 月)
# weekday(年,月,日)


# time模块
### 时间戳
    - 一个时间表示，根据不同语言，可以是整数或浮点数
    - 从1970年1月1日0分0秒到现在经历的秒数
    - 如果表示时间是1970年以前或太遥远的未来，可能出现异常
    - 32位操作系统能支持到2038年
    
- UTC时间
    - 世界标准时间 中国UTC+8

- 夏令时
    就是在夏天的时候将时间调快1小时
- 时间元组
    - 一个包含时间内容的普通元组
    
    
import time
# 时间模块的属性
# 打印当前时区和UTC时间相差的秒数，没有夏令时
print(time.timezone)
# altzone 有夏令时
# daylight 测当前是否是夏令时  0表示是

# 得到时间戳
print(time.time())
# localtime 得到当前时间的时间结构
print(time.localtime())
print(time.localtime().tm_hour)
# asctime()返回元组的正常字符串化之后的时间格式
# return str   Tue Jun 6 11:11:00 2019
print(time.asctime(time.localtime()))

# ctime 获取字符串化的当前时间
print(time.ctime())

# mktime() 使用时间元组获取对应的时间戳
print(time.mktime(time.localtime()))
# clock: 获取CPU时间
# sleep使程序进入睡眠，n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)
    
# strftime: 将时间元组转化为自定义的字符串格式
t = time.localtime()
ft = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
print(ft)
ft = time.strftime("%Y{y}%m{m}%d{d} %H:%M:%S", t).format(y='年', m='月', d='日')
print(ft)


# datetime 模块
# 提供日期和时间的运算和表示
import datetime
dt = datetime.date(2019, 1, 24)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)
# datetime.time 提供一个理想和的时间，居于hour, minute,sec microsec等内
# datetime.datetime:提供日期跟时间的组合
# datetime.timedelta 提供一个时间差，时间长度

from datetime import datetime
import time
dt = datetime(2019,1,24)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

from datetime import datetime, timedelta
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


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
