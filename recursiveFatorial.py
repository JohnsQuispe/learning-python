def fat(n):
    if n == 0:
        return 1
    else:
        return n * (fat(n - 1))

f  = int (input())

print(fat(f))