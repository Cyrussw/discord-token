# Made by Cyr8s - Sairus
# 6/9/23

import string
import random
import base64
import os

os.system("cls")


def getFirstPart(discord_id):
    try:
        discord_id_bytes = str(discord_id).encode("ascii")
        base64_encoded_id = (
            base64.b64encode(discord_id_bytes).decode("ascii").rstrip("=")
        )
        return base64_encoded_id
    except Exception as e:
        return f"Token alınmaya çalışırken bir hata oluştu! {e}"


def getSecondaryPart():
    try:
        characters = list(string.ascii_letters + string.digits)
        auth = "".join(random.sample(characters, 6))
        return auth
    except Exception as e:
        return e


def getLastPart():
    try:
        characters = list(string.ascii_letters + string.digits)
        rand = "".join(random.sample(characters, 29))
        return rand
    except Exception as e:
        return f"Random oluşturulmaya çalışırken bir hata oluştu! {e}"


def createTxt(dcId):
    part1 = getFirstPart(dcId)

    with open(f"{dcId}-tokenler.txt", "w") as dosya:
        for i in range(100000):
            part2 = getSecondaryPart()
            part3 = getLastPart()
            all = f"{part1}.{part2}.{part3}"
            dosya.write(all + "\n")


MENU_UI = """Sairus: Token Solver'a Hoş Geldiniz!

1) Sadece ID giriniz.
2) Çıkış - (çıkış yazman yeterli!)
"""

print(MENU_UI)

while True:
    discord_id = input("Discord ID: ")

    if not discord_id:
        print("Sairus: Lütfen ID girin.")
    elif discord_id == "çıkış":
        print("Sairus: Yine Bekleriz.")
        exit(0)
    else:
        print("Sairus: İşlem Başlıyor!")
        createTxt(discord_id)
        print("Sairus: 100000 Token oluşturuldu!")