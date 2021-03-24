t=int(input(" "))
ans=1
for i in range(t):
    n=int(input(' '))
    for j in range(1,n+1):
        ans=ans*j
    print(ans)
    ans = 1