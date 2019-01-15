import re

text = "Arizona 479, 501, 870. California 209, 213, 650. "

t = re.findall("\d",text,re.IGNORECASE)
print(t)

t2 = re.findall("\d*[,.]",text)
print(t2)
