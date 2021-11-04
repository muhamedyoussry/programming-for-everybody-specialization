fname = input("Enter file name: ")
fh = open(fname)

words = fh.read()

wordsString = words.split()

result = []
for word in wordsString:
    if word in result:
        continue
    else:
        result.append(word)

result.sort()

print(result)
