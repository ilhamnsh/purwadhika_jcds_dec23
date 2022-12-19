#key utama : ikanlele
#value utama : nama barang:ikan lele dll
#subkey : nama barang
#sub value : ikan lele
#Daftar Stok Gudang Awal
daftar_stok = {
    "ikanlele":{"Nama Barang":"Ikan Lele","Kategori":"Ikan","Satuan":"Kg","Stok":"10","Harga beli/satuan":13000,"Harga jual/satuan":20000},
    "ikannila":{"Nama Barang":"Ikan Nila","Kategori":"Ikan","Satuan":"Kg","Stok":"20","Harga beli/satuan":17000,"Harga jual/satuan":25000},
    "wortel":{"Nama Barang":"Wortel","Kategori":"Sayur","Satuan":"gr","Stok":"30","Harga beli/satuan":2000,"Harga jual/satuan":3500},
    "kentang":{"Nama Barang":"Kentang","Kategori":"Sayur","Satuan":"gr","Stok":"25","Harga beli/satuan":3000,"Harga jual/satuan":5000},
    "kemiri":{"Nama Barang":"Kemiri","Kategori":"Sayur","Satuan":"gr","Stok":"10","Harga beli/satuan":15000,"Harga jual/satuan":3000},
    "udang":{"Nama Barang":"Udang","Kategori":"Ikan","Satuan":"Kg","Stok":"23","Harga beli/satuan":45000,"Harga jual/satuan":60000},
    "ayam":{"Nama Barang":"Ayam","Kategori":"Daging","Satuan":"Kg","Stok":"14","Harga beli/satuan":22000,"Harga jual/satuan":28000},
    "sapi":{"Nama Barang":"Sapi","Kategori":"Daging","Satuan":"Kg","Stok":"15","Harga beli/satuan":30000,"Harga jual/satuan":35000},
    }

password = 'PPIC01!'
log_in = ''
trial = 1
limit = 4
#Operasi log in password
print("------------------------------------------\nSelamat Datang Di Gudang Agroindustri JCDS\n------------------------------------------\n")
while log_in!= password and trial <= limit:
    if trial <= limit:
        log_in = input("Masukkan pasword anda: ")
        if log_in != password and trial < limit:
            print(f'Password salah. Sisa kesempatan login {limit-trial} kali')
            trial = trial + 1
        elif log_in != password and trial == limit:
            print("Maaf, anda melebihi limit login. Silahkan coba beberapa saat lagi")
            trial = trial + 1
            quit()
        else:
            print("Password benar. Silahkan masuk.\n")

#Tampil default_stok
def default_stok():
    if len(daftar_stok)==0:
        print("Daftar tidak tersedia")
    else :
        print('='*83)
        print(' ' *23+'DAFTAR STOK BARANG AGROINDUSTRI JCDS')
        print('='*83)
        print("Daftar Barang \n\n\t  |Nama Barang \t| Kategori \t| Satuan   |   Stok   | Harga beli/satuan | Harga jual/satuan")
        for key in daftar_stok.keys():
            print("\t  |{} \t| {}   \t|   {}     |   {}     |\t    {}\t  |\t{}".format(daftar_stok[key]["Nama Barang"],daftar_stok[key]["Kategori"],daftar_stok[key]["Satuan"],daftar_stok[key]["Stok"],daftar_stok[key]["Harga beli/satuan"],daftar_stok[key]['Harga jual/satuan']))

