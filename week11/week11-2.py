a,b=map(int,input().split( ))
ans=0

if a<0:
	a=-a
elif b<0:
	b=-b

for i in range(1,a+1):
	if a%i==0 and b%i==0:
		ans=i
print(ans,end="")