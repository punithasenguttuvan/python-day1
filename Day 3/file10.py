def editdistancehelper(i,j,str1,str2):
    if i == 0:
        return j
    if j == 0:
        return i
    ans = 1 + min(
        {
            editdistancehelper(i,j - 1,str1,str2), 
            editdistancehelper(i - 1,j,str1,str2), 
            editdistancehelper(i - 1,j - 1,str1,str2), 
        }
    )
    if str1[i - 1] == str2[j- 1]:
        ans = min(ans,editdistancehelper(i - 1,j - 1,str1,str2))


    return ans


def editdistance(str1,str2):
    n = len(str1)
    m = len(str2)
    ans = editdistancehelper(n,m,str1,str2)
    return ans
print(editdistance("cat","cut"))
