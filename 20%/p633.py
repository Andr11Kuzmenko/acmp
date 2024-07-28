t_n = input()
sn = []

for i in range(3):
    sn.append(input())

sn.sort()

print(t_n + ': ' + ', '.join(sn))
