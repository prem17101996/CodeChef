# cook your dish here
t=int(input())
lst=[]
for i in range(t):

    numbers=input()
    for j in range(len(numbers)):
        lst.append(numbers[j])
    count=0
    for i in range(len(lst)):
        if int(int(lst[0]))==4:
            count+=1
            lst.pop(0)
        else:
            lst.pop(0)
    print(count)
