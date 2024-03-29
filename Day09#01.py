n = int(input()) #20

# 是否為質數
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 小於 n 的質數
def primes(n):
    prime_list = []
    for num in range(2, n):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

f = primes(n)
print(f) # 2, 3, 5, 7, 11, 13, 17, 19
