a=int(input())
hr=a//60//60
minute=a//60%60
sec=a%60
print(f"{hr:02}:{minute:02}:{sec:02}",end="")