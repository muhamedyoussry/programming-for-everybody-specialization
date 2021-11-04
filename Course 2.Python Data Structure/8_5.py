fname = input("Enter the file name: ")

fh = open(fname)
counter = 0

for line in fh:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            MailCC = line.split()
            print(MailCC[1])
            counter = counter + 1
    else:
        continue

print("There were", counter, "lines in the file with From as the first word")
