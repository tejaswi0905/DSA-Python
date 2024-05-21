# smallest prime factor array
import math

def spf(n):
    spf_array = [i for i in range(n + 1)]
    root = math.sqrt(n)
    i = 2
    while i <= int(root) + 1:
        if spf_array[i] == i:
            j = i * i
            while j < n + 1:
                if spf_array[j] == j:
                    spf_array[j] = i
                j += i
        i += 1
    return spf_array

spf_array = spf(50)
for i in range(len(spf_array)):
    print(i, spf_array[i])
