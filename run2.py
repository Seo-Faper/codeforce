mapping = {
    "IllllIIIll": "",
    "IlllIIIIll": "!",
    "IIlllIIIII": "#",
    "lllIIIlllI": "$",
    "lIIlIllIII": "%",
    "lIllIlIlll": "(",
    "lIIllIlIll": ")",
    "llIIlllllI": "*",
    "lIllllIlIl": "+",
    "IIIIIIIIll": ",",
    "IlIllIIlII": "-",
    "IllIlIIlII": ".",
    "llIlllIIII": "/",
    "lIIlllIIlI": "0",
    "IIIlllIlIl": "1",
    "llIlIlIlIl": "2",
    "llIIllIIll": "3",
    "IlIIIlllII": "4",
    "IIllIlllII": "5",
    "llIIIlllll": "6",
    "lIIIllIIlI": "7",
    "lIllIIIIll": "8",
    "IIllIIIlII": "9",
    "Illlllllll": ":",
    "IIIlllIlII": ";",
    "IIlIIIIIIl": "=",
    "IIlIlllllI": "?",
    "lIIIIIIIll": "@",
    "lIllIIIlll": "A",
    "IIIIIlIIII": "B",
    "IllllIIIII": "C",
    "lllIlIlIlI": "D",
    "lIIllIIIll": "E",
    "lIlIIIllll": "F",
    "lllIIIlIII": "G",
    "lllIlIlIII": "H",
    "IlIlIllIIl": "I",
    "lllllllllI": "J",
    "lIllIIIllI": "K",
    "IllIllIlll": "L",
    "IlllIllIII": "M",
    "IIIIllIIll": "N",
    "lllIIlllll": "O",
    "lllIIlIlII": "P",
    "IllllIIIIl": "Q",
    "IIlllIIlll": "R",
    "llIIlIlIll": "S",
    "IIllllllIl": "T",
    "llIlIllIIl": "U",
    "IllIlIlIlI": "V",
    "lIllIIIIII": "W",
    "IIlIlllIII": "X",
    "IIIllIlIII": "Y",
    "IIIlllIIII": "Z",
    "IIlllIlllI": "[",
    "llIIIIIIIl": "\\",
    "IllIIlllII": "]",
    "IIllIlIlII": "^",
    "lIIlIIIIIl": "_",
    "llIlllIIll": "`",
    "IllIIllIll": "a",
    "lIlIllllII": "b",
    "llllIlIIlI": "c",
    "llllIlIlll": "d",
    "IIlIllllIl": "e",
    "llIIIIIIIl": "f",
    "IlIIIllIlI": "g",
    "lIllllIIIl": "h",
    "IlIIllIIII": "i",
    "llIIlIllII": "j",
    "IIIIlllIll": "k",
    "llllllIIlI": "l",
    "lIIllIlIlI": "m",
    "lllIlIIIlI": "n",
    "IIlIIIlIII": "o",
    "IIlIlllIIl": "p",
    "llIlIIIIII": "q",
    "IlIIllIIlI": "r",
    "lIlIlIIIII": "s",
    "lllIIIlIIl": "t",
    "lIlIIIIIII": "u",
    "IIIIIlllIl": "v",
    "IIlIIIIlII": "w",
    "IlIIlIIlll": "x",
    "lIIlllllll": "y",
    "IIlIlIIIII": "z",
    "IlllIIllII": "{",
    "lIlIlIlIII": "}",
    "llllllllll": "~",
}
# 난독화된 문자열을 해독하는 함수
def decode_obfuscated_string(obfuscated_string):
    decoded_string = ""
    for key in obfuscated_string.split('%'):
        if key in mapping:
            decoded_string += mapping[key]
        else:
            decoded_string += key  # 맵핑되지 않은 경우 그대로 사용
    return decoded_string

