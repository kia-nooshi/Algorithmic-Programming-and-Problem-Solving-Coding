
n, d = map(int, input().split())

people = []
for i in range(n):
    m, s = map(int, input().split())
    people.append((m, s))

people.sort()

f = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        f[i][j] = f[i-1][j]
        if i-1 >= j and people[i-1][0] - people[j][0] >= d:
            f[i][i] = max(f[i][i], f[i-1][j] + people[i-1][1])

print(max(f[n]))