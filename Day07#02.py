#奇偶數分堆
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
oddnum = []
evennum = []

for num in L:
  if num % 2 == 0:
    evennum.append(num)
  else:
    oddnum.append(num)

oddnum.sort() 
evennum.sort()

L = oddnum + evennum

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
