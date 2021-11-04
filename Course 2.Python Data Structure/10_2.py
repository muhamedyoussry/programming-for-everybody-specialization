fileName = input("Enter the file name : ")

if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandle = open(fileName)

counters = dict()

for line in fileHandle:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            words = line.split()
            clock = words[5]
            hour = clock.split(":")
        counters[hour[0]] = counters.get(hour[0], 0) + 1

tmp = list()
for k, v in counters.items():
    newKV = (k, v)
    tmp.append(newKV)

tmp.sort()

for k, v in tmp:
    print(k, v)
