#variable dan tipe data
nama = "Adn" #string
umur = 19 #integer
tinggi = 165.5 #float
is_mahasiswa = True #boolean

#output
print(f'\nHalo, nama saya {nama}. Umur saya {umur} tahun')
print('Tinggi saya ', tinggi, ' cm')

print('\n-----------------------------------------------------\n')

#fungsi input
name = input('Masukkan nama anda : ')
age = int(input('Masukkan umur anda : '))
status = input('Apakah anda mahasiswa? (ya/tidak) : ')

#percabangan1
if status.lower() == 'ya':
    status_mahasiswa = "Mahasiswa Aktif"
elif status.lower() == 'tidak':
    status_mahasiswa = "Bukan Mahasiswa"
else:
    print('input tidak valid')

#output
print(f'Halo, nama saya {name}. Umur saya {age} tahun')
print('Status saya :', status_mahasiswa)

print('\n-----------------------------------------------------\n') 

#perulangan for 
for i in range(1, age+1):
    print(f'Umur saya {i} tahun')


