#header
print('---------------------------')
print('---- Simple To-Do List ----')
print('---------------------------')

#list
task_list = []

#fungsi tambah task
def add_task():
    task = input('\nMasukkan task : ')
    task_list.append(task)
    print('Task berhasil ditambahkan!')

#fungsi tampil task
def show_task():
    if not task_list:
        print('\nTidak ada task')
    else : 
        print('\nDaftar Task : ')
        for i, task in enumerate(task_list, start = 1):
            print(f'{i}. {task}')

#fungsi hapus task
def delete_task():
    show_task()
    try : 
        task_number = int(input('\nMasukkan nomor task yang ingin dihapus : '))
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            print(f'Task "{deleted_task}" berhasil dihapus!')
        else:
            print('Nomor task tidak valid!')
    except ValueError:
        print('Input tidak valid! Harap masukkan nomor task yang benar.')

#menu
while True:
    print('\nMenu : ')
    print('1. Tambah Task')
    print('2. Tampil Tasks')
    print('3. Hapus Task')
    print('4. Exit')

    pilihan = int(input('Pilih menu : '))

    if pilihan == 4:
        print('\nTerima Kasih')
        break
    elif pilihan == 1:
        add_task()
    elif pilihan == 2:
        show_task()
    elif pilihan == 3:
        delete_task()
    else:
        print('Pilihan tidak valid! Harap pilih menu yang benar.')



