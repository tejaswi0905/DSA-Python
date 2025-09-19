def solve(r, g, b):
    if (r == 0) or (g == 0) or (b == 0):
        return (r // 3) + (g // 3) + (b // 3)
    ans = float("-inf")
    for i in range(3):
        ans = max(((r - i) // 3) + ((g - i) // 3) + ((b - i) // 3) + i, ans)
    return ans

def main():
    r, g, b = list(map(int, input().split()))
    print(solve(r, g, b))


main()
