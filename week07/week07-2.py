a=12345
ans=0 #用來組合答案
while a>0:
  ans=ans*10+a%10 #ans先抬升10倍，再加個位數的a%10
  print("現在a:",a,"現在a%10",a%10,"現在的ans:",ans)
  a=a//10 #最後面才能撥掉皮(削皮)
print("ans:",ans)