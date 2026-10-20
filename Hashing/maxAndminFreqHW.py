arr = [11,22,33,11,22,33,66,88,44,99,22]
freq = {}

for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1

print(f"Maximum frequency: {max(freq,key=freq.get)}")
print(f"Minimum frequency: {min(freq,key=freq.get)}")