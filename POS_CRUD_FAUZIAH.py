#================================================================================================================================
# daftar dictionary yg akan dipakai

# dictionary bread berisi stock jenis roti beserta nutricition facts dan harga
bread={ #{jenis bread: {stock, fat, protein, dan kalori}} /serving
    "Italian HerbsCheese":{"stock": 1, "fat": 12.09, "protein":9.53, "calories": 271, "harga": 15000}, 
    "Italian Bread":{"stock": 1,"fat": 3.5, "protein":8.8, "calories": 271,"harga": 15000}, 
    "Whole Wheat Tortilla":{"stock": 100,"fat": 0.91, "protein":6.73, "calories": 184, "harga": 17000}, 
    "Flat White Bread":{"stock": 100, "fat":3.29, "protein":7.64, "calories": 266, "harga": 10000}}

# dictionary protein berisi stock jenis protein beserta nutricition facts dan harga
protein={ #{jenis protein: {stock, fat, protein, dan kalori}} /serving
    "Smoked Beef Salami":{"stock": 100,"fat": 5.11, "protein":2.9, "calories": 59, "harga": 12000 }, 
    "Pepperoni":{"stock": 100,"fat": 11.28, "protein":5.7, "calories": 130, "harga": 10000}, 
    "Chicken Strips":{"stock": 100, "fat":5.5, "protein":6.6, "calories": 105, "harga": 15000}, 
    "Beef Brisket":{"stock": 100, "fat":22.23, "protein":21.11, "calories": 291, "harga": 20000}}

# dictionary cheese berisi stock jenis keju beserta nutricition facts dan harga
cheese={ #{jenis cheese: {stock, fat, protein, dan kalori}} /serving
    "Cream Cheese":{"stock": 100, "fat":5.06, "protein":1.09, "calories": 51, "harga": 3000 }, 
    "Mozarella":{"stock": 100, "fat":5.61, "protein":7.27, "calories": 85, "harga": 7000}, 
    "Cheddar Cheese":{"stock": 100, "fat":9.28, "protein":6.97, "calories": 113, "harga": 5000}}

# dictionary sauce dressing berisi stock jenis beserta nutricition facts dan harga
sauce={ #{jenis sauce: {stock, fat, protein, dan kalori}} /serving
    "Mayo": {"stock": 100, "fat":4.91, "protein":0.13, "calories": 57, "harga": 2000 },
    "Thousand Island": {"stock": 100, "fat":5.47, "protein":0.17, "calories": 58, "harga": 3000 },
    "Italian Dressing": {"stock": 100,"fat":4.26, "protein":0.06, "calories": 44, "harga": 3000 }, 
    "Sesame oil": {"stock": 100, "fat": 4.5, "protein":0, "calories": 40, "harga": 4000 }, 
    "Roasted Sesame": {"stock": 100, "fat":9, "protein":1, "calories": 100, "harga": 4000 }}

# dictionary protein berisi stock jenis sayuran beserta nutricition facts dan harga
veggie={ #{jenis veggie: {stock, fat, protein, dan kalori}} /serving
    "Lettuce": {"stock": 100, "fat":0.08, "protein":0.5, "calories": 8, "harga": 2000 }, 
    "Tomatoes": {"stock": 100, "fat":0.06, "protein":0.27, "calories": 6, "harga": 1000 }, 
    "Cucumber": {"stock": 100, "fat":0.08, "protein":0.3, "calories": 6, "harga": 2000 }, 
    "Onion": {"stock": 100, "fat":0.09, "protein":1.06, "calories": 48, "harga": 3000 }, 
    "Green Olives": {"stock": 100, "fat":4.44, "protein":0.3, "calories": 42, "harga": 5000 }}

# dictionary drink berisi stock jenis minuman beserta nutricition facts dan harga
drink={ #{jenis drink: {stock, fat, protein, dan kalori}} /serving
    "Mineral Water": {"stock": 100, "fat":0, "protein":0, "calories": 0, "harga": 7000}, 
    "Diet Coke": {"stock": 100, "fat":0, "protein": 0, "calories": 0, "harga": 10000}}


#================================================================================================================================
# merupakan dictionary yg beriisi semua dictionary bahan baku
inventory_all={} #inisiasi dict kosong
inventory_all.update(bread) #menggabungkan semua dict ke dalam dict inventory_all
inventory_all.update(protein)
inventory_all.update(cheese)
inventory_all.update(sauce)
inventory_all.update(veggie)
inventory_all.update(drink)

