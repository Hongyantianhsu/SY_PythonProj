#coding=utf-8
class Person:
	Id = 0;

	def __init__(self,name,age,address): #类似java构造函数
		self.name = name;
		self.age = age;
		self.__address = address

	def setAddress(self,address):
		self.__address = address;
		pass

	def getAddress(self):
		return self.__address;
		pass

	def a(self):
		if self.age <18:
			print "未成年"
			pass
		else:
			print "已成年"
			pass
	def __b__(self):
		print "Person-->私有方法b()"
		pass
	

p = Person("sunyan",18,"shenzhen");
print p.name;
print p.age;
print p.Id,Person.Id
#p.address; address被申明为了私有属性，外部无法访问
print p.getAddress();
p.setAddress("湖北")
#print p._Person__address 这样虽然可以，但是不同Python解释器把————name改成不同的变量名

p.__address = "厦门" #这里的__address并不是Person的内部address
print p.getAddress();
p.a();


print "==================================================="


#继承

class Man:
	pass;
	def a(self):
		print "Man-->a()"
		pass
class Student(Man):
	pass;
class Teacher(Person):
		pass

student = Student();
student.a();

teacher = Teacher("万老师",27,"长沙");
print teacher.getAddress();

#多态
class Animal:
	def show(slef):
		print "Animal-->show()"
	def a(self):
		self.show();

class Cat(Animal):
	pass;

class Dog(Animal):
	def show(self):
		print "Dog-->show()"

def test(animal):
	animal.show();
	pass

animal = Animal();
dog = Dog();
cat = Cat();

test(animal); #Animal-->show()
test(Dog()) #Dog-->show()
test(Cat()) #Animal-->show()

dog.a(); #Dog-->show()

print "----======================================"

#获取对象类型type()
print type(1) #int
print type(test) #function 方法类型
print type(dog) #instance 实例类型

#比较是否为某种类型
print type(111) == int
print isinstance(dog,Animal)

#获取对象所有属性和方法dir()
print dir(111)
print dir(dog)

#设置对象所有属性setattr()
setattr(dog,"name","小黄");
#获取对象某个属性getattr()
print getattr(dog,"name")
#print getattr(dog,"age") 获取不存在的属性会报错
print getattr(dog,"age",5)
#判断对象是否有某个属性
print hasattr(dog,"name")
print hasattr(dog,"age")
