fileName = input("Enter the file name: ")

if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandle = open(fileName)

counters = dict()

for line in fileHandle:
    if line.startswith("From:"):
        words = line.split()
        counters[words[1]] = counters.get(words[1], 0) + 1

maxValue = None
maxKey = None

for key, value in counters.items():
    if maxValue == None or maxValue < value:
        maxValue = value
        maxKey = key
print(maxKey, maxValue)
