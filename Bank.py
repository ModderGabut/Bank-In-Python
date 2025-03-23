import os as o
import time as t
from datetime import datetime as dt
from colorama import Fore, Back, Style

class Bank:
    def __init__(self):
        self.nasabah = self.load_data()
        
    def load_data(self):
      try:
        with open(".data.txt", "r") as file:
            self.nasabah = {}
            for line in file.readlines():
                values = line.strip().split(",")
                nama = values[0]
                saldo = ",".join(values[1:])
                self.nasabah[nama] = saldo
            return self.nasabah
      except FileNotFoundError:
        return main
      except Exception as e:
        print(f"Error: {e}")

    def save_data(self):
      with open(".data.txt", "w") as file:
        for nama, saldo in self.nasabah.items():
            saldo_int = int(saldo.replace(',', ''))
            file.write(f"{nama},{saldo_int:,}\n")

    def buat_rekening(self, nama, saldo):
        o.system('clear')
        self.nasabah[nama] = saldo
        self.save_data()
        print(f"Rekening {nama} berhasil dibuat dengan saldo {saldo}.")
        t.sleep(1)
        o.system('clear')

    def cek_saldo(self, nama):
        o.system('clear')
        if nama in self.nasabah:
            print(f"Saldo {nama} adalah {self.nasabah[nama]}.")
            t.sleep(1)
        else:
            print(f"Rekening {nama} tidak ditemukan.")
            t.sleep(1)

    def setor(self, nama, jumlah):
      o.system('clear')
      if nama in self.nasabah:
        jumlah_int = int(jumlah.replace(',', '')) 
        saldo_int = int(self.nasabah[nama].replace(',', ''))
        saldo_baru = saldo_int + jumlah_int
        self.nasabah[nama] = "{:,}".format(saldo_baru)
        self.save_data()
        print(f"Setor {jumlah.replace(',', ',')} ke rekening {nama} berhasil. Saldo: {self.nasabah[nama]}")
        t.sleep(1)
      else:
        print(f"Rekening {nama} tidak ditemukan.")
        t.sleep(1)

    def tarik(self, nama, jumlah):
      o.system('clear')
      if nama in self.nasabah:
        saldo = int(self.nasabah[nama].replace(',', ''))
        jumlah = int(jumlah.replace(',', ''))
        if saldo >= jumlah:
            self.nasabah[nama] = "{:,}".format(saldo - jumlah)
            self.save_data()
            print(f"Penarikan {jumlah} dari rekening {nama} berhasil.")
            t.sleep(0.5)
        else:
            print(f"Saldo {nama} tidak cukup.")
            t.sleep(0.5)
      else:
        print(f"Rekening {nama} tidak ditemukan.")
        t.sleep(0.5)

    def see_bank_acount(self):
      try:
        with open(".data.txt", "r") as file:
          print(file.read())
          print("\n(udin=nama nasbah/100000=uang/saldo)")
          t.sleep(3)
          o.system('clear')
      except FileNotFoundError:
        return main

    def about(self):
      o.system('clear')
      try:
        with open(".ab.txt", "r") as ab:
          print(ab.read())
          t.sleep(5)
      except FileNotFoundError:
        return main

def main():
  bank = Bank()
  while True:
    o.system('clear')
    o.system('cowsay -f eyes Made By Modder_Gabut| lolcat')
    o.system('figlet Bank Menu | lolcat')
    print("")
    print(Fore.GREEN + Style.BRIGHT + "1. Buat Rekening" + Fore.RESET)
    print(Fore.GREEN + "2. Cek Saldo" + Fore.RESET)
    print(Fore.BLUE + "3. Setor" + Fore.RESET)
    print(Fore.BLUE + "4. Tarik" + Fore.RESET)
    print(Fore.MAGENTA + "5. Lihat Nasabah/See Account" + Fore.RESET)
    print(Fore.RED + "0. Exit" + Fore.RESET)
    choose = input(Back.BLACK + Fore.WHITE + "Silahkan Memilih: "+ Back.RESET + Fore.RESET)
  
    if choose == "1":
      nama = input("Masukkan nama nasabah: ")
      saldo = input("Masukkan saldo awal: ")
      bank.buat_rekening(nama, saldo)
    elif choose == "2":
      nama = input("Masukkan nama nasabah: ")
      bank.cek_saldo(nama)
    elif choose == "3":
      nama = input("Masukkan nama nasabah: ")
      jumlah = input("Masukkan jumlah setor: ")
      bank.setor(nama, jumlah)
    elif choose == "4":
      nama = input("Masukkan nama nasabah: ")
      jumlah = input("Masukkan jumlah tarik: ")
      bank.tarik(nama, jumlah)
    elif choose == "5":
      bank.see_bank_acount()
    elif choose == "about":
      bank.about()
    elif choose == "0":
        print(Back.RED + Fore.WHITE + 'Exited!' + Fore.RESET + Back.RESET)
        break
    elif choose == "reset":
      o.system('rm .data.txt')
      break
    else:
      print(Fore.WHITE + Back.RED + "Pilihan tidak valid. Silakan coba lagi." + Fore.RESET + Back.RESET)
      t.sleep(5)
      o.system('clear')
    
if __name__ == "__main__":
    main()
