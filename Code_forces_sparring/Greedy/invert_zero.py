def solve(n, arr):
    answer = []
    i = 0
    while i < n:
        j = i
        while j < n and arr[j] == 1:
            j += 1
        if j == n:
            return []
        answer.append(j - 1)
        for k in range(i, j):
            answer.append(k)
        i = j
    return answer


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("The answer is ", solve(n, a))
main()