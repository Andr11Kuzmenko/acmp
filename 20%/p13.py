a, b = input().split()
arr = []
c1 = 0
c2 = 0

for i in range(0, len(a)):
    if a[i] == b[i]:
        c1 += 1
        arr.append(i)
    elif a[i] in b:
        for j in range(0, len(a)):
            if a[i] == b[j] and j not in arr:
                c2 += 1
                arr.append(j)

print(str(c1) + ' ' + str(c2))
