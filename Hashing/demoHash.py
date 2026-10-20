arr = [1,3,2,1,3]

hash_arr =  [0]*len(arr)

for i in range(len(arr)):
    hash_arr[arr[i]]+=1

print(arr)
target = int(input("Enter a number: "))
print(f"{target} has freqency of : {hash_arr[target]}")
