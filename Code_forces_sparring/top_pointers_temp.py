def int_part(string):
    ans = []
    for ch in string:
        if ch == ".":
            break
        ans.append(ch)
    return ans
    

def deci_part(string):
    ans = []
    found_dot = False
    for ch in string:
        if ch == ".":
            found_dot = True
            continue
        if found_dot:
            ans.append(ch)
    return ans
def add(num1, num2):
    val = int(num1) + int(num2)
    return str(val)

def fill_zeros(count, s, is_before):
    if is_before:
        ans = ["0"] * count
        for ch in s:
            ans.append(ch)
        return ans
    else:
        ans = []
        for ch in s:
            ans.append(ch)
        for i in range(count):
            ans.append("0")
        return ans


def solve(s1,s2):
    # Filling with zeros
    #int part
    ns1 = int_part(s1)
    ns2 = int_part(s2)
    n, m = len(ns1), len(ns2)
    if n > m:
        ns2 = fill_zeros(n - m, ns2, True)
    elif m > n:
        ns1 = fill_zeros(m - n, ns1, True)

    #deci part
    ds1 = deci_part(s1)
    ds2 = deci_part(s2)
    p, q = len(ds1), len(ds2)
    if p > q:
        ds2 = fill_zeros(p - q, ds2, False)
    elif q > p:
        ds1 = fill_zeros(q - p, ds1, False)



    #add_decimal_part
    d_carray = ""
    deci_sum = []
    for i in range(len(ds1) - 1, -1, -1):
        n1 = ds1[i]
        if d_carray:
            n1 = add(n1, d_carray)
        n2 = ds2[i]
        val = add(n1, n2)
        if len(val) > 1:
            deci_sum.append(val[1])
            d_carray = val[0]
        else:
            deci_sum.append(val)
            d_carray = ""
    
    #add_int_part
    i_carry = ""
    i_sum = []
    for i in range(len(ns1) - 1, -1, -1):
        v1 = ns1[i]
        if i == len(ns1) - 1 and d_carray:
            v1 = add(v1, d_carray)
        if i_carry:
            v1 = add(v1, i_carry)
        v2 = ns2[i]
        ival = add(v1, v2)
        if len(ival) > 1:
            i_sum.append(ival[1])
            i_carry = ival[0]
        else:
            i_sum.append(ival)
            i_carry = ""
    i_sum.reverse()
    deci_sum.reverse()
    ans = "".join(i_sum) + "." + "".join(deci_sum)
    return ans
        


n1 = "969.8979"
n2 = "98769.7978"



print(solve(n1, n2))


