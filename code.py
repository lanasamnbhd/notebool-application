notDefteri=[]

def secenekler():
    print("not defteri uygulaması")
    print("1. yeni not ekle")
    print("2. notu sil")
    print("3. notları görüntüle")
    print("4. çıkış yap")

def notEkle():
    yeniNot=input("yeni notu girin: ")
    notDefteri.append(yeniNot)
    print("not eklendi")

def notSil():
    notNo=int(input("silmek istediğiniz notun numarasını giriniz: "))
    if 1<=notNo<=len(notDefteri):
        notDefteri.pop(notNo-1)
        print("not silindi")
    else:
        print("girdiğiniz numaraya uygun not bulunamadı")

def notGoruntule():
    if not notDefteri:
        print("not defteri boş. not ekleyin")
    else:
        for i, notO in enumerate(notDefteri,1):
            print(f"{i}. {notO}")

while True:
    secenekler()
    secim=int(input("yapmak istediğiniz işlemi seçiniz(1/2/3/4): "))

    if secim==1:
        notEkle()
    elif secim==2:
        notSil()
    elif secim==3:
        notGoruntule()
    elif secim==4:
        print("çıkış yapıldı...")
        break
    else:
        print("bir hata oluştu, tekrar deneyin.")
