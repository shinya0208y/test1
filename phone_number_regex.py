import re

phone_number_regex = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
mo = phone_number_regex.search("私の電話番号は(415)-555-4242です。")
#print("電話番号が見つかりました： " + mo.group())
print(mo.groups())
area_code,main_number = mo.groups()
print("市街局番：" + area_code + "\n番号：" + main_number)


