a=list(map(int,input().split()))    #斷開，整數，變數
ans=a[0]    #取最前面的數字a[0]

for x in a:   #for迴圈，把a的每個數字x都巡一遍
  if x>ans:   #如果現在的x比ans還大
    ans=x   #更新答案
print("最大值是",ans)   #離開迴圈時便找到答案

for x in a:
  print(x)