# a = [2,1,5,1,3,2]
# k = 3
# def max_sum_of_array(arr,k):
#     windows_sum = 0
#     answer_array = []
#     left = 0

#     for right in range(len(a)):
#         windows_sum += arr[right]

#         if right - left >= k-1:
#             answer_array.append(windows_sum)
#             windows_sum -= arr[left]
#             left+=1
#     return max(answer_array)

# print(max_sum_of_array(a,k))


def solve(n, a, b):
    hash_a = {}
    hash_b = {}
    l = 0
    r = 1
    while r < n:
        if a[r] == a[l]:
            r += 1
            continue
        hash_a[a[l]] = max((r - 1) - l + 1, hash_a.get(a[l], 0))
        l = r
        r += 1
    hash_a[a[l]] = max((r - 1) - l + 1, hash_a.get(a[l], 0))
    
    
    l = 0
    r = 1
    while r < n:
        if b[r] == b[l]:
            r += 1
            continue
        hash_b[b[l]] = max((r - 1) - l + 1, hash_b.get(b[l], 0))
        l = r
        r += 1
    hash_b[b[l]] = max((r - 1) - l + 1, hash_b.get(b[l], 0))

    answer = 0
    all_vals = set(hash_a.keys()).union(set(hash_b.keys()))
    for val in all_vals:
        answer = max(answer, hash_a.get(val, 0) + hash_b.get(val, 0))
    return answer

    
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(solve(n, a, b))
main()
