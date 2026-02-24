import socket 

hedef_ip = input("Taranacak ip adresini giriniz: ")
girilen_sifre = input("Lutfen sifreyi giriniz: ")

if girilen_sifre == "root":
    print("---- Sistem Baslatiliyor ----")

    for aktif_port in range(1,100):
        tarayici = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        tarayici.settimeout(0.5)
        sonuc = tarayici.connect_ex((hedef_ip , aktif_port))

        if sonuc == 0:
            print("Port Bulundu: " , aktif_port)
        tarayici.close()
else:
    print("Yetkisiz islem tespit edildi!!")