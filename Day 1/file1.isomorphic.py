def is_isomorphics(s,t):
    if len(s)!=len(t):
        return False
    char_map={}
    for i in range(len(s)):
        if s[i] in char_map:
            if char_map [s[i]]!=t[i]:
                return False
            elif t[i] in char_map.values():
                return False
            else:
                char_map[s[i]]=t[i]
    return True
s=input("Enter string s: ")
t=input("Enter string t: ")
result=is_isomorphics(s,t)
if result:
    print("The strings are isomorphic.")
else:
    print("The strings are not isomorohic.")  
