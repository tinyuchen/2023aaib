#分式化簡 瘋狂程設裡
a=51
b=68
#a,b=map(int,input().split( ))

def gcd(a,b):
  if a==0:
    return b
  elif b==0:
    return a
  return gcd(b,a%b)
ans=gcd(a,b)
print(a//ans,b//ans)