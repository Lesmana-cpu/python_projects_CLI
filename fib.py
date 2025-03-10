def fibonacci():
    pilihan_n = int(input("mau sampai berapa kali penjumlahannya?\n"))

    print(f"hasil dari perulangan fibonacci dari {pilihan_n} adalah\n")
    
    a, b = 0, 1
    while a < pilihan_n:
        print(a, end=' ')
        a, b = b, a + b
        
if __name__ == "__main__":
    fibonacci()
