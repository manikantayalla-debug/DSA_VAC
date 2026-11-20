arr = [5,10,15,20,25,30]
pos = 2
print("Original array: ")
for i in range(pos,0,-1):
    arr[i] = arr[i-1]

arr[0] = 0

print(arr)