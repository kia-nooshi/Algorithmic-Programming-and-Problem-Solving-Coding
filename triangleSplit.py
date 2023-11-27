from math import isclose

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

def find_horizontal_line(x1, y1, x2, y2, x3, y3):
    a = min(y1, y2, y3) + 0.0001
    b = max(y1, y2, y3) - 0.0001
    while not isclose(a, b, rel_tol=1e-5, abs_tol=1e-5):
        c = (a + b) / 2
        a1, a2, a3 = area(x1, y1, x2, y2, x3, y3), 0, 0
        if y1 > c and y2 > c or y1 < c and y2 < c:
            a2 = area(x1, y1, x2, y2, (y2 - c) * (x1 - x2) / (y1 - y2) + x2, c)
            a3 = area(x3, y3, x2, y2, (y2 - c) * (x3 - x2) / (y3 - y2) + x2, c)
        elif y1 > c and y3 > c or y1 < c and y3 < c:
            a2 = area(x1, y1, x3, y3, (y3 - c) * (x1 - x3) / (y1 - y3) + x3, c)
            a3 = area(x2, y2, x3, y3, (y3 - c) * (x2 - x3) / (y2 - y3) + x3, c)
        else:
            a2 = area(x2, y2, x1, y1, (y1 - c) * (x2 - x1) / (y2 - y1) + x1, c)
            a3 = area(x3, y3, x1, y1, (y1 - c) * (x3 - x1) / (y3 - y1) + x1, c)
        if isclose(a1, a2 + a3, rel_tol=1e-5, abs_tol=1e-5):
            return c
        elif a1 > a2 + a3:
            b = c
        else:
            a = c
    return a

n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    print('{:.4f}'.format(find_horizontal_line(x1, y1, x2, y2, x3, y3)))

