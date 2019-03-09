t1,t2,term=1,1,0
n=int(input("enter the number"))
for i in range(0,n):
	if i==0:
		print(t1)
	elif i==1:
		print(t2)
	else:
		term=t1+t2
		print(term)
		t1=t2
		t2=term