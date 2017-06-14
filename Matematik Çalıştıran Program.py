
import os
import random
if os.name == "nt":
    os.system("color a")
    os.system("title Basit bir Matematik Programi---Tasarlayan---Ege Enc")

print("Basit bir Matematik Programı","\n"*4)

print("Tasarlayan:Ege Enc","\n"*4)

def SoruUret():
  while True:
    sayilar = []
    for i in range(random.randrange(2,5)):
        sayilar.append(str(random.randrange(1,10)))
    bulunanİslem = ""
    for bitir in sayilar:
        bulunanİslem += bitir
        bulunanİslem += random.choice(["+", "-", "*", "/"])
    bulunanİslem = str(bulunanİslem[:-1])
    if len(str(eval(bulunanİslem))) > 3:
        continue
    return bulunanİslem
while True:
    uretilenSoru = SoruUret()
    soruCevabi = eval(uretilenSoru)
    while True:
     try:
        sor = float(input("{} isleminin sonucu kac eder?".format(uretilenSoru)))
        break
     except:
        print("Lütfen bir sayi giriniz!")
        continue
    if sor == soruCevabi:
        print("Tebrikler!Dogru cevap.")
    elif sor != soruCevabi:
        print("Yanlis cevap!Dogru cevap {}".format(soruCevabi))