#!/usr/bin/env python
import os
os.system("apt-get install git")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet monsterx")
print("""
Merhaba! monsterx aracına hoşgeldiniz.

Aşağıdan yapmak istediğiniz işlemi seçiniz;

""")
print("""
1) SQLmap		6) Metasploit

2) Zphisher		7) Nikto

3)PhoneInfoga		8) Fsociety

4) Ip-Tracer		9) Hydra

5) RED_HAWK		10) Hammer

Hepsini Kurmak İçin A Tuşuna Basınız.

""")
islemNumara = str(input("Seçiminizi Yapınız: "))

if(islemNumara == "1"):
	os.system("clear")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "2"):
	os.system("clear")
	os.system("git clone https://github.com/htr-tech/zphisher")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "3"):
	os.system("clear")
	os.system("git clone https://github.com/sundowndev/phoneinfoga")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "4"):
	os.system("clear")
	os.system("git clone https://github.com/rajkumardusad/IP-Tracer")
	print("Başarıyla Yüklendi!")

	
elif(islemNumara == "5"):
	os.system("clear")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "6"):
	os.system("clear")
	os.system("git clone https://github.com/rapid7/metasploit-framework")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "7"):
	os.system("clear")
	os.system("git clone https://github.com/sullo/nikto")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "8"):
	os.system("clear")
	os.system("git clone https://github.com/Manisso/fsociety")
	print("Başarıyla Yüklendi!")


elif(islemNumara == "9"):
	os.system("git clone https://github.com/vanhauser-thc/thc-hydra")
	print("Başarıyla Yüklendi!")

elif(islemNumara == "10"):
	os.system("clear")
	os.system("git clone https://github.com/cyweb/hammer")
	print("Başarıyla Yüklendi!")



elif(islemNumara == "A", "a"):
	os.system("clear")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("git clone https://github.com/sundowndev/phoneinfoga")
	os.system("git clone https://github.com/rajkumardusad/IP-Tracer")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("git clone https://github.com/rapid7/metasploit-framework")
	os.system("git clone https://github.com/sullo/nikto")
	os.system("git clone https://github.com/Manisso/fsociety")
	os.system("git clone https://github.com/vanhauser-thc/thc-hydra")
	os.system("git clone https://github.com/cyweb/hammer")	

else:
	print("Böyle Bir Seçenek Bulunamadı!")
