import random
import main

def start():
    nama = input(f"masukkan nama  ")
    print(f"\n hai  {nama}")

    while True:
        shape_goa = "|_|"
        goa_kosong = [shape_goa] * 5

        position = random.randint(1, 5)

        goa = goa_kosong.copy()
        goa[position - 1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        print(f"\n coba perhatikan goa di bawah ini \n \n {goa_kosong}")

        pilihan = int(input("menurut mu ada di goa no berapa suki liar itu berada 1/2/3/4/5? = "))
        
        if pilihan == position:
            print(f"\n good!! {nama} \n si suki memang ada di goa no {position}\n{goa} ini piala untuk mu \U0001F3C6")
        else:
            print(f"\n lol {nama} \n si suki itu ada di goa \n {goa}")

        play_again = input("\n  apakah kamu ingin memulai ulang gamenya? [y/n]")
        if play_again == "n":
            main.menu()
    
if __name__ == '__main__':
    start()
