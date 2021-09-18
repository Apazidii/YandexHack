s1 = "1:34"
s2 = "12:453:124:2010:30"
def strf(s):
    arr = []
    while (":" in s):
        k = s.find(":")
        arr.append(s[:k+3])
        s = s[k+3:]
    return arr
print(strf(s1))
print(strf(s2))
