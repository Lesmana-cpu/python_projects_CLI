from library import welcome, exit_program
from games import suki
import library
import kalkulator
from fib import fibonacci
from konver_suhu import perbandingan_suhu
import datetime as dt
import rumus_mtk
from dt import cek_umur

def menu():
    user_option = int(input ('''menu program ini:\n1. games menangkap suki liar \U0001F47D\n2. kalkulator \U0001F5A9 \n3. menghitung beberapa macam rumus MTK\n4. menghitung fibonacci \n5. hitung perbandingan suhu \U0001F321 \n6. menghitung umur (otomatis)
                             \nsilahkan pilih no berapa yang anda inginkan: '''))
    if user_option == 1:
         suki.start()
    elif user_option == 2:
         kalkulator.start()
    elif user_option == 3:
         rumus_mtk.menghitung_rumus_mtk()
    elif user_option == 4:
         fibonacci()
    elif user_option == 5:
         perbandingan_suhu()
    elif user_option == 6:
         cek_umur()
    else: 
         print("hanya boleh yang ada di menu ")
         
def program():
    welcome("WELCOME TO PROGRAM MADE BY LESMANA!! \U0001F60E")
    menu()
    print("\nprogramnya telah selesai\n")
    pilihan = str(input("apakah anda ingin mengulangi dari menu?  y/n = "))
    if pilihan == "y":
        program()
    else:
        print("program selesai, terimakasih telah memakai program saya (lesmana/L7)")
        waktu = dt.date.today()
        print(f'tanggal = {waktu}\nhari = {waktu:%A}')   # <-- %A untuk menunjukan hari
    
if __name__ == '__main__':
    program()
    
                                                    # MADE BY LESMANA
                                        
    

