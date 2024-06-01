#leetcode 680 twopointers
def validPalindrome(self, s: str) -> bool:
    i,j = 0,len(s)-1
    def check(s,i,j):
        while(i<=j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True


    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return check(s,i+1,j) or check(s,i,j-1)
    return True




        

                
            