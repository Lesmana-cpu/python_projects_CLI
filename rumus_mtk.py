from math import pi

def menghitung_rumus_mtk():
    print(f'''kamu ingin menghitung apa?\n\n1.menghitung volumue segitiga (sama kaki) \U0001F53A \n2.menghitung keliling lingkaran \u26AA 
3.menghitung keliling persegi \u25A0 \n4.menghitung luas persegi \u25A1 \n5.menghitung keliling persegi panjang {'\u25AE'}
6.menghitung luas persegi panjang \u25AD \n7.menghitung volume kubus \U0001F532 \n8.menghitung luas kubus \U0001F533 \n9.menghitung volume balok
10.menghitung luas balok \n11.menghitung volume tabung \n12.menghitung luas tabung \n13.mencari sisi miring segitiga siku-siku \u25E3
        ''')

    while True:
        pilihan = int(input('pilih salah satu menu di atas = '))
        if pilihan == 1:
            alas = float(input('Masukkan alas segitiga: '))
            tinggi = float(input('Masukkan tinggi segitiga: '))
            luas = 0.5 * alas * tinggi
            print(f'Luas segitiga adalah {luas:.2f}\n')

        elif pilihan == 2:
            print("\nPilih cara menghitung keliling lingkaran:")
            print("1. Menggunakan Diameter")
            print("2. Menggunakan Jari-jari")
            opsi = int(input("Masukkan pilihanmu: "))

            if opsi == 1:
                    diameter = float(input('Masukkan diameter lingkaran: '))
                    keliling = pi * diameter
                    print(f'Keliling lingkaran adalah {keliling:.2f}\n')
            elif opsi == 2:
                r = float(input('Masukkan jari-jari lingkaran: '))
                keliling = 2 * pi * r
                print(f'Keliling lingkaran adalah {keliling:.2f}\n')
            else:
                print("Pilihan tidak valid.\n")

        elif pilihan == 3:
            sisi = float(input('Masukkan sisi persegi: '))
            keliling = 4 * sisi
            print(f'Keliling persegi adalah {keliling:.2f}\n')

        elif pilihan == 4:
            sisi = float(input('Masukkan sisi persegi: '))
            luas = sisi ** 2
            print(f'Luas persegi adalah {luas:.2f}\n')

        elif pilihan == 5:
            panjang = float(input('Masukkan panjang: '))
            lebar = float(input('Masukkan lebar: '))
            keliling = 2 * (panjang + lebar)
            print(f'Keliling persegi panjang adalah {keliling:.2f}\n')

        elif pilihan == 6:
            panjang = float(input('Masukkan panjang: '))
            lebar = float(input('Masukkan lebar: '))
            luas = panjang * lebar
            print(f'Luas persegi panjang adalah {luas:.2f}\n')

        elif pilihan == 7:
            sisi = float(input('Masukkan sisi kubus: '))
            volume = sisi ** 3
            print(f'Volume kubus adalah {volume:.2f}\n')

        elif pilihan == 8:
            sisi = float(input('Masukkan sisi kubus: '))
            luas = 6 * (sisi ** 2)
            print(f'Luas permukaan kubus adalah {luas:.2f}\n')

        elif pilihan == 9:
            panjang = float(input('Masukkan panjang balok: '))
            lebar = float(input('Masukkan lebar balok: '))
            tinggi = float(input('Masukkan tinggi balok: '))
            volume = panjang * lebar * tinggi
            print(f'Volume balok adalah {volume:.2f}\n')

        elif pilihan == 10:
            panjang = float(input('Masukkan panjang balok: '))
            lebar = float(input('Masukkan lebar balok: '))
            tinggi = float(input('Masukkan tinggi balok: '))
            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            print(f'Luas permukaan balok adalah {luas:.2f}\n')

        elif pilihan == 11:
            r = float(input('Masukkan jari-jari tabung: '))
            t = float(input('Masukkan tinggi tabung: '))
            volume = pi * (r ** 2) * t
            print(f'Volume tabung adalah {volume:.2f}\n')

        elif pilihan == 12:
            r = float(input('Masukkan jari-jari tabung: '))
            t = float(input('Masukkan tinggi tabung: '))
            luas = 2 * pi * r * (r + t)
            print(f'Luas permukaan tabung adalah {luas:.2f}\n')

        elif pilihan == 13:
            a = float(input('Masukkan sisi pertama: '))
            b = float(input('Masukkan sisi kedua: '))
            c = (a**2 + b**2) ** 0.5
            print(f'Sisi miring segitiga siku-siku adalah {c:.2f}\n')

        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.\n")
                
        userOptions = input('apakah kamu ingin mengulannya?\ny/n : ')
        if userOptions == 'n':
            break


