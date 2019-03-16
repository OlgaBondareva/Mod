def lehmer(n):
    a = 1567
    m = 68030
    r = 2797
    x = []

    i = 0
    while i < n:
        r = (a * r) % m
        x.insert(i, round(r / m, 4))
        i += 1

    return x
