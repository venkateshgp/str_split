from timeit import Timer

def str_split(s, sep):
    res=[]
    st, i=0, 0
    for char in s:
        if char == sep:
            res.append(s[st:i])
            st=i+1
        i=i+1
    else:
        if st != len(s):
            res.append(s[st:])
    return res
# print(Timer(str_split('12dewrd34','d')))
print(str_split('12dewrd34dq','d'))
