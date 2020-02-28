# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:11:34 2020

@author: mehmet
"""

# -*- coding: utf-8 -*-

# substring

"""
Substringler metinsel ifadelerde çalışır. Yazdıracağımız metini belirttiğimiz koşula göre keserek yazdırır.
Kesme işlemini yaparken her bir harfe denk gelen boşluğu numaralandırır. Numaralandoırma işlemi daima 0 ile
başlar. Mehmet kelimesini numaralandırırsak M=0 E=1 H=2 şeklinde devam eder.

"""

isim = "Mehmet Erdem"
print(isim[2:5]) #hme yazdırır.
print(isim[2:]) #2 den itibaren her şeyi yazdırır.
print(isim[2:]) #2 ye kadar her şeyi yazdırır.

# len
"""
Len fonksiyonu metnin kaç karakterden oluştuğunu bulmak için kullanılır.

"""

print(len(isim)) #10 yazdıracak


# lower upper
"""
Lower bir metnin tüm karakterlerini küçültmeye , Upper ise Tüm karakterleri büyütmek için kullanılır.
"""

print(isim.upper()) #MEHMET ERDEM
print(isim.lower()) #mehmet erdem

# replace
"""
Replace fonksiyonu metin içerisinde geçen seçtiğimiz bir harfi değiştirmek istediğimiz harfe çevirir.
"""

metin = "Merhaba Dünya"

print(metin.replace("ü","u")) # ü harfini u ile değiştirir.
print(metin.replace("a","e")) # a harfini e ile değiştirir.
"""
fakat değiştirdiğimiz harfler kalıcı olmayacaktır, tek seferliktir. Kalıcı olmasını istiyorsanız aşağıdaki
komutu kullanmalısınız
"""
metin = metin.replace("ü","u")


# split ve strip
"""
Strip yazdıracağımız metnin başı ve sonunda bulunan boşlukları devre dışı bırakmak için kullanılır.
Split yazdıracağımız metinin belirttiğimiz koşula göre ayırır.
örneklere geçtiğiniz zaman daha iyi anlayacaksınız.
"""

Künye = "     Mehmet;Erdem;Akın;19;Sinop ".strip() # Baştaki ve sondaki boşlukları almadan yazacaktır.

print(Künye.split(";")) # Parantez içine noktalı virgül koşulu koyduğumuz için her noktalı virgülde ayıracaktır.
print(Künye.split(";")[0]) # Sona köşeli parantez içinde yazacağımız değer bize o değere denk gelen elemanı verecektir.
print("Adı = " + Künye.split(";")[0]) # hatta biraz süslü hali böyle olacaktır :)

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






















