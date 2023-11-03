a=[9,8,7,6,5,4,3,2,1,0]
N=len(a)
print(a)    #排之前印一下
for k in range(N):
  for i in range(1,N):
    if a[i]<a[i-1]:   #比大小，不對的話就交換
      a[i],a[i-1]=a[i-1],a[i] #就左右交換
  print(a)    #排完一輪，在印出來