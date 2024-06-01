def isValidPalindrome(s):
    count_for_left = [0]
    count_for_right = [0]
    def skipping_left(s,count_for_left):
        l = 0
        r = len(s) - 1
        while l < r:
            if (l + 1) == r and s[l] != s[r]:
                if count_for_left[0] > 0:
                    return False
                return True
                
            if count_for_left[0] > 1:
                return False
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            left_next_char = s[l + 1]
            if left_next_char == s[r]:
                l += 1
                count_for_left[0] += 1
                continue
            return False
        return True
        
    def skipping_right(s,count_for_right):
        l = 0
        r = len(s) - 1
        while l < r:
            if (l + 1) == r and s[l] != s[r]:
                if count_for_right[0] > 0:
                    return False
                return True
                
            if count_for_right[0] > 1:
                return False
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            right_next_char = s[r - 1]
            if right_next_char == s[l]:
                r -= 1
                count_for_right[0] += 1
                continue
            return False
        return True
    answer = skipping_left(s, count_for_left) or skipping_right(s, count_for_right)
    return answer
    
    

print(isValidPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))