import time

hedef_ip = input("Taranacak ip adresini giriniz: ")
girilen_sifre = input("Lutfen sifreyi giriniz: ")

if girilen_sifre == "root":
    print("Erisim onaylandi!" + hedef_ip + "taranmaya basliyor.")
    print("---------------------------------------")


    for aktif_port in range (1,100):
        print("Taraniyor -> port:" , aktif_port)
        time.sleep(0.01)


else:
    print("Yetkisiz islem tespit edildi! Sistem kilitleniyor.")