
s1 = "michael"
s2 = "bradshaw"


def string_merge(s1 , s2):
    i = 0
    ans = ''
    while i < len(s1) or i < len(s2):
        if i < len(s1):
            print(s1[i])
            ans += s1[i]
    
        if i < len(s2):
            print(s2[i])
            ans += s2[i]
        i += 1
    return ans



print(string_merge(s1, s2))