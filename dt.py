# Date and time

import datetime as dt  # as <-- menyimpan variabel hasil import ke dalam variabel as....

hari_this = dt.date.today()
print(f'{hari_this}\n')

def cek_umur():
    print(10*'=' + ' MASUKKAN TANGGAL BULAN DAN TAHUN KELAHIRAN ANDA ' + 10*'=' + '\n')
    tanggal = int(input('Tanggal lahir mu   = '))
    bulan = int(input('Bulan lahir mu     = '))
    tahun = int(input('Tahun kelahiran mu = '))

    kelahiran = dt.date(tahun, bulan, tanggal)
    print(f'\ntanggal lahir mu adalah = {kelahiran}')
    print(f'hari kelahiran mu adalah = {kelahiran:%A}\n')

    tahun = 'tahun'
    umur_hari = hari_this - kelahiran 
    umur_tahun = umur_hari / 365
    umur_bulan = umur_tahun * 12 

    print(f'Dalam tahun umur mu adalah = {umur_tahun.days} {tahun}')
    print(f'Dalam bulan umur mu adalah = {umur_bulan.days} bulan')
    print(f'Dalam hari umur mu adalah = {umur_hari.days} hari')