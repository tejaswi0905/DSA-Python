"""
rec(i, j) I have the len of the lcs from [0...., i - 1] and [0......, j - 1] from the arrays of A and B.
if A[i] == B[j] then we need to add 1 to the current lcs and move both i and j and call the rec(i + 1, j + 1)
if not, then either A[i] can match with [j + 1...... m-1] or B[j] can match with [i + 1, ....... n -1 ]
so we need another two more calls, rec(i + 1, j) and rec(i, j + 1).

Base case: if either i or j reach the end, then there is no chars left to compare so lcs at that state will be 0
Initil call: rec(0, 0)

"""

