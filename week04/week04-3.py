for i in range(1,10):
  for j in range(1,10):
    if i*j<10:
      print(j,"x",i,"= ",i*j,sep="",end=" ")
    else:
      print(j,"x",i,"=",i*j,sep="",end=" ")
  print()