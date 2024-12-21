import time

kulAdi = "taha"
sifre = "12345"

hata_Hakki = 3

yemekler = ["1-) Döner: 80", "2-) Tavuk Pilav: 50", "3-) Kebap: 150", "4-) Ayran: 15", "5-) Kola: 35", "6-) Çıkış", " "]
sepet = []
tutar = 0

while hata_Hakki > 0:
    
    girilen_kulAdi = input("Kullanıcı Giriniz: ")
    girilen_Sifre = input("Şifrenizi Giriniz: ")
    
    if kulAdi == girilen_kulAdi and sifre == girilen_Sifre:
        print("Hoş Geldiniz")
        time.sleep(2)
        break
        
    elif kulAdi == girilen_kulAdi and sifre != girilen_Sifre:
        print("Hatalı Şifre")
        hata_Hakki = hata_Hakki - 1
        
    elif kulAdi != girilen_kulAdi and sifre == girilen_Sifre:
        print("Hatalı Kullanıcı Adı")
        hata_Hakki = hata_Hakki - 1
        
    else:
        print("Hatalı Kullanıcı Adı ve Şifre")
        hata_Hakki = hata_Hakki - 1

print(" ")
print("******* Ne Yemek İstersiniz? *******")   
print(" ") 

for i in yemekler:
    print(i)
    
while True:
    secim = input("Numaralarını Giriniz: ")
    
    if secim == "1":
        sepet.append("Döner")
        tutar = tutar + 80
        
    elif secim == "2":
        sepet.append("Tavuk Pilav")
        tutar = tutar + 50
    
    elif secim == "3":
        sepet.append("Kebap")
        tutar = tutar + 150
        
    elif secim == "4":
        sepet.append("Ayran")
        tutar = tutar + 15
        
    elif secim == "5":
        sepet.append("Kola")
        tutar = tutar + 35
        
    elif secim == "6":
        break
    else:
        print("Hatalı Giriş")
        
time.sleep(2)
        
adres = input("Adresinizi Giriniz: ")

print(" ")
print("******* Siparişiniz Adresinize Gönderiliyor *******")
print(" ")
print("Adresiniz: " + adres)
print(" ")
print("Sepet: ")
print(" ")
for i in sepet:
    print(i)

print(" ")    
print("Sipariş Tutarı: " , tutar)

print("Siparişiniz İçin Teşekkür Ederiz")
    