s={1,2,3,4}   #第1種：使用大括號
print(s)

s=set((1,3,5,7))    #第2種：使用set()，裡面放入「圓括號(一開始要加入的東西)」。
print(s)

s=set([1,2,4,3])    #第2種：使用set()，裡面放入「方括號[list陣列的東西]」。
print(s)

s=set("Hello")    #第2種：使用set()，裡面放入「字串""」，python會把它一個個拆分開來。
print(s)

#.add()和.remove()
s.add(100)
print(s)
s.remove("H")
print(s)