#coding=utf-8
#for循环
for x in range(1,10):
	print x;

for x in 'python':
	print x

print "=====================================>"

#99乘法表
for i in range(1,10):   
	for j in range(1,i+1):  
		if i*j < 10: 
			print i,"*",j,"=","", #O(1)
		else :
			print i,"*",j,"=",i*j, #O(1)
	print #O(1)
#T(n) = O(f(n)) = (1+n)n/2 + 1 + 1 + 1 = O(n^2) = O(81)