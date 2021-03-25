t=int(input())
for i in range (t):
    lst=[]
    n=int(input())
    n=str(n)
    for i in range(len(n)):
        lst.append(n[i])

    def fun(lst):
        for i in range(len(lst)):
            if lst[-1] == "0":
                lst.pop()
                return(fun(lst))
            else:
                return(lst)

    p=fun(lst)
    a=p[::-1]
    print("".join(a))