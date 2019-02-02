import re

hero_regex = re.compile(r"059-(86\||68|88)")
mo1 = hero_regex.search("059-86|-6919")
mo2 = hero_regex.search("059-68-2120")
mo3 = hero_regex.search("059-88-2120")
print(mo1.group(1))
print(mo2.group(1))
print(mo3.group(1))
