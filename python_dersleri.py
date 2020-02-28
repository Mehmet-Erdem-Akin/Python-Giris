# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:05:22 2020

@author: mehmet
"""
#Yazdırma("Çıktı Alma")


"""
Python'da yazdırma işlemi 
"""

print("yazılacak metin veya rakam")
print(123456789)
 
"""
ile gösterilir
"""

#Veri Tipleri:

"""
   
Integer - İnt :(Tamsayılar ): Matematikte gördüğümüz pozitif ve negatif sayıların tamamına denir ve 
Python da bir temel sayısal veri türüdür. Örnek verecek olursak; 5, -10, 423365 vb.

"""
print(5)
print(-10)
print(9384738)

"""

Float -  :(Ondalıklı sayılar): Matematikte gördüğümüz kesirli negatif ve pozitif sayıların tamamına denir. 
Integer gibi Python da bir sayısal temel veri türüdür. Örneğin; -1.25, 8.20, 66.40 vb.

"""
print(-125)
print(-1.25)
print(66.40)

"""

String - Str :(metinsel ifadeler): Stringler kullandığımız a,b,c veya tırnak içinde olduğu takdirde yazılan 
rakamlar gibi metinsel karakterleri ifade eder. Tırnak işareti ile kullanılır. Örneğin; "Mehmet" , "Erdem" , "Akın" , "36663" , "57AT643"

"""
print('tek tırnak ile veya')
print("çift tırnak ile veya")
print("""üç tırnak ile""")

# input
""" 
İnputlar kullanıcıdan veri almak için kullanılır. Kullanıcının girdiği veriyi genelde bir değişkene
atayarak kullanırız
"""
input() # çalıştırdığımız zaman bizden bir veri girmemiz bekleniyor olacak fakat bunu string ile 
# birleştirirsek daha anlamlı bir ifade ortaya çıkar.

input("Adınızı giriniz : ?") # şuan adınızı girin diye belirteceği için ne gireceğimizi anlamış olduk

ad = input("Adınız?") # eğer girdimiz bir değişkene atanırsa o veriyi ileride çağırabiliriz.

# KÜÇÜK BİR ÖRNEK


ad = input("Lütfen isminizi giriniz : ") # kullanıcıdan ismini istedik
soyad = input("Lütfen soyadınızı giriniz : ") # kullanıcıdan soyadınız istedik 

print("Hoşgeldin"+" "+ ad + " "+ soyad)

# VEYA

ad = input("Lütfen isminizi giriniz : ") # kullanıcıdan ismini istedik
soyad = input("Lütfen soyadınızı giriniz : ") # kullanıcıdan soyadınız istedik 

print("Hoşgeldin",ad,soyad)

# GİRDİLER İLE MATEMATİK İŞLEMLERİ ÖRNEĞİ
# Toplama
print("Toplama İşlemine Hoşgeldiniz Toplamak İstediğiniz Sayıları Giriniz !!! ")

sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ")
print("Toplamları : ",int(sayi1) + int(sayi2))

#Çıkarma
print("Çıkarma İşlemine Hoşgeldiniz Toplamak İstediğiniz Sayıları Giriniz !!! ")

sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ")
print("Kalan : ",int(sayi1) - int(sayi2))