#================================================================================================================================
# display_inventory -> 
# fungsi ini untuk menampilkan tabel inventory
def display_inventory (pilih_dict,teks): 
    #pilih_dict= isi dictionary sesuai yang dipilih, teks=nama dictionary yg dipilih(dalam string)
    print()
    print(f"DAFTAR INVENTORY {teks.upper()}")
    print(f'Index\t||Cal\t||Fat\t||Prot\t||Stock\t||Harga\t||{teks.title()}')
    print("============================================================================")
    for index_, (jenis, nutri_inv) in enumerate(pilih_dict.items()):  
        print(f'{index_+1}\t||{nutri_inv["calories"]}\t||{nutri_inv["fat"]}\t||{nutri_inv["protein"]}\t||{nutri_inv["stock"]}\t||{nutri_inv["harga"]}\t||{jenis} ')
    print("============================================================================")
    print()

#================================================================================================================================
# lanjut -> 
# fungsi ini untuk mengkonfirmasi user apakah akan melanjutkan akses pada menu yg sedang berjalan atau kembali ke main menu
def lanjut(menu):
    global posisi
    # menu = nama menu yg sedang berjalan, sehingga bisa dipanggil sebagai variabel dinamis
    lanjut_menu_ini= str(input(f"Apakah Anda mau mengakses menu {menu} kembali (ketik Y jika ya)? ")).lower()
    print("============================================================================")
    if lanjut_menu_ini!='y': 
        lanjut_main_menu=str(input('Apakah Anda mau kembali ke main menu (ketik Y jika ya)? ')).lower()
        print("============================================================================")
        if lanjut_main_menu!='y':
            exit_program()
        elif lanjut_main_menu=='y':
            main_menu(posisi)

#================================================================================================================================
# create_program ->
# fungsi ini untuk menambah inventory sesuai dengan yang diinginkan user
# dengan catatan: primary key yg ingin ditambahkan, tidak boleh existing
# primary key= nama item
def create_program():
    global posisi
    while True:
        print('''============================================================================
Menambah Inventory Gudang:
1. Menambah Inventory Bread
2. Menambah Inventory Protein
3. Menambah Inventory Cheese
4. Menambah Inventory Sauce
5. Menambah Inventory Veggie
6. Menambah Inventory Drink
7. Kembali ke Main Menu
============================================================================''')
        
        opsi_menu_create=(input("Masukkan Menu Pilihan Anda (angka): "))
        if opsi_menu_create.isdigit():
            opsi_menu_create=int(opsi_menu_create)
            print("============================================================================")
            if opsi_menu_create>=1 and opsi_menu_create<=6:
                opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                    1: (bread, 'Roti'),
                    2: (protein, 'Protein'),
                    3: (cheese, 'Keju'),
                    4: (sauce, 'Saus'),
                    5: (veggie, 'Sayur'),
                    6: (drink, 'Minuman')}
                
                pilih_dict=opsi_opsi[opsi_menu_create][0] #mau mengambil dict dalam tuple sesuai inputan user
                teks=opsi_opsi[opsi_menu_create][1] #untuk mengambil string dict dalam tuple

                display_inventory (pilih_dict,teks)

                
                print(f"Masukkan nama {teks.lower()} yang ingin ditambahkan.")
                print("============================================================================")
                tambah_item = str(input("Nama bahan baku tidak boleh sama dengan yang sudah ada: ")).title()
                print("============================================================================")
                    
                if tambah_item in pilih_dict:
                    print(f'{tambah_item} sudah ada didalam inventory.')
                    print("============================================================================")
                              
                else:
                    try:
                        tambah_stock=int(input("Masukkan stock item: "))
                        tambah_harga= int(input('Masukkan harga item: '))
                        tambah_fat=float(input ('Masukan info nutrition (fat) item: '))
                        tambah_prot=float(input ('Masukan info nutrition (protein) item: '))
                        tambah_kal=float(input ('Masukan info nutrition (kalori) item: '))
                        print("============================================================================")
                                        
                        if int(tambah_stock)>=0 and int(tambah_harga)>=0 and float(tambah_fat)>=0 and float(tambah_prot)>=0 and float(tambah_kal)>=0:
                            pilih_dict[tambah_item.title()]={ 
                                "stock": (tambah_stock),
                                "harga": (tambah_harga),
                                "fat": tambah_fat,
                                "protein": tambah_prot,
                                "calories": (tambah_kal)}
                                
                            display_inventory (pilih_dict,teks)
                            
                        else: 
                            print(f'{tambah_item.title()} gagal ditambahkan')
                            print('Info stock dan harga harus berupa bilangan bulat lebih dari 0')
                            print('Kandungan nilai fat, protein, dan kalori harus lebih dari nol')
                            print("============================================================================")
                             
                    except:
                        print(f'{tambah_item.title()} gagal ditambahkan')
                        print('Info stock dan harga harus berupa angka bilangan bulat lebih dari 0')
                        print('Kandungan nilai fat, protein, dan kalori harus berupa angka lebih dari nol')
                        print("============================================================================")

            elif opsi_menu_create==7:
                main_menu(posisi)
            
            else:
                print("Angka yang Anda Masukkan Tidak Valid!")
                print("============================================================================")

            lanjut('menambah inventory')                                
        else:
            print("Inputan Anda tidak valid!")
            print("============================================================================")
            lanjut('menambah inventory')   

