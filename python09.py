#coding=utf-8
class Student:

	name=""
	age = 0

	def __init__(self,name,age):
		self.name = name;
		self.age = age;

	def getName(self):
		print self.name;

	def getAge(self):
		print self.age;

student = Student("sunyan",26);
student.getName();
student.getAge();


print "-------------------------------------------------------------------"
#给实例绑定属性与方法

#给student绑定address属性
student.address = "深圳";

def a():
	print "方法a"
#给student绑定a()
student.a = a();

def b(self):
	print "方法b"
	pass

print "-------------------------------------------------------------------"

# 给class绑定方法，那么所有的实例都将拥有此方法
Student.b = b;

student1 = Student("dounai",26);
student1.b();

#限制实例属性
class Animal:
	__slots__ = ("name","age")

animal = Animal();
animal.name = "小黑"
animal.age = "4"
animal.color = "red"