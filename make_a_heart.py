import math
from turtle import *

def heart_a(k):
    return 16 * math.sin(k)**3  

def heart_b(k):
    return 13 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
           math.cos(3 * k) - \
           math.cos(4 * k)

speed(3)  # Kecepatan tertingg
tracer(1, 1)  # Menonaktifkan animasi untuk mempercepat
bgcolor("black")

color("red")
fillcolor("red")
begin_fill()

penup()
goto(heart_a(0) * 20, heart_b(0) * 20)
pendown()

# Menggambar hati dengan rentang sudut yang lengkap (0 hingga 2 * pi)
for i in range(0, 628):  # 628 = 200 * pi (untuk mencakup 0 hingga 2 * pi)
    k = i / 100  # k akan berkisar dari 0 hingga 6.28 (2 * pi)
    goto(heart_a(k) * 20, heart_b(k) * 20)

end_fill()  # **Akhiri pengisian warna merah**

penup()
# goto(-50, -10)
goto(0, -10)
pendown()
color("black")
write(f'I just want to say:\n\n"I Love You"', align="center", font=("Times New Roman", 24, "bold italic"))


hideturtle()
update()  # **Langsung tampilkan hasilnya tanpa animasi**
done()