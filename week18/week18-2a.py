a=int(input())
first=list(map(int,input().split()))
second=list(map(int,input().split()))

for i in range(a):
	print(first[i]+second[i],end=" ")