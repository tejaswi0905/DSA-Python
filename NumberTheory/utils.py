def eea(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [g, x, y]

