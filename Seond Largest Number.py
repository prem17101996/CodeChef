t=int(input())
for i in range(t):
    (a,b,c)=map(int,input().split(' '))
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    print(lst[1])