#================================================================================================================================
#read_program
def read_program():
    global posisi
    while True:
        print("============================================================================")
        print('''Menampilkan Inventory Gudang:
1. Menampilkan Inventory Bread
2. Menampilkan Inventory Protein
3. Menampilkan Inventory Cheese
4. Menampilkan Inventory Sauce
5. Menampilkan Inventory Veggie
6. Menampilkan Inventory Drink
7. Menampilkan Seluruh Inventory
8. Menampilkan Inventory Dengan Stock Minimal 
9. Kembali ke Main Menu''')
        print("============================================================================")
        print()
        opsi_menu_read=(input("Masukkan Menu Pilihan Anda (angka): "))
        print()
        if opsi_menu_read.isdigit():
            opsi_menu_read=int(opsi_menu_read)
            if opsi_menu_read>=1 and opsi_menu_read<=7:
                opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                    1: (bread, 'Roti'),
                    2: (protein, 'Protein'),
                    3: (cheese, 'Keju'),
                    4: (sauce, 'Saus'),
                    5: (veggie, 'Sayur'),
                    6: (drink, 'Minuman'),
                    7: (inventory_all, "Semua Bahan Baku")}

                pilih_dict=opsi_opsi[opsi_menu_read][0] #mau mengambil nama dict dalam tuple
                teks=opsi_opsi[opsi_menu_read][1] #untuk mengambil string dict dalam tuple

                display_inventory (pilih_dict,teks)
                lanjut('menampilkan inventory')           
            
            elif opsi_menu_read==8:
                
                minimal_stock = input('Masukkan angka stok yang menjadi batas minimal stock inventory : ')
                if minimal_stock.isdigit(): #memastikan inputan angka
                    minimal_stock=int(minimal_stock) #jika inputan berupa angka, maka di casting menjadi int
                    if minimal_stock>=0:
                        print("============================================================================")
                        print(f"DAFTAR INVENTORY DENGAN STOCK KURANG DARI", minimal_stock)
                        print(f'||Cal\t||Fat\t||Prot\t||Stock\t||Harga\t||Bahan Baku')
                        print("============================================================================")
                        for index_, (jenis, nutri_inv) in enumerate(inventory_all.items()):
                            if int(nutri_inv['stock'])<= int(minimal_stock):
                                print(f'||{nutri_inv["calories"]}\t||{nutri_inv["fat"]}\t||{nutri_inv["protein"]}\t||{nutri_inv["stock"]}\t||{nutri_inv["harga"]}\t||{jenis} ')
                        print("============================================================================")
                        print()    
                        print("============================================================================")
                        print(f"DAFTAR INVENTORY DENGAN STOCK LEBIH DARI", minimal_stock)
                        print(f'||Cal\t||Fat\t||Prot\t||Stock\t||Harga\t||Bahan Baku')
                        print("============================================================================")
                        for index_, (jenis, nutri_inv) in enumerate(inventory_all.items()):
                            if int(nutri_inv['stock'])> int(minimal_stock):
                                print(f'||{nutri_inv["calories"]}\t||{nutri_inv["fat"]}\t||{nutri_inv["protein"]}\t||{nutri_inv["stock"]}\t||{nutri_inv["harga"]}\t||{jenis} ')
                            print("============================================================================")
                            print()
                            lanjut('menampilkan inventory')
                        else:
                            print("Angka yang Anda Masukkan Tidak Valid!")
                            print("============================================================================")
                            lanjut('menampilkan inventory')
                                                                              
                else:
                    print("Inputan Anda tidak valid!") #jika inputan tidak berupa angka, keluar warning
                    print("============================================================================")
                    lanjut('menampilkan inventory')
    
            elif opsi_menu_read==9:
                main_menu(posisi)
            
            else:
                print("Angka yang Anda Masukkan Tidak Valid!")
                print("============================================================================")
        
        else:
            print("Inputan Anda tidak valid!")
            print("============================================================================")
            lanjut('menampilkan inventory')

