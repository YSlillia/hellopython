#利用程式取出網址當中的 domain 後輸出
s = input() # https://www.facebook.com/dscareer

s = s.split('/')
s = s[2]

print(s) #www.facebook.com