#Tampil list stok
def list_stok():
    while len(daftar_stok)==0:
        print("Tidak ada stok yang tersedia dalam gudang")
        break      
    else:
        while True:
            pilih_tampilan=int(input("--------MENU TAMPILAN STOK-------- \n1. Tampilkan per kategori  \n2. Tampilkan semua \n3. Cari Dengan Keyword \n4. Kembali ke Menu Utama \n\nTampilan Stok Yang Ingin Dipilih (1-4): "))
            if pilih_tampilan==1: 
                pilih_kategori=int(input("-----PILIHAN KATEGORI----- \n1. Daging  \n2. Ikan  \n3. Sayur \n4. Kembali ke Menu Utama \n\nKategori Yang Ingin Ditampilkan (1-4): "))
                if pilih_kategori==1:
                    print("Daftar Barang \n\n\t  |Nama Barang \t| Kategori \t| Satuan   |   Stok   | Harga beli/satuan | Harga jual/satuan")
                    for key in daftar_stok.keys():
                        if daftar_stok[key]["Kategori"]=="Daging":
                            print("\t  |{} \t| {}   \t|   {}     |   {}     |\t    {}\t  |\t{}".format(daftar_stok[key]["Nama Barang"],daftar_stok[key]["Kategori"],daftar_stok[key]["Satuan"],daftar_stok[key]["Stok"],daftar_stok[key]["Harga beli/satuan"],daftar_stok[key]['Harga jual/satuan']))
                        else:
                            continue

                elif pilih_kategori==2:
                    print("Daftar Barang \n\n\t  |Nama Barang \t| Kategori \t| Satuan   |   Stok   | Harga beli/satuan | Harga jual/satuan")
                    for key in daftar_stok.keys():
                        if daftar_stok[key]["Kategori"]=="Ikan":
                            print("\t  |{} \t| {}   \t|   {}     |   {}     |\t    {}\t  |\t{}".format(daftar_stok[key]["Nama Barang"],daftar_stok[key]["Kategori"],daftar_stok[key]["Satuan"],daftar_stok[key]["Stok"],daftar_stok[key]["Harga beli/satuan"],daftar_stok[key]['Harga jual/satuan']))
                        else:
                            continue

                elif pilih_kategori==3:
                    print("Daftar Barang \n\n\t  |Nama Barang \t| Kategori \t| Satuan   |   Stok   | Harga beli/satuan | Harga jual/satuan")
                    for key in daftar_stok.keys():
                        if daftar_stok[key]["Kategori"]=="Sayur":
                            print("\t  |{} \t| {}   \t|   {}     |   {}     |\t    {}\t  |\t{}".format(daftar_stok[key]["Nama Barang"],daftar_stok[key]["Kategori"],daftar_stok[key]["Satuan"],daftar_stok[key]["Stok"],daftar_stok[key]["Harga beli/satuan"],daftar_stok[key]['Harga jual/satuan']))
                        else:
                            continue
                elif pilih_kategori == 4:
                    break #break ke main menu
                else: #jika selain angka diatas, maka akan muncul tampilan "pilihan menu tidak ada"
                    print("Pilihan menu tidak ada")

            elif pilih_tampilan == 2 :
                default_stok()
            elif pilih_tampilan == 3 :
                cari = input("Cari nama barang : ")
                print("Daftar Barang \n\n\t  |Nama Barang \t| Kategori \t| Satuan   |   Stok   | Harga beli/satuan | Harga jual/satuan")
                for key in daftar_stok.keys():
                    if cari.lower() in daftar_stok[key]["Nama Barang"].lower():
                        print("\t  |{} \t| {}   \t|   {}     |   {}     |\t    {}\t  |\t{}".format(daftar_stok[key]["Nama Barang"],daftar_stok[key]["Kategori"],daftar_stok[key]["Satuan"],daftar_stok[key]["Stok"],daftar_stok[key]["Harga beli/satuan"],daftar_stok[key]['Harga jual/satuan']))
                    else:
                        continue
            elif pilih_tampilan == 4:
                break
            else:
                print("Menu tidak ada")

#Fitur tambah stok
def tambah_stok():
    while True :
        default_stok()
        input_nama=input("Masukkan Nama Barang yang Ingin Ditambahkan: ")
        item_baru=input_nama.replace(" ","")
        if item_baru.lower() not in daftar_stok.keys():
            input_nama_baru = input("Masukkan nama barang : ")
            input_kategori_baru = input("Masukkan jenis kategori : ")
            input_satuan_baru = input("Masukkan satuan dari produk : ")
            input_stok_baru = int(input("Masukkan stok dari produk : "))
            input_hargabeli = int(input("Masukkan harga beli produk/satuan : "))
            input_hargajual = int(input("Masukkan harga jual produk/satuan : "))
            checker1=input(f"Apakah anda yakin ingin menambahkan produk {input_nama_baru}; kategori : {input_kategori_baru}; stok : {input_stok_baru}; harga beli {input_hargabeli}; harga jual {input_hargajual}? (Yes/No): ")
            if checker1 != "Yes".lower():
                print("Data batal ditambahkan")
                break
            else:
                daftar_stok[item_baru.lower()]={"Nama Barang":input_nama_baru.capitalize(),"Kategori":input_kategori_baru.capitalize(),"Satuan":input_satuan_baru.capitalize(),"Stok":input_stok_baru,"Harga beli/satuan":input_hargabeli,"Harga jual/satuan":input_hargajual}
                default_stok()
                break
        else:
            print("Data sudah ada di dalam daftar")
            break

