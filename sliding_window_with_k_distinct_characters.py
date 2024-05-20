

# def longest_subarray_with_distinct_chars(str,k):
#     left = 0
#     right = 1
#     length = 0
#     arr = []
#     count = 0

#     for left in range(len(str)):
#         arr.append(str[left])
#         count += 1
        
#         while(right<len(str)):
#             if str[right] in arr and count<=3:
#                 arr.append(str[right])
#                 right+=1
#             elif str[right] not in arr and count<=3:
#                 arr.append(str[right])
#                 right+=1
#                 count+=1
#             else:
#                 break
#         count = 0
        
#         if len(arr) > length:
#             length = len(arr)
#         arr = []
#     return length

string = "cbbebi"
k = 3

'''
{
  "b" : 3
  "e" : 1
  "i" : 1
}

'''
def longest_string(str, k):
    chars_freq = {}
    l = 0
    answer = float("-inf")

    for r in range(len(str)):
        cur_char = str[r]
        if cur_char not in chars_freq:
            chars_freq[cur_char] = 0
        chars_freq[cur_char] += 1

        while len(chars_freq) > k:
            left_char = str[l]
            chars_freq[left_char] -= 1
            if chars_freq[left_char] == 0:
                del chars_freq[left_char]
            l += 1
        answer = max(answer, r - l + 1)
    return answer
print(longest_string(string, k))

# if we are calculating min, we need to update the answer whenever we move the left side of the window
# if we are calculating the max, we need to update the answer whenever we move the right side of the window.

