#coding=utf-8
#for循环
for x in range(1,10):
	print x;

for x in 'python':
	print x

#=====================================>
#99乘法表
for i in range(1,10):
	for j in range(1,i+1):
		if i*j < 10:
			print i,"*",j,"=","",i*j,
		else :
			print i,"*",j,"=",i*j,
	print