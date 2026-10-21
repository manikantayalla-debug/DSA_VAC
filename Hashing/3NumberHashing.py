n = 121352133215

hash_arr = [0] * 4

while n % 10:
    if n%10 <= len(hash_arr):
        hash_arr[n%10]+=1
    n//=10


for i in range(1,len(hash_arr)):
    print(f"{[i]} -> {hash_arr[i]}")