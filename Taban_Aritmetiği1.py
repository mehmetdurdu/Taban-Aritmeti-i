print('Lütfen Gerçekleştireceğiniz İşlemler İçin Aşağıda ki Menüyü Kullanınız. ')
print('2. İki Tabanında Sayı')
print('4. Dört Tabanında Sayı')
print('8. Sekiz Tabanında Sayı')
print('10. On Tabanında Sayı')
print('16. Onaltı Tabanında (Hexadecimal Sayı)Sayı')
print('İşlem Yaptırmak istediğiniz Sayının Tabanını Menüden Seçiniz.')
def get_source_base():
    x = -1
    x = int(input('Seçtiğiniz Kodu giriniz:  ')) # kullanıcıdan çevirlecek sayıyı ister
    while x!=2 and x!=4 and x!= 8 and x!=10 and x!=16: #girilen sayi  2 8 veya 10 dan birisi değilse
        try:
            x = int(input('geçerli bir taban girmediniz. Geçerli tabanlar 2,8 ve 10. Tekrar deneyiniz. ')) # tekrar girilmesi isteniyor
            if x==2 or x==4 or x==8 or x==10 or x ==16: # yeni girilen sayi 2 8 ve 10 dan biri ise döngü sonlandırılıyor.
                break
        except ValueError:
            print('Tam sayi giriniz...!') # girilen tam sayi değilse hatayı ekrana yazdırır

    return x

def get_target_base():
    y = -1
    y = int(input('Hangi Tabana Çevirmek İstediğini Menüden Seçiniz: \n Seçtiğiniz Kodu Giriniz:  '))
    while y != 2 and y !=4 and y != 8 and y != 10 and y !=16:
        try:
            y = int(input('geçerli bir taban girmediniz. Geçerli tabanlar 2,8 ve 10. Tekrar deneyiniz. '))
            if y == 2 or y ==4 or y == 8 or y == 10 or y ==16:
                break
        except ValueError:
            print('Tam sayi giriniz...!')
    return y

def get_number(source_base): #calışıyor...
    cevrilecek_Sayi = input('Lütfen İşlem Yaptırmak İstediğiniz Sayıyı Giriniz: ') # cevirlecek sayiyi ister
    while True:
        for index, item in enumerate(cevrilecek_Sayi): # sayinin indexini ve rakamını aynı anda döndürür
            if int(item) >= int(source_base): # dönen rakam source_base den büyükse sayiyi yeniden istiyor.
                cevrilecek_Sayi = input('%i tabanında geçerli bir sayi girmediniz tekrar giriniz (%i>=%i):  ' % (int(source_base), int(item), int(source_base)))
                break
            if index+1==len(cevrilecek_Sayi): #döngü sayinın basamakları kadar döndüyse bitir.
                return cevrilecek_Sayi
        if index==len(cevrilecek_Sayi):
            return cevrilecek_Sayi
    return cevrilecek_Sayi

def convert_number(source_base, target_base, number): #çalısıyor.....
    if int(source_base)==10:
        convert_10_to_base(number, target_base)
    else:
        donusen=convert_base_to_10(number,source_base)
        convert_10_to_base(donusen, target_base)

def convert_base_to_10(number, base): #çalısıyor....
    toplam=0
    number= ''.join(reversed(number))
    for index, item in enumerate(number):
        toplam+=int(item)*int(base)**index
    return toplam
def convert_10_to_base(number, base): #çalısıyor.....
    liste=[]
    while int(number)>0:
        tmp=int(number)%int(base)
        liste.append(tmp)
        number=int(number)/int(base)

    liste.reverse()
    b = ''.join(str(i) for i in liste)
    print("SONUC : ",b)

gX=get_source_base()
gY=get_target_base()
num=get_number(gX)
convert_number(gX,gY,num)

