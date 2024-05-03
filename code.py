def squaresum(n):
    if n == 0:
        return 0
    else:
        return 2 * n + squaresum(n - 1) - 1

result = squaresum(100)
print(result)