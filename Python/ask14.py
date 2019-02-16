a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
d=int(input("Enter a number: "))
for i in range(a,b):
   if i>1:
     for j in range(2,i):
	   if(i%j)==0:
	     break
	   else:
	      x=i
		  y=x+d
	if y>1:
      for k in range(2,y):
        if (y%k)==0:
          break
        else:
          print x,y		