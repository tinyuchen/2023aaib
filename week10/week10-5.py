a=int(input("輸入1個整數"))
ans=0

for i in range(1,a+1):
  print("現在測試",a,i,"相除的結果",a%i)
  if a%i==0:
    ans+=1

print(ans)