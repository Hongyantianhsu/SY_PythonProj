#coding=utf-8

#算数运算符
a = 10
b = 20
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** 2 #a的2次幂
i = a // b #取整除整数部分
print c
print d
print e
print f
print g
print h
print i

#比较运算符
print (a == b);
print (a != b)
print a <> b
print a > b
print a < b
print a >= b
print a <= b

#赋值运算符 + - * / % // **
a += b
print a
a -= b
print a
a *= b
print a
a /= b
print a 
a %= b
print a 
a **= 2
print a
a //= b
print a

#位运算符 &(与运算)、|(或运算)、^(异或运算)、~(取反运算)、>>(右移动运算)、<<(左移动运算)
m = 2 #0010 
n = 4 #0100
print m & n #0000
print m | n #0110
print m ^ n #0110
print ~m    #1101
print m >> 2 #0000
print m << 2 #1000

#逻辑运算符
print m and n #4
print m or n  #2
print not m  #false

#成员运算符 in、not in  针对 列表[]和元组()
a = 10
list = [1,2,3,10]
tuple = (11,20,30)
print a in list    # true 
print a in tuple   # false

print "=======>身份运算符"
#身份运算符 is 、is not
str0 = "abcd"
str1 = "abcd"
print str0 is str1
arr0 = [1,2,3,4]
arr1 = arr0
arr2 = arr0[:]
print arr0 is arr1 # 引用对象同一个 true
print arr0 == arr1 # 值相同 true
print arr0 is arr2 # 引用对象不是同一个 false
print arr0 == arr2 # 值相同 true

	