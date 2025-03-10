# import socket
# pc_name = socket.gethostname()
from time import sleep
import datetime as dt


def welcome(judul):
    style = "\U0001F667" *  (len(judul) + 8)
    print(style)
    print(f"## {judul}  ##")
    print(style)
    
def exit_program():
    print("program akan di hentikan dalam")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("program telah dihentikan \U0001F667")


# bisa untuk pengujian hasil output, pas di file ini
if __name__ == '__main__':  
    welcome("LESMANA GAME")
    exit_program()