import re

with open("zen.txt","r") as f:
    files = f.read()

t = re.findall("Dutch",files,re.IGNORECASE)
print(files)
print(t)
