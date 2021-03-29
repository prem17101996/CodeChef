t=int(input())
for i in range(t):
    n=input()
    k = [int(k) for k in input().split()]
    k.sort()
    p=int(k[0])+int(k[1])
    print(p)