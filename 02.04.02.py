a = []
n = int(input())
if n < 100000:
    for i in range(n):
        x = int(input())
        a.append(x)
        
b = []
N = int(input())
if n < 100000:
    for i in range(N):
        x = int(input())
        b.append(x)

a = set(a)
b = set(b)
c = a.intersection(b)
print(len(c))
        