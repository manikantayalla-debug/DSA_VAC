arr = [1,2,3,1,3,2,12]
freq = {}

for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1

target = 1

print(f"{target} : {freq.get(target)}")