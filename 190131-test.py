import re

pn = re.compile(r"(\(\d\d\))\+(\d\d\d)")
mo = pn.search("(22)+455test33+789ssss")
n1,n2 = mo.groups()

print(mo.group())
print(mo.groups())
print(n1)
print(n2)

