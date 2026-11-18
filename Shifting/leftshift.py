arr = [5,10,15,20,25,30,35,40,45,50]

pos = 3

for i in range(len(arr)-pos):
  arr[i] = arr[i+pos]

for i in range(len(arr)-pos,len(arr)):
  arr[i] = 0

print(arr)