import re

line = "my name is mohamedyoussryahmed@gmail.com, i am 20 years old. Thanks"

print (re.findall("@([^,]+),", line))


