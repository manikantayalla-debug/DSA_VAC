
s = "abcdabehfaa"

hash_arr = [0] * 26

for i in range(len(s)):
    hash_arr[ord(s[i]) - 97]+=1

target = 'z'

print(f"Frequency of {target} = {hash_arr[ord(target) - 97]}")
