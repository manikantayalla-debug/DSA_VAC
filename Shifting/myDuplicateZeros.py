arr =[1, 2, 0, 3, 4, 0, 5, 0, 9]
n = len(arr)
skip = False
for i in range(n):
  if skip:
    skip = False
    continue
  if arr[i] == 0:
    for j in range(n-1,i,-1):
      arr[j] = arr[j-1]
    skip = True

print(arr)