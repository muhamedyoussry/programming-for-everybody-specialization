fileName = input("Enter file name: ")
fh = open(fileName)
result = 0
count = 0

for line in fh:
    if "X-DSPAM-Confidence:" in line:  # line.startwith("X-DSPAM-Confidence:")
        strPos = line.find(":")
        number = float(line[strPos+1:])
        result = result + number
        count = count + 1

print("Average spam confidence:", result/count)
