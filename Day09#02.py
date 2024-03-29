#定義一個可以計算總和的 sum function，其中參數的數量可以是動態不固定的

def f(*args):
    return sum(args)
    # 使用內建的 sum 函數計算 args 元組中所有元素的總和

print(f(1, 2, 3))  # 6
print(f(1, 2, 3, 4, 5))  # 15
