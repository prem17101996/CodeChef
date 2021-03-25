t = int(input())
for i in range(t):
    n = input()
    lst = []
    for o in n:
        lst.append(o)
        sum = int(lst[0]) + int(lst[-1])
    print(sum)