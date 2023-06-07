import math

n, s = map(int, input().split())

patches = []
for i in range(n):
    x, y, k = map(int, input().split())
    patches.append((x, y, k))

total_crop = sum(p[2] for p in patches)
if total_crop + s < 1000000:
    print("-1")
else:
    left, right = 0, 1e9
    while right - left > 1e-6:
        mid = (left + right) / 2
        covered_crop = sum(p[2] for p in patches if math.hypot(p[0], p[1]) <= mid)
        if covered_crop >= 1000000 - s:
            right = mid
        else:
            left = mid
    print("{:.7f}".format(left))


