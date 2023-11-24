#輾轉相除法(減法;用除法取餘數的原理)
a=12345678912
b=98765432102

def gcd(a,b):
  print(a,b)
  if a==0:
    return b
  elif b==0:
    return a
  return gcd(b,a%b)
ans=gcd(a,b)
print(ans)