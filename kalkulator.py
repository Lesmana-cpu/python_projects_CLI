def start():
  while True:
        awal = int(input("masukkan angka awal...\n"))
        akhir = int(input("masukkan akhir...\n"))

        kali = awal * akhir
        bagi = awal / akhir
        kurang = awal - akhir
        tambah = awal + akhir
        pangkat = awal ** akhir                       #ini eksponen
        mod = awal % akhir                      #ini modulus (sisa dari pembagian) 2:8 hasilnya 2 karena pembilangnya lebih  kecil dari pada penyebutnya
        flo_div = awal // akhir                  #ini floor division (hasil pembagian di bulatkan ke bawah) 2:8 hasilnya 0 karena 2 lebih kecil dari 8


        pilihan = str(input("ini mau di\n bagi = : \n tambah = +\n kali = x\n kurang = -\n pangkat = * \n modulus = % \n flo  = //\nsilahkan di pilih mau di apain..."))

        if pilihan == ":":
            print(f"hasilnya adalah = \n {bagi}")
        elif pilihan == "+":
           print(f"hasilnya adalah = \n {tambah}")
        elif pilihan == "-":
            print(f"hasilnya adalah = \n {kurang}")
        elif pilihan == "x":
            print(f"hasilnya adalah = \n {kali}")
        elif pilihan == "*":
            print(f"hasilnya adalah = \n {pangkat}")
        elif pilihan == "%":
            print(f"hasilnya adalah = \n {mod}")
        elif pilihan == "//":
            print(f"hasilnya adalah = \n {flo_div}")
        else:
            print("tolol kamu dan ulangi programnya")
            start()
            
        pilihan= input(str("apakah kamu ingin mengulangi kalkulatornya? y/n \n")) 
        if pilihan == "n":
            print("kalkulator di hentikan")
            break   
        elif pilihan == "y":
            print("\nkalkukator di mulai ulang \n")
            
        else:
            print("ya udah berhenti")
            
            
if __name__ == '__main__':
    start()