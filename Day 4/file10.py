def isScramble(s1,s2):
    if len(s1)!=len(s2):
        return False
    if sorted(s1)!=sorted(s2):
        return False
    if s1==s2:
        return True
    for i in range(1,len(s1)):
        s1_left = s1[:i]
        s1_right = s1[i:]
        s2_left = s2[:i]
        s2_right = s2[i:]
        if isScramble(s1_left,s2_left) and isScramble(s1_right,s2_right):
            return True
        s2_left = s2[len(s2) - i:]
        s2_right = s2[len(s2) - i]
        if isScramble(s1_left,s2_left) and isScramble(s1_right,s2_right):
            return True
        return False
s1=input("enter the string")
s2=input("enter the string")
print(isScramble(s1,s2))

 

