arr = [10,20,30,40,50,60]
P = 1


for i in range(P,len(arr)-1):
    arr[i]= arr[i+1]

arr[-1] = 0

print(arr)