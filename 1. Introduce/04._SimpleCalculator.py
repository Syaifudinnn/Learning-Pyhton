#header
print('----------------------')
print('----- Calculator -----')
print('----------------------')

#fungsi calculator
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#menu calculator
print('\nPilih operasi : ')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Keluar')

#input menu
while True:
    pilihan = int(input('\nMasukkan pilihan (1-5) : '))

    if pilihan == 5:
        print('\nTerima kasih!')
        break
    elif pilihan < 1 or pilihan > 5:
        print('Pilihan tidak valid!')
        continue

    no1 = float(input('Masukkan angka pertama : '))
    no2 = float(input('Masukkan angka kedua   : '))

    if pilihan == 1:
        hasil = plus(no1, no2)
        operasi = '+'
        print(f'{no1} {operasi} {no2} = {hasil}')
    elif pilihan == 2:
        hasil = minus(no1, no2)
        operasi = '-'
        print(f'{no1} {operasi} {no2} = {hasil}')
    elif pilihan == 3:
        hasil = multiply(no1, no2)
        operasi = '*'
        print(f'{no1} {operasi} {no2} = {hasil}')
    elif pilihan == 4:
        if no2 == 0:
            print('Pembagian dengan nol tidak diperbolehkan!')
            continue
        hasil = divide(no1, no2)
        operasi = '/'
        print(f'{no1} {operasi} {no2} = {hasil}')