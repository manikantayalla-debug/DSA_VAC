arr = [10,20,30,40,50,60]
r = 2
# print(arr)

# for _ in range(r):
#     first = arr[0]
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#     arr[-1] = first
# print(arr)

# Method 2
tempArr = []
for i in range(r):
    tempArr.append(arr[i])

for i in range(len(arr)-r):
    arr[i] = arr[i+r]
j=0
for i in range(len(arr)-r,len(arr)):
    arr[i] = tempArr[j]
    j+=1
print(arr)