s = "the sky is blue"
words = s.split(' ')
string = []
for word in words:
	string.insert(0, word)

print(" ".join(string))
