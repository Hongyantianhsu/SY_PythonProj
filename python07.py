#coding=utf-8

# python函数
def showStr(str):
	"打印传入的字符串"
	print str
	return 
showStr("hello world!!!")

#可更改、不可更改对象
def show(a):
	a = 10
	print '函数内a=',a #10
a = 5
show(a)  #5 
print '函数外a=',a

def show1(list1):
	list1[0] = 8
	print '函数内:',list #8,2,3,4
list = [1,2,3,4]
show1(list)
print list #8,2,3,4

print '----------------------->'

#必备参数
def show(name):
	print 'name:',name
show('sunyan') #必须传入参数

#关键字参数
def show1(name,age):
	print 'name:',name,"age:",age
show1(age=20,name="xiaohua") #启用关键字传参顺序可变

#缺省参数
def show2(name,age=23): #当没传age时，会启用默认值23
	print 'name:',name,"age:",age
show2("xiaohei")

#不定长参数 类似java可变参数
def show3(name,*age):
	print 'name:',name,"age:",age
show3("sunyan",10,20)

#lambda匿名函数
sum = lambda a1,a2:a1+a2
print sum(10,23) #33