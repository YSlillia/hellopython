a = input() #5
b = input() #10
print(a, b) 

a, b = b, a

'''
解法2
a = int(a) + int(b)
b = a - int(b)
a = a - int(b)
'''

print(a, b) #10, 5
