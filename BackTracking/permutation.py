def permutation(arr):

    def get_perm(arr):
        if len(arr) == 1:
            return [arr]
        
        res = []
        
        head = arr[0]
        tail = arr[1:]

        all_perms = get_perm(tail)

        for perm in all_perms:
            for i in range(len(perm) + 1):
                p_copy = perm.copy()
                p_copy.insert(i, head)
                res.append(p_copy)
        return res
    return get_perm(arr)

# print(permutation([1,2,3,4,5]))

def permutations_with_rep(arr):

    res = []
    def rec(cur):
        if len(cur) == len(arr):
            res.append(cur[:])
            return
        for num in arr:
            cur.append(num)
            rec(cur)
            cur.pop()
    rec([])
    return rec

print(permutations_with_rep([1,2,3]))

def other_perm(arr):
    res = []
    used = [False for _ in range(len(arr))]

    def rec(path):
        if len(path) == len(arr):
            res.append(path[:])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            path.append(arr[i])
            used[i] = True

            rec(path)

            path.pop()
            used[i] = False
    rec([])
    return res

# print(other_perm([1,2,3]))

'''
The basic code for generating combinations of size k from an array. All the elements of the array are unique and all the combinations must be unique.

The most important setp is to call the recursive call from the next index of the arr, in this case if we take a closer look into the for loop that we are using in the backtracking(i, cur_comb) function, we can see that the recursive call is (j + 1, cur_comb) so that we can avoid repetition of elements.
'''
def comb(arr, k):
    res = []

    def backtracking(i, cur_comb):
        if len(cur_comb) == k:
            res.append("".join(cur_comb))
            return
        
        for j in range(i, len(arr)):
            cur_comb.append(arr[j])
            backtracking(j + 1, cur_comb)
            cur_comb.pop()
    backtracking(0, [])
    return res


'''
Now for the question combinations with repetition allwed, that means we can select one element upto r times. Only thing that changes form the previous code is that the recursive all we start from the same index not the next one, the backtarcking(j + 1, cur_comb) will become backtracking(j, cur_comb)
'''

def comb_with_reps(arr, k):
    res = []

    def backtracking(i, cur_comb):
        if len(cur_comb) == k:
            res.append("".join(cur_comb))
            return
        
        for j in range(i, len(arr)):
            cur_comb.append(arr[j])
            backtracking(j, cur_comb)
            cur_comb.pop()
    backtracking(0, [])
    return res
print(comb('abcd', 3))


'''
For duplicates in the arr, we need to avoide them in the loop, so what we do is first sort the input array so that all the duplicates come to one place and then we can skip them in the loop, 
Like this, 
for j in range(i, len(arr)):
    if j > i and arr[j - 1] == arr[j]:
        continue
rest of the code stays same.

'''

def comb_with_duplicates(arr, k):
    res = []
    arr.sort()
    def backtracking(i, cur_comb):
        if len(cur_comb) == k:
            res.append(cur_comb[:])
            return
        
        for j in range(i, len(arr)):
            if j > i and arr[j] == arr[j - 1]:
                continue
            cur_comb.append(arr[j])
            backtracking(j + 1, cur_comb)
            cur_comb.pop()
    backtracking(0, [])
    return res

print(comb_with_duplicates([2, 1, 3, 3, 1, 4], 3))

                