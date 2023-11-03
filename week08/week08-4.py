a=[3,0,1,8,7,2,5,4,6,9]
N=len(a)
print(a)    #排之前印一下
for i in range(1,N):
  if a[i]<a[i-1]:   #比大小，不對的話就交換
    a[i],a[i-1]=a[i-1],a[i] #就左右交換
print(a)    #排完一輪，在印出來