#================================================================================================================================
# UPDATE_pROGRAM
def update_program ():
    global posisi
    while True:
        print("============================================================================")
        print('''Mengupdate Inventory Gudang:
1. Mengupdate Inventory Bread
2. Mengupdate Inventory Protein
3. Mengupdate Inventory Cheese
4. Mengupdate Inventory Sauce
5. Mengupdate Inventory Veggie
6. Mengupdate Inventory Drink
7. Kembali ke main menu''')
        
        print("============================================================================")
        opsi_menu_update=input("Masukkan Menu Pilihan Anda (angka): ")
        if opsi_menu_update.isdigit():
            opsi_menu_update=int(opsi_menu_update)
            print("============================================================================")
            if opsi_menu_update>=1 and opsi_menu_update<=6:
                opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                    1: (bread, 'Bread'),
                    2: (protein, 'Protein'),
                    3: (cheese, 'Keju'),
                    4: (sauce, 'Saus'),
                    5: (veggie, 'Sayur'),
                    6: (drink, 'Minuman')}
                    
                pilih_dict=opsi_opsi[opsi_menu_update][0] #mau mengambil nama dict dalam tuple
                teks=opsi_opsi[opsi_menu_update][1] #untuk mengambil string dict dalam tuple

                display_inventory (pilih_dict,teks)
                    
                print('''Pilihan Update 
1. Update Stock
2. Update Harga''')
                print("============================================================================")
                try:
                    opsi_update=int(input("Masukkan menu update Anda (angka): "))
                    print("============================================================================")

                    if opsi_update==1 or opsi_update==2:
                        if opsi_update==1:
                            update_valuesnya="stock"
                        elif opsi_update==2:
                            update_valuesnya="harga"

                        try:
                            index_update= int(input('Masukkan index inventory yang Akan Anda Update: '))
                            print("============================================================================")
                            if index_update>=1 and index_update<=len(pilih_dict):
                                update_key = (list(pilih_dict.keys()))[index_update-1]
                                info_update = int(input(f"Masukkan {update_valuesnya} {update_key} yang Akan Anda Update: "))
                                print("============================================================================")
                                if info_update>=0:
                                    pilih_dict[update_key][update_valuesnya]=info_update
                                    print(f'{update_valuesnya.capitalize()} untuk {update_key} berhasil di update menjadi {info_update}')
                                    print("============================================================================")
                                    display_inventory (pilih_dict,teks)
                                else:
                                    print('Gagal mengupdate data!')
                                    print(f'{update_valuesnya.capitalize()} update tidak boleh kurang dari nol')
                                    print("============================================================================")                           
                            else:
                                print("Angka yang Anda Masukkan Tidak Valid!")
                                print("============================================================================")

                        except:
                            print("Inputan Anda Tidak Valid!")
                            print("Inputan harus berupa bilangan bulat positif!")
                            print("============================================================================")
                        # display_inventory (pilih_dict,teks)

                    elif opsi_update!=1 or opsi_update!=2:
                        print("Angka yang Anda Masukkan Tidak Valid!")
                        print("============================================================================")

                except:
                    print("Inputan Anda Tidak Valid!")
                    print("Inputan harus berupa bilangan bulat positif!")
                    print("============================================================================")
                    # lanjut('mengupdate invetory')

            elif opsi_menu_update==7:
                main_menu(posisi)
            
            else:
                print("Angka yang Anda Masukkan Tidak Valid!")
                print("============================================================================")
            
            lanjut('mengupdate invetory') 
        else:
            print("Inputan Anda Tidak Valid!")
            print("Inputan harus berupa bilangan bulat positif!")
            print("============================================================================")
            lanjut('mengupdate invetory')

