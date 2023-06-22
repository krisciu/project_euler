for c in range(1, 501):
    for b in range(1, c):
        for a in range(1, b):
            if a * a + b * b == c * c and a + b + c == 1000:
                print("a: ", a, " b: ", b, " c: ", c)
                print(a * b * c)