#Fitur hapus stok
def hapus_stok():
    default_stok()
    hapus_stok = input("Masukkan nama produk yang ingin dihapus : ")
    nama_hapus = hapus_stok.replace(" ","")
    while nama_hapus.lower() not in daftar_stok.keys():
        print("Data tidak tersedia")
        break
    else: 
        checker2 = input(f'Apakah anda yakin ingin menghapus seluruh informasi untuk produk {hapus_stok} ini? (Yes/No)')
        while checker2 != "Yes".lower():
            print("Data tidak berhasil dihapus")
            break
        else:
            del daftar_stok[nama_hapus.lower()]
            default_stok()

#Fitur update stok
def update_stok():
    update_stok=int(input("-----UPDATE STOK----- \n1. Update berdasarkan Nama \n2. Kembali ke Menu Utama \n\nUpdate yang Ingin Dipilih (1-2): "))
    if update_stok == 1:
        default_stok()
        update_stok=input("Masukkan nama barang yang ingin di update: ")
        new_update = update_stok.replace(" ","")
        while new_update.lower() in daftar_stok.keys():
            jenis_update = int(input("--------PILIHAN UPDATE-------- \n1. Nama Barang \n2. Kategori \n3. Satuan \n4. Stok \n5. Harga beli/unit \n6. Harga jual/unit\n 7. Kembali ke Menu Utama \nJenis yang ingin diupdate(1-6): "))
            if jenis_update == 1:
                update_name = input("Masukkan nama barang baru : ")
                new_name_update = update_name.replace(" ","")
                while new_name_update.lower() in daftar_stok.keys():
                    print("Nama produk sudah ada. Masukkan nama baru")
                    update_name = input("Masukkan nama barang baru : ")
                    new_name_update = update_name.replace(" ","")
                checker2=input(f'Apakah anda yakin ingin memperbarui nama? (Yes/no)')
                if checker2 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_name_update.lower()]=daftar_stok[new_update.lower()]
                    del daftar_stok[new_update.lower()]
                    daftar_stok[new_name_update.lower()]["Nama Barang"]=update_name.capitalize()
                    default_stok()
                    print("Nama telah diperbaharui")
                    break
            elif jenis_update == 2:
                kategori_baru = input("Masukkan kategori produk baru : ")
                checker3=input(f"Apakah anda yakin ingin memperbarui kategori ? (Yes/No) ")
                if checker3 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_update.lower()]["Kategori"]=kategori_baru.capitalize()
                    default_stok()
                    print("Kategori telah diperbaharui")
                    break
            elif jenis_update == 3:
                satuan_baru = input("Masukkan satuan produk baru : ")
                checker4=input(f"Apakah anda yakin ingin memperbarui kategori? (Yes/No) ")
                if checker4 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_update.lower()]["Satuan"]=satuan_baru.capitalize()
                    default_stok()
                    print("Satuan telah diperbaharui")
                    break
            elif jenis_update == 4:
                stok_baru = input("Masukkan jumlah stok produk baru : ")
                checker5=input(f"Apakah anda yakin ingin memperbarui kategori ? (Yes/No) ")
                if checker5 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_update.lower()]["Stok"]=stok_baru.capitalize()
                    default_stok()
                    print("Stok telah diperbaharui")
                    break
            elif jenis_update == 5:
                hargabeli_baru = input("Masukkan harga beli (satuan) produk baru : ")
                checker6=input(f"Apakah anda yakin ingin memperbarui harga beli? (Yes/No) ")
                if checker6 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_update.lower()]["Harga beli/satuan"]=hargabeli_baru.capitalize()
                    default_stok()
                    print("Harga beli telah diperbaharui")
                    break
            elif jenis_update == 6:
                hargajual_baru = input("Masukkan harga jual (satuan) produk baru : ")
                checker7=input(f"Apakah anda yakin ingin memperbarui harga beli? (Yes/No) ")
                if checker7 != 'Yes'.lower():
                    break
                else:
                    daftar_stok[new_update.lower()]["Harga jual/satuan"]=hargajual_baru.capitalize()
                    default_stok()
                    print("Harga jual telah diperbaharui")
                    break
            else:
                break
        else: 
            print("Item yang anda masukkan tidak ada list. Update tidak bisa dilakukan.")

while True:
    pilih_menu = int(input(''' ------------------------------------------\n Selamat Datang Di Gudang Agroindustri JCDS\n ------------------------------------------
    MAIN MENU:
    1. Melihat daftar stok
    2. Menambah daftar stok
    3. Update daftar stok
    4. Menghapus daftar stok
    0. Keluar program program
    
    Masukkan pilihan menu (0-4): '''))

    if pilih_menu == 1:
        list_stok()
    elif pilih_menu == 2:
        tambah_stok()
    elif pilih_menu == 3:
        update_stok()
    elif pilih_menu == 4:
        hapus_stok()
    elif pilih_menu == 0:
        quit()
    else:
        print('Menu tidak ada')



