#================================================================================================================================
#delete_program
def delete_program():
    while True:

        print("============================================================================")
        print('''Menghapus Inventory Gudang:
1. Menghapus Inventory Bread
2. Menghapus Inventory Protein
3. Menghapus Inventory Cheese
4. Menghapus Inventory Sauce
5. Menghapus Inventory Veggie
6. Menghapus Inventory Drink
7. Menghapus Seluruh Inventory 
8. Kembali ke main menu''')
        print("============================================================================")
        opsi_menu_delete=input("Masukkan Menu Pilihan Anda (angka): ")
        print("============================================================================")
        if opsi_menu_delete.isdigit():
            opsi_menu_delete=int(opsi_menu_delete)
            if opsi_menu_delete>=1 and opsi_menu_delete<=6:
                opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                    1: (bread, 'Roti'),
                    2: (protein, 'Protein'),
                    3: (cheese, 'Keju'),
                    4: (sauce, 'Saus'),
                    5: (veggie, 'Sayur'),
                    6: (drink, 'Minuman')}
                
                pilih_dict=opsi_opsi[opsi_menu_delete][0] #mau mengambil nama dict dalam tuple
                teks=opsi_opsi[opsi_menu_delete][1] #untuk mengambil string dict dalam tuple

                display_inventory (pilih_dict,teks)
                
                key_pilih_dict= list(pilih_dict.keys()) #memanggil list dari nama2 bahan baku
                # print(len(key_pilih_dict))
                try:
                    index_hapus=int(input('Masukkan index inventory yang Akan Anda Hapus: '))-1
                    print("============================================================================")
                 
                    if index_hapus>=0 and index_hapus<len(key_pilih_dict):
                        opsi_delete = str((input(f"Anda yakin akan menghapus {key_pilih_dict[index_hapus]}? (Y/N)?"))).lower()
                        if opsi_delete== "y":
                            del pilih_dict[key_pilih_dict[index_hapus]]
                            print(f'Inventory {key_pilih_dict[index_hapus]} telah di hapus')
                            print("============================================================================")
                    else:
                        print("Angka (index) yang Anda Masukkan Tidak Valid!")
                        print("============================================================================")
                except:
                    print("Inputan Anda Masukkan Tidak Valid!")
                    print("============================================================================")

            elif opsi_menu_delete==7:
                display_inventory (inventory_all,"Bahan Baku")
                print("============================================================================")
                opsi_delete = str((input(f"Anda yakin akan menghapus (Y/N)?"))).lower()
                print("============================================================================")
                if opsi_delete!= "y":
                    print(f'Batal Menghapus Seluruh Inventory')
                    print("============================================================================")
            
                else:
                    bread.clear()
                    protein.clear()
                    cheese.clear()
                    sauce.clear()
                    veggie.clear()
                    drink.clear()
                    inventory_all.clear()
                      
                    print(f'Seluruh Inventory Telah di Hapus')
                    print("============================================================================")

            elif opsi_menu_delete==8:
                main_menu(posisi)
            else:
                print("Angka yang Anda Masukkan Tidak Valid!")
                print("============================================================================")
            
            
            lanjut("menghapus inventory")
        else:
            print("Inputan Anda Masukkan Tidak Valid!")
            print("============================================================================")
            lanjut("menghapus inventory")

