import re

fh = open("actual.txt")

total = 0
result = []

for line in fh:
    line = line.rstrip()
    result = result + re.findall("[0-9]+", line)

result_int = [int(x) for x in result]
total = sum(result_int)

print(total)
