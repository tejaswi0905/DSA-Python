'''
ngl stands for next grater left, and for each idx i, find the closest element left that is grater than arr[i]

As we move from right to left, the stack hold elements to the left of your current position.

'''

def next_grater_left(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n - 1, - 1, -1):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = i
        stack.append(i)
    return res

def next_grater_right(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = i
        stack.append(i)
    return res


def next_small_right(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = i
        stack.append(i)
    return res

def next_small_left(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = i
        stack.append(i)
    return res


arr = [3, 1, 5, 2, 6]
print(next_grater_left(arr))
print(next_grater_right(arr))
print(next_small_right(arr))
print(next_small_left(arr))