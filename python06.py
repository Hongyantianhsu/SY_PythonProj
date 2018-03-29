#coding=utf-8
import time;
import calendar;

#时间类time
t = time.time(); #获取时间戳
print '当前时间:',t #1522304797.02

t1 = time.localtime(); #获取时间元组
print t1          #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=29, tm_hour=14, tm_min=26, tm_sec=37, tm_wday=3, tm_yday=88, tm_isdst=0)

t2 = time.asctime(t1);#格式化时间
print t2          #Thu Mar 29 14:26:37 2018

t3 = time.strftime("%Y-%m-%d %H-%M-%S",t1);#格式化日期 年-月-日 时-分-秒
print t3          #2018-03-29 14-26-37

time.sleep(2)   #休眠了2s
print '休眠了2s---'

print '--------------------------------------------------------'


#时间日历 Calendar
cal = calendar.month(2018,3); #2018年3月份日历
print '2018年3月份日历：'
print cal
#           March 2018
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

cal1 = calendar.calendar(2016,w=2,l=1,c=6) #2016年全年日历
print cal1

print calendar.firstweekday() #每周起始日期 0

print calendar.isleap(2018) #是否是闰年

print calendar.leapdays(2000,2018); #2000 ~ 2018年之间闰年数量

print calendar.monthcalendar(2018,3) #以列表形式返回3分月的日历

