t= int(input())
for i in range(t):
    lst=[100,50,10,5,2,1]
    res=0
    n=int(input(''))
    for j in range(6):
        res+=int(n/lst[j])
        n=int(n%lst[j])
    print(res)