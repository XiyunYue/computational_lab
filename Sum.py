def sumOdd(n):
    sum = 0
    for i in range(n+1):
        if i%2 == 1:
            sum = sum + i
    return sum

