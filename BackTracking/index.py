
def sub_sets(arr):
    res = []
    curr = []
    call_count = [0]
    def rec(arr, i, curr, call_count):
        print("start of the call", i, curr, call_count[0])
        if i == len(arr):
            res.append(curr.copy())
            return
        curr.append(arr[i])
        call_count[0] += 1
        rec(arr, i + 1, curr, call_count)
        curr.pop()
        call_count[0] += 1
        rec(arr, i + 1, curr, call_count)



    rec(arr, 0, curr, call_count)
    print(res)

sub_sets([1, 2, 3])

        