#================================================================================================================================
# transaksi_program
def transaksi_makanminum (makan_minum):
    global keranjang
    global no_urut
    global total_keseluruhan
    global opsi_opsi

    while True:
        menu_pesanan=[]
        sum_fat_menu = 0
        sum_prot_menu = 0
        sum_cal_menu = 0
        sum_harga_menu = 0

        for i in range(1,len(opsi_opsi)+1):

            dictionary_=opsi_opsi[i][0] #mau mengambil nama dict dalam tuple
            teks=opsi_opsi[i][1] #untuk mengambil string dict dalam tuple            

            display_inventory (dictionary_,teks)
                
            validasi_index_input=False
            while validasi_index_input==False:  
                #KASIH TRY except
                print('Pisahkan dengan koma jika lebih dari 1 pilihan. Contoh:(1,2)')
                print('Input angka (index) berlaku kelipatan, (contoh:2,2,2 untuk pemesana 3 item yg sama) ')
                print('Input angka nol (0), untuk melewatkan item) ')
                index_input_pilihan = (input(f"Pilih index yang diinginkan (ANGKA): "))
                print("============================================================================")
                
                input_pilihan_split = index_input_pilihan.split(',')  # hasil inputan dijadikan list:nya ['1','2','3']
                            
                for r in input_pilihan_split:
                    # print ('r adalah ',r) # r adalah 1,r adalah 2, r adalah 3
                    if int(r)>len(dictionary_) or int(r)<0: #cek apakah index yg diinput tidak lebih dari len(dict)
                        
                        print("Angka (index) yang Anda Masukkan Tidak Valid!")
                        validasi_index_input=False
                        print("Silahkan input kembali!")
                        print("============================================================================")
                        # lanjut_transaksi=(input('Apakah Anda mau input ulang index yg diinginkan (Y/N)? ')).lower()
                        # print("============================================================================")
                        # if lanjut_transaksi!='y':
                        #     break
                        #     # lanjut('transaksi')
                        #     # print('Terimakasih')
    
                    else:
                        validasi_index_input=True

                if validasi_index_input==False:
                    continue                   

                # CEK_STOK UNTUK INPUTAN YG DI INPUT
                if validasi_index_input==True:
                    count_char ={}
                    for index_input in input_pilihan_split: #kalkulasi yg index dan brp jumlahnya (mau dipesan)
                        # print("index_input :", index_input) #1 //2//3
                        if index_input in count_char:
                            count_char[index_input] +=1 #kalo sudah ada, dijumlahkan
                        else:
                            count_char[index_input] = 1

                    # print('count_char :',count_char) #{'1':1,'2':1,'3':1}

                    #kalau sudah di rekap di count_char, kita abandingkan dengan stok pada dict dictionary_
                    item_jumlah_pembelian_char=[] #isinya teks buat rekapan []

                    for x, (y,z) in enumerate(dictionary_.items()): #slicing keys&value di dict dalam dict (dict dictionary_)
                        for keys, value in count_char.items(): #slicing key&value di dic count_char
                            if int(x)==int(keys)-1: #ketika index dictionary_=index keys-1 count_char, cek stok
                                if int(value)>int(z["stock"]): #klo stok pesanan di count_char > stok di dictionary_ maka stok tdk cukup
                                    print(f'Mohon maaf stock {y} tidak cukup')
                                                                       
                                    validasi_index_input=False
                                    menu_pesanan=[]
                                    print("Silahkan input kembali!")
                                    print("============================================================================")
                        
                                else: #stock aman
                                    teks= str(value) + ' ' + str(y)
                                    # print('teks :', teks)
                                    item_jumlah_pembelian_char.append(teks) #masukin teksnya 
                                    # print('item_jumlah_pembelian_char', item_jumlah_pembelian_char)
                                    menu_pesanan.append(item_jumlah_pembelian_char)

                if validasi_index_input==False:
                    continue  

                if validasi_index_input==True:
                    for index_bekurang, stock_berkurang in count_char.items():
                        for index_dict, (item_dict, stock) in enumerate(dictionary_.items()):
                            if (int(index_bekurang)-1)==(index_dict):
                                # print('index sama')
                                dictionary_[item_dict]['stock']=stock['stock']-stock_berkurang
                                sum_fat_menu= sum_fat_menu+(float(stock_berkurang))*float(dictionary_[item_dict]['fat'])
                                # print(sum_fat_menu)
                                sum_prot_menu= sum_prot_menu+(float(stock_berkurang))*float(dictionary_[item_dict]['protein'])
                                # print(sum_prot_menu)
                                sum_cal_menu= sum_cal_menu+(float(stock_berkurang))*float(dictionary_[item_dict]['calories'])
                                # print(sum_cal_menu)
                                sum_harga_menu= sum_harga_menu+(stock_berkurang*dictionary_[item_dict]['harga'])
                                # print(sum_harga_menu)

        teks_rekapan_menu=''
        for item in menu_pesanan:
            teks_rekapan_menu +=item[0]+' '
        
        nutrisi_rekap_menu=(f'Fat :{sum_fat_menu:.2f}, Prot:{sum_prot_menu:.2f}, Cal:{sum_cal_menu:.2f}, Harga Item:{sum_harga_menu}')

        print(teks_rekapan_menu[:-1])
        print(nutrisi_rekap_menu)
        print('berhasil ditambahkan ke chart.')
        print("============================================================================")

        item_belanja={teks_rekapan_menu[:-1]:nutrisi_rekap_menu}        
        keranjang.append(item_belanja)
        
        # no_urut+=1
        total_keseluruhan=total_keseluruhan+sum_harga_menu

        lanjut_belanja=input(f'Apakah Anda mau melanjutkan berbelanja {makan_minum} (Y/N)? ').lower()
        print("============================================================================")
        if lanjut_belanja!='y':
            break

