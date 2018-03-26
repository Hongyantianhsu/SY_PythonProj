#coding=utf-8
# Python变量类型
a = 100
b = "hell"
c = 100.0
print a,b,c

# 多个变量赋值
a = b = c = 2;
print a,b,c
a ,b ,c = 1,2,"yanzong"
print a,b,c
a = 1,2,"yanzong"
print a
a = [1,2,"yanzong"]
print a
a = {1,2,"yanzong"}
print a

#数字数据类型：int long float complex
var1 = 1 #int
var2 = 2; #int
del var1,var2 #删除
var3 = 100l #long

#字符串
s = "read the fucking souce code";
s0 = s[0] #从左向右取值，下标从0开始
s1 = s[-1] #从右向左取值，下标从-1开始
s2 = s[0:4] #从0-3字符，跟java一样，包头不包尾
s3 = s[1:] #从第一个位置到最后一个位置
s4 = s*2 #字符串x2
s5 = s + "!!!"; #字符串拼接
print s0 #从左到右第一个字母
print s1 #从右向左第一个字母
print s2;
print s3
print s4
print s5

#列表[] 类似List
list = [1,2,3,4,5]
list1 = [1,2,3,"hello",4,5l]
print list
print list1
print list[0:]
print list[1:4]
print list*2
print list+list1
print list+[6,7,8]
list[2] = 8 #列表可以重新赋值
print list;

#元组() 类似于list
tuple = (1,2,3,4,5)
tuple1 = (1,2,3,"hello",4,5l)
print tuple
print tuple1
print tuple[0:]
print tuple[1:4]
print tuple*2
# tuple[2] = 8  错误，元组不能重新赋值


#字典dictionary 类似于Map
dict = {};
dict["name"] = "sunyan"
dict[1] = "111"
dict1 = {"name":"xuwei","1":"111"};
print dict["name"]
print dict[1]
print dict.keys();
print dict.values();
print dict1.keys();
print dict1.values();

#数据类型转换
a = 100;
b = long(a)
c = str(a)
print a
print b
print c 
