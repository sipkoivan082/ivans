def f(a, b, p):
    if (a + b) >= 65 and p%2==0:
        return 1
    if (a + b) < 65 and p == 4:
        return 0
    if (a + b) >= 65 and p %2==1:
        return 0

    else:
        if p % 2 == 0:
            return f(a + 1, b, p + 1) and f(a * 3, b, p + 1) and f(a, b + 1, p + 1) and f(a, b * 3, p + 1)
        else:
            return f(a + 1, b, p + 1) or f(a * 3, b, p + 1) or f(a, b + 1, p + 1) or f(a, b * 3, p + 1)


for s in range(1, 59):
    if f(6, s, 0) == True:
        print(s)