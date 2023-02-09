def countvowelstrings(n):
    return sum(range(1,n+1))

n=int(input("Enter the length of the strings:"))
result=countvowelstrings(n)
print("The number of lexicographically sorted strings of length",n,"consisting only of vowels is :",result)
