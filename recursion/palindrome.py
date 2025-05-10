def palin(n,s,e):
    if s == e:
        return True
    if e - s == 1:
        return n[s] == n[e]
    return n[s] == n[e] and palin(n,s+1,e-1)

print(palin('13231',0,4))