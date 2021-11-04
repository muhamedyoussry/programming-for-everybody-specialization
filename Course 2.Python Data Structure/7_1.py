# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

words = fh.read()
print(words.upper().rstrip())
