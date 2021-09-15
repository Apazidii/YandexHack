s1 = "1234"
s2 = "12345678"
def strf(s):
    l = len(s)
    arr = []
    for i in range(0, l, 4):
        arr.append(s[i:i+4])
    return arr
print(strf(s1))
print(strf(s2))