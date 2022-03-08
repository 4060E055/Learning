def Func(n):
    return 1 if n < 3 else Func(n - 1) + Func(n - 3)


# 通常工具包下面會寫一個show這個工具包大概長什麼樣子的程式
if __name__ == '__main__':
    print("輸出費式數列:")
    for i in range(0, 16):
        print(Func(i))
