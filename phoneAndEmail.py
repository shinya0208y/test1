import pyperclip,re

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                  # 市外局番
    (\s|-|\.)?                          # 区切り
    (\d{3})　　　　　　　　　　　　　　   # 3桁の番号　 
    (\s|-|\.)                           # 区切り
    (\d{4})　　　　　　　　　　　　　　　 # 4方の番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?　　  # 内戦番号
    )""",re.VERBOSE)

#TODO:　電子メールの正規表現を作る。
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+  # ユーザ名
    @                  # ＠記号
    [a-zA-Z0-9.-]+     # ドメイン名
    (\.[a-zA-Z]{2,4}   # ドットなんとか
    )""",re.VERBOSE)


#TODO:　クリップボードのテキストを検索する。
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1],groups[3],groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])p

#TODO:　検索結果をクリップボードに貼り付ける。
