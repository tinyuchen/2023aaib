a,c,b=input().split()
if c=="+":
	ans=int(a)+int(b)
elif c=="-":
	ans=int(a)-int(b)
elif c=="*":
	ans=int(a)*int(b)
elif c=="/":
	ans=int(a)//int(b)
print(ans,end="")