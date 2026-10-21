n1 = 1221
n2 = 121223

if len(str(n1)) != len(str(n2)):
    print("Not an anagram!")
    exit()

hash_arr = [0] * 10

while n1 > 10 and n2 > 10:
    hash_arr[n1 % 10] += 1
    hash_arr[n2 % 10] -= 1
    n1 //= 10
    n2 //= 10

for i in range(len(hash_arr)):
    if hash_arr[i] != 0:
        print("Not an anagram!")
        exit()

print("It is an anagram!")

