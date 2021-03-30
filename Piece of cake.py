t=int(input())
for i in range(t):
    s=str(input())
    lst = []
    for i in range(len(s)):
        n = s.count(s[i])
        lst.append(n)
    lst.sort()
    k = lst[-1]


    if ((len(lst))/2 == k):
        print("YES")

    else:
        print("NO")