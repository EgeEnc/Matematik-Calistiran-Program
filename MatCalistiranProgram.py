
import os
import random
if os.name == "nt":
    os.system("color a")
    os.system("title Basit bir Matematik Programi---Tasarlayan---Ege Enc")

print("Basit bir Matematik Programi","\n"*4)

print("Tasarlayan:Ege Enc","\n"*4)

def SoruUret():
  while True:
    sayilar = []
    for i in range(random.randrange(2,5)):
        sayilar.append(str(random.randrange(1,10)))
    bulunanislem = ""
    for bitir in sayilar:
        bulunanislem += bitir
        bulunanislem += random.choice(["+", "-", "*", "/"])
    bulunanislem = str(bulunanislem[:-1])
    if len(str(eval(bulunanislem))) > 3:
        continue
    return bulunanislem
while True:
    uretilenSoru = SoruUret()
    soruCevabi = eval(uretilenSoru)
    while True:
     try:
        sor = float(input("{} isleminin sonucu kac eder?".format(uretilenSoru)))
        break
     except:
        print("Lutfen bir sayi giriniz!")
        continue
    if sor == soruCevabi:
        print("Tebrikler!Dogru cevap.")
    elif sor != soruCevabi:
        print("Yanlis cevap!Dogru cevap {}".format(soruCevabi))