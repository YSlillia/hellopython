#實作題 n! 階乘計算
x = input() # 4

if x.isdigit():
  x = int(x)
  result = 1
  for i in range(1, x+1):
    result *=i
  print(result)
else:
  print(f'{x} 是一個不合法的輸入，無法運算')
