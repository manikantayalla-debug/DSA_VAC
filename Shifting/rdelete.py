arr = [5,10,15,20,25,30]
pos = 2

print("Original array:",arr)
for i in range(pos,len(arr)-1):
    arr[i] = arr[i+1]

arr[-1]=0

print("Array after deletion:",arr)