arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

number_of_zero = 3

for i in range(len(arr)-number_of_zero,len(arr)):
    arr[i] = 0

print(arr)