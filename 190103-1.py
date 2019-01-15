import re

texts = "The ghost that says boo haunts the loo"

t = re.findall("oo",texts,re.IGNORECASE)
print(t)
