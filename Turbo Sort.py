t=int(input())
lst=[]
for i in range(t):
    numbers=int(input())
    lst.append(numbers)

lst.sort() 
for item in lst:
    print(item)