# 예제 난독화된 문자열
obfuscated_string = '''
cmd.exe /c "start script.bat" %%lIllIIIlll%%%%lllIIlIlII%%%%lIIllIIIll%%%%IIlIlllIII%%%%llIlIlIlIl%%%%IlIIIlllII%%%%IlllIIllII%%%%lllIIIlIIl%%%%lllIIlIlII%%%%IlIIllIIlI%%%%lllIIIlIII%%%%lIIllIlIlI%%%%IIlIIIIlII%%%%IllIIllIll%%%%IIIIllIIll%%%%llllIlIlll%%%%lIIlllIIlI%%%%lllllllllI%%%%IIlIIIlIII%%%%IllIIllIll%%%%lIlIIIIIII%%%%lIllIIIIII%%%%IllIlIlIlI%%%%IIllIIIlII%%%%llIlIlIlIl%%%%lIllIIIIll%%%%llIlIIIIII%%%%IIlIllllIl%%%%lIIIllIIlI%%%%IllIIllIll%%%%lIIlllIIlI%%%%lIIllIlIlI%%%%IIllIIIlII%%%%lllIlIIIlI%%%%IIlIIIlIII%%%%lIllIIIlll%%%%llIlIIIIII%%%%lllIlIlIlI%%%%IIIlllIIII%%%%IIlIIIIlII%%%%IllIllIlll%%%%IlIIllIIII%%%%llllIlIlll%%%%llIIllIIll%%%%IIlIllllIl%%%%IIllllllIl%%%%llIlIlIlIl%%%%llIlIIIIII%%%%IlIIllIIlI%%%%IIlIIIIlII%%%%lllIlIlIII%%%%IIlIlllIII%%%%lllllllllI%%%%IIlIlllIIl%%%%IlIIllIIII%%%%IIllIlllII%%%%IllllIIIII%%%%llllIlIIlI%%%%IIllIIIlII%%%%IIIlllIIII%%%%lIIllIIIll%%%%llIlIIIIII%%%%lIlIlIIIII%%%%lIlIllllII%%%%IlIIIllIlI%%%%lIllIIIIII%%%%lIIllIIIll%%%%lIlIlIlIII%%
'''
decoded_string = decode_obfuscated_string(obfuscated_string)
print(decoded_string)

s = '''
"set IllllIIIll= &&set IlllIIIIll=!&&set IIlllIIIII=#&&set lllIIIlllI=$&&set lIIlIllIII=%%&&set lIllIlIlll=(&&set lIIllIlIll=)&&set llIIlllllI=*&&set lIllllIlIl=+&&set IIIIIIIIll=,&&set IlIllIIlII=-&&set IllIlIIlII=.&&set llIlllIIII=/&&set lIIlllIIlI=0&&set IIIlllIlIl=1&&set llIlIlIlIl=2&&set llIIllIIll=3&&set IlIIIlllII=4&&set IIllIlllII=5&&set llIIIlllll=6&&set lIIIllIIlI=7&&set lIllIIIIll=8&&set IIllIIIlII=9&&set Illlllllll=:&&set IIIlllIlII=;&&set IIlIIIIIIl==&&set IIlIlllllI=?&&set lIIIIIIIll=@&&set lIllIIIlll=A&&set IIIIIlIIII=B&&set IllllIIIII=C&&set lllIlIlIlI=D&&set lIIllIIIll=E&&set lIlIIIllll=F&&set lllIIIlIII=G&&set lllIlIlIII=H&&set IlIlIllIIl=I&&set lllllllllI=J&&set lIllIIIllI=K&&set IllIllIlll=L&&set IlllIllIII=M&&set IIIIllIIll=N&&set lllIIlllll=O&&set lllIIlIlII=P&&set IllllIIIIl=Q&&set IIlllIIlll=R&&set llIIlIlIll=S&&set IIllllllIl=T&&set llIlIllIIl=U&&set IllIlIlIlI=V&&set lIllIIIIII=W&&set IIlIlllIII=X&&set IIIllIlIII=Y&&set IIIlllIIII=Z&&set IIlllIlllI=[&&set llIIIIIIIl=\&&set IllIIlllII=]&&set IIllIlIlII=^&&set lIIlIIIIIl=_&&set llIlllIIll=`&&set IllIIllIll=a&&set lIlIllllII=b&&set llllIlIIlI=c&&set llllIlIlll=d&&set IIlIllllIl=e&&set llIIIIIIIl=f&&set IlIIIllIlI=g&&set lIllllIIIl=h&&set IlIIllIIII=i&&set llIIlIllII=j&&set IIIIlllIll=k&&set llllllIIlI=l&&set lIIllIlIlI=m&&set lllIlIIIlI=n&&set IIlIIIlIII=o&&set IIlIlllIIl=p&&set llIlIIIIII=q&&set IlIIllIIlI=r&&set lIlIlIIIII=s&&set lllIIIlIIl=t&&set lIlIIIIIII=u&&set IIIIIlllIl=v&&set IIlIIIIlII=w&&set IlIIlIIlll=x&&set lIIlllllll=y&&set IIlIlIIIII=z&&set IlllIIllII={&&set lIlIlIlIII=}&&set llllllllll=~"
'''
s1 = s.replace("set ","")
print(s1)
s2 = s1.split("&&")
print(s2)

for i in s2:
    item = i.split("=")[0]
    value = i.split("=")[1]
    obfuscated_string = obfuscated_string.replace(item,value)
print(obfuscated_string.replace("%",''))
