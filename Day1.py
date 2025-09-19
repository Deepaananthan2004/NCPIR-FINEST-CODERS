n = int(input())
k = int(input("Range:"))
for i in range(k):
    rev = str(n)[::-1]
    n1 = int(rev)
    total = n + n1
    if i == k-1:
        print([-1,-1])
    if str(total) == str(total)[::-1]:
        print([i,total])
        break
    n = total