'''
Docstring for Code_forces_sparring.Greedy.building_next_table

The way we need to build the next table is, next[pos][ch] will tell us what is the closest spot at or after pos that has the char ch. IF there no char ch at or after the pos, then we get the value of next[pos][ch] as n.

lets look at a sample table of s = '123'. The number of rows is 4, for pos 0, 1, 2, 3. Number of colums are 10, from 0 to 9

     0  1  2  3  4  5  6  7  8  9
0-> [3, 0, 1, 2, 3, 3, 3, 3, 3, 3]
1-> [3, 3, 1, 2, 3, 3, 3, 3, 3, 3]
2-> [3, 3, 3, 2, 3, 3, 3, 3, 3, 3]
3-> [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

form this table if I say next[0][2], what is the closest idx of ch = 2, at/from idx 0
'''

def next_table_right(n, s):
    nxt = [[n]*10 for _ in range(n + 1)]
    for ch in range(10):
        ptr = n
        for pos in range(n -1, -1, -1):
            if int(s[pos]) == ch:
                ptr = pos
            nxt[pos][ch] = ptr
    return nxt

def next_table_left(n, s):
    nxt = [[3]*10 for _ in range(n + 1)]
    for ch in range(10):
        ptr = 3
        for pos in range(n):
            if int(s[pos]) == ch:
                ptr = pos
            nxt[pos][ch] = ptr
    return nxt


def next_table_alf(n, s):
    ch_map = {}
    counter = 0
    for i in range(ord('a'), ord('z') + 1):
        ch_map[counter] = chr(i)
        counter += 1
    nxt = [[n] * (26) for _ in range(n + 1)]
    for i in range(26):
        ch = ch_map[i]
        ptr = n
        for pos in range(n - 1, -1, -1):
            if s[pos] == ch:
                ptr = pos
            nxt[pos][i] = ptr
    return nxt


            


ntra = next_table_alf(3, 'abc')
for row in ntra:
    print(row)

print('----------------')
ntr = next_table_right(3, '123')
for row in ntr:
    print(row)

print('------------------------')

ntl = next_table_left(3, '123')
for row in ntl:
    print(row)