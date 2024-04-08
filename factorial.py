def fact(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * fact(n-1)
    return result