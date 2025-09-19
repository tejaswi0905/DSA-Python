def solve(n, ranges):
    answer = 0
    s = 0   # current column
    d = "r" # current direction

    i = 0
    while i < n - 1:
        l, r = ranges[i]

        # --- case 1: current row empty ---
        if l is None and r is None:
            # find the next non-empty row
            j = i + 1
            while j < n and ranges[j][0] is None:
                # just vertical moves (no horizontal here)
                answer += 1
                d = "l" if d == "r" else "r"
                j += 1

            if j == n:   # no more 1's below
                return answer

            ln, rn = ranges[j]

            # align horizontally before dropping into row j
            if d == "r":
                if s != rn:
                    answer += abs(rn - s)
                    s = rn
                answer += 1
                d = "l"
            else:
                if s != ln:
                    answer += abs(s - ln)
                    s = ln
                answer += 1
                d = "r"

            i = j
            continue

        # --- case 2: current row non-empty ---
        ln, rn = ranges[i + 1]

        # if next row empty, just finish current row before dropping
        if ln is None and rn is None:
            if d == "r":
                answer += (r - s)
                s = r
                answer += 1
                d = "l"
            else:
                answer += (s - l)
                s = l
                answer += 1
                d = "r"
            i += 1
            continue

        # normal transition (both rows have 1's)
        if d == "r":
            if r > rn:
                answer += (r - s)
                s = r
                answer += 1
                d = "l"
            else:
                answer += (rn - s)
                s = rn
                answer += 1
                d = "l"
        else: # d == "l"
            if l < ln:
                answer += (s - l)
                s = l
                answer += 1
                d = "r"
            else:
                answer += (s - ln)
                s = ln
                answer += 1
                d = "r"

        i += 1

    # --- final row cleanup ---
    l, r = ranges[-1]
    if l is not None:
        if d == "r":
            answer += abs(r - s)
        else:
            answer += abs(s - l)

    return answer


def main():
    n, m = list(map(int, input().split()))
    ranges = []
    found_w = False
    for _ in range(n):
        arr = list(input().strip())
        l, r = None, None
        for idx, val in enumerate(arr):
            if val == "W":
                found_w = True
                if l is None:
                    l = idx
                r = idx
        if l is None:  # no 1's in this row
            ranges.append([None, None])
        else:
            ranges.append([l, r])
    if not found_w:
        print(0)
        return
    print(solve(n, ranges))


if __name__ == "__main__":
    main()