# total_keseluruhan = 0 #untuk menyimpan total harga pada seluruh pembelian menu custom
# keranjang = []
#================================================================================================================================
# transaksi_program
def transaksi():
    global keranjang
    global no_urut
    global total_keseluruhan
    global opsi_opsi
    
    if inventory_all!={}:
        while True:
            keranjang = []
            total_keseluruhan = 0
            print("============================================================================")
            print("==========================TRANSKASI PENJUALAN===============================")
            print("============================================================================")
            
            opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                1: (bread, 'Roti'),
                2: (protein, 'Protein'),
                3: (cheese, 'Keju'),
                4: (sauce, 'Saus'),
                5: (veggie, 'Sayur')}

            transaksi_makanminum('makanan')

            pesan_minum=input('Apakah Anda mau memesan minum (Y/N? ')
            print("============================================================================")
            if pesan_minum =='y':
                opsi_opsi={ #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
                    1: (drink, 'Minuman')}

                transaksi_makanminum('minuman')

            print("KERANJANG BELANJA ANDA")
            print("============================================================================")               
            no_urut = 1 #assign untuk urutan di rakapan belanja
            for dict_dalam_keranjang in keranjang:
                for key_keranjang, value_keranjang in dict_dalam_keranjang.items():
                    print(no_urut,'. ',key_keranjang)
                    print('    ',value_keranjang)
                    print()
                    no_urut+=1

            print("============================================================================")
            print('TOTAL BELANJA        :',total_keseluruhan)               
            while True:
                uang_pembayaran = int(input('PEMBAYARAN TUNAI     : '))
                print("============================================================================")
                if uang_pembayaran>total_keseluruhan and uang_pembayaran>0:
                    uang_kembali= uang_pembayaran-total_keseluruhan
                    print('KEMBALI              :',uang_kembali)       
                    print("============================================================================")
                    print('PEMBAYARAN BERHASIL, TERIMAKASIH TELAH BERBELANJA')
                    print('-----KEDATANGAN ANDA SELALU KAMI TUNGGU :)-------')
                    break
                elif uang_pembayaran<total_keseluruhan or uang_pembayaran<0:
                    print('UANG ANDA KURANG.')
                    print('PASTIKAN UANG PEMBAYARAN MINIMAL:', total_keseluruhan)
                    print()
                break       
            
            lanjut('transaksi')
    else:
        print(' Transaksi tidak bisa dilakukan, karena Inventory Anda Kosong.')
        print('Silahkan kembali ke main menu')
        main_menu(posisi)  

#================================================================================================================================
# exit_program
def exit_program():
    print("================================================================================")
    print("Anda telah keluar dari aplikasi Point of Sales ini. Terimakasih dan Sampai Jumpa")
    print("================================================================================")
    quit()

#=========================================================================================================================

