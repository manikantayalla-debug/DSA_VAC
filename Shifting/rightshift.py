arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

pos = 3

for i in range(len(arr) - 1, pos-1, -1):
    arr[i] = arr[i - pos]

for i in range(0, pos):
    arr[i] = 0

print(arr)
