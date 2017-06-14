#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
tasarlayan = "Ege Enç"
if os.name == "nt":
    os.system("color a")
    os.system("title Basit bir Matematik Programı---Tasarlayan---{}".format(tasarlayan))

print("Basit bir Matematik Programı","\n"*4)

print("Tasarlayan:{}".format(tasarlayan),"\n"*4)

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
        sor = float(input("{} işleminin sonucu kaç eder?".format(uretilenSoru)))
        break
     except:
        print("Lütfen bir sayı giriniz!")
        continue
    if sor == soruCevabi:
        print("Tebrikler!Doğru cevap.")
    elif sor != soruCevabi:
        print("Yanlış cevap!Doğru cevap {}".format(soruCevabi))