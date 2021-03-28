t=int(input(''))
for i in range(t):
    (d,n)=map(int,(input().split(' ')))
    for j in range(d):
        n=int((n*(n+1))/2)
    print(n)