# main_menu
def main_menu(posisi):
    while True:
        if posisi == 'owner':
            print('''============================================================================
Menu Utama Owner:
1. Menampilkan Inventory Bahan Baku
2. Menambah Inventory Bahan Baku
3. Menghapus Inventory Bahan Baku
4. Update Inventory Bahan Baku
5. Transaksi 
6. Log in dengan posisi lain
7. Keluar Program
============================================================================''')
            opsi_main_menu = (input('Masukkan Menu Pilihan Anda (angka): '))
            print("============================================================================")
            if opsi_main_menu.isdigit():
                opsi_main_menu=int(opsi_main_menu)
                if opsi_main_menu==1: #1. Menampilkan Inventory Bahan Baku
                    read_program()
                elif opsi_main_menu==2: #2. Menambah Inventory Bahan Baku
                    create_program()
                elif opsi_main_menu==3: #3. Menghapus Inventory Bahan Baku
                    delete_program()
                elif opsi_main_menu==4: #4. Update Inventory Bahan Baku
                    update_program()
                elif opsi_main_menu==5: #5. Transaksi 
                    transaksi()
                elif opsi_main_menu==7: #7. Keluar Program
                    print('Anda keluar dari main menu Owner')
                    print("============================================================================")
                    lanjut_ke_main_menu=input('Apakah Anda mau login kembali (Y/N)? ').lower()
                    print("============================================================================")
                    if lanjut_ke_main_menu!='y':
                        exit_program()
                    else:
                        posisi_jabatan()
                elif opsi_main_menu==6:
                    posisi_jabatan()
                else:
                    print('Angka yang Anda Masukkan Tidak Valid!')
                    lanjut_menu_profesi=input('Apakah Anda mau input ulang index yg diinginkan (Y/N)? ').lower()
                    print("============================================================================")
                    if lanjut_menu_profesi!='y':
                        if lanjut_menu_profesi!='y':
                            exit_program()
                        else:
                            main_menu(posisi) 
            else:
                print('Angka yang Anda Masukkan Tidak Valid!')
                lanjut_menu_profesi=input('Apakah Anda mau input ulang index yg diinginkan (Y/N)? ').lower()
                print("============================================================================")
                if lanjut_menu_profesi!='y':
                    if lanjut_menu_profesi!='y':
                        exit_program()
                    else:
                        main_menu(posisi) 
            
        elif posisi=='kasir':
            print()
            print('''============================================================================
Menu Utama Kasir:
1. Transaksi 
2. Log in dengan posisi lain
3. Keluar Program
============================================================================''')      
            opsi_main_menu = (input('Masukkan Menu Pilihan Anda (angka): '))
            print("============================================================================")
            if opsi_main_menu.isdigit():
                opsi_main_menu=int(opsi_main_menu)
                if opsi_main_menu==1: #1. Transaksi 
                    transaksi()
                elif opsi_main_menu==3: #2. Keluar Program
                    print('Anda keluar dari main menu Kasir')
                    print("============================================================================")
            
                    lanjut_ke_main_menu=input('Apakah Anda mau login kembali (Y/N)? ').lower()
                    print("============================================================================")
                    if lanjut_ke_main_menu!='y':
                        exit_program()
                    else:
                        posisi_jabatan()

                elif opsi_main_menu==2:
                    posisi_jabatan()
                else:
                    print('Angka yang Anda Masukkan Tidak Valid!')
                    lanjut_menu_profesi=input('Apakah Anda mau input ulang index yg diinginkan (Y/N)? ').lower()
                    print("============================================================================")
                    if lanjut_menu_profesi!='y':
                        if lanjut_menu_profesi!='y':
                            exit_program()
                        else:
                            main_menu(posisi) 

            else:
                print('Angka yang Anda Masukkan Tidak Valid!')
                lanjut_menu_profesi=input('Apakah Anda mau input ulang index yg diinginkan (Y/N)? ').lower()
                print("============================================================================")
                if lanjut_menu_profesi!='y':
                    if lanjut_menu_profesi!='y':
                        exit_program()
                    else:
                        main_menu(posisi) 
                             
# main_menu
def posisi_jabatan():
    global posisi
    print()
    print(""""============================================================================
Selamat Datang di Aplikasi Point of Sales
============================================================================""")
    while True:
        print()
        # constraint:: insiasi posisi HANYA untuk 'owner' dan 'kasir' 
        posisi= input('Silahkan masukkan profesi Anda: ').lower()
        print("============================================================================")
        
        if posisi=='owner' or posisi=='kasir':
            main_menu(posisi)
                         
        else :
            print('Posisi yang Anda Masukkan Salah!')
            print("============================================================================")      
            lanjut=input('Apakah Anda mau login kembali(Y/N)? ').lower()
            print("============================================================================")
            if lanjut!='y':
                exit_program()
            else:
                posisi_jabatan()           
#================================================================================================================================
posisi_jabatan()
