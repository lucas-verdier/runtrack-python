import re

count: int = 0

with open('domains.xml') as f:
    line = f.readlines()
    regex = r'\.[a-zA-Z]{2,}'
    for l in line:
        if re.search(regex, l):
            count += 1


print(count)
