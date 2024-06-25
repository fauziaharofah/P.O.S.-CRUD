Point of Sales (P.O.S)
by: Fauziah Arofah 

Point of sales atau yang lebih familiar dengan sebutan aplikasi kasir merupakan aplikasi yang mengintegrasi seluruh kegiatan bisnis dan menghasilkan laporan yang dapat di lihat secara real time, yang akses pada setiap menunya dapat di setting sesuai dengan kebutuhan user.

Pada aplikasi point of sales kali ini, akan dibatasi menunya pada inventory (Create, Read, Update, Delete) dan transaksi penjualan, yang mana user dibatasi oleh posisi 'Owner' atau 'Kasir' saja.

Dalam transaksi penjualan, hanya ada 2 jenis: makanan dan minuman. Terinspirasi dari menu custom sandwich "subway", penjualan makanan pada p.o.s. ini merupakan custom dari inventory bahan baku makanan yang tersedia, sesuai dengan yg diinginkan pembeli (selama persediaan stock inventory bahan baku mencukupi). Sedangkan untuk transaksi minuman, seperti transaksi pada umumnya saja.


Berikut merupakan gambaran singkat mengenai source code python yang dibuat:
--------------------------------------------------------------------------------------------------------------------------
* Kumpulan dictionary inventory bahan baku makanan:
    bread={} , protein={}, cheese={}, sauce={}, veggie={}
    - Dictionary inventory bahan baku makanan nama item, stock, fat, protein, calories, dan harganya 

* Dictionary inventory bahan baku minuman:
    drink={}
    - Dictionary inventory minuman yang berisi nama item, stock, fat, protein, calories, dan harganya 

* inventory_all={} 
    - Merupakan dictionary kosong, yg bisa berisi semua dictionary bahan baku (dengan cara mengupdate isinya dengan inventory bahan baku makanan dan minuman)

--------------------------------------------------------------------------------------------------------------------------
# def posisi_jabatan()
- Fungsi ini meminta user untuk memasukan jabatan user, yang akan disimpan pada variabel posisi.
- Jika posisi yang diinputkan benar, maka akan memanggil fungsi main_menu(posisi), jika tidak sesuai akan dikonfirmasi untuk menginputkan kembali atau exit (memanggil fungsi exit_program()

- Constraint -> jabatan user hanya bisa: 'Owner' atau 'Kasir'.

--------------------------------------------------------------------------------------------------------------------------
# def main_menu(posisi)
- Fungsi main_menu(posisi)-> fungsi ini akan menampilkan menu utama yang dapat diakses berdasarkan jabatan (argumen:'posisi').

- Constraint -> akses hanya untuk posisi 'Owner' dan 'Kasir'.
- Posisi = variabel global yang berisi jabatan user ('Owner' atau 'Kasir')

- Jika posisi='Owner', maka menu yang akan ditampilkan sebagai berikut:
Menu Owner:
1. Menampilkan Inventory Bahan Baku # akan memanggil fungsi read_program()
2. Menambah Inventory Bahan Baku    # akan memanggil fungsi create_program()
3. Menghapus Inventory Bahan Baku   # akan memanggil fungsi delete_program()
4. Update Inventory Bahan Baku      # akan memanggil fungsi update_program()
5. Transaksi                        # akan memanggil fungsi transaksi()
6. Log in dengan posisi lain        # akan memanggil fungsi posisi_jabatan()
7. Keluar Program                   # akan mengkonfirmasi ingin login kembali (memanggil fungsi posisi_jabatan()) atau exit (memanggil fungsi exit_program()

- Jika posisi='Kasir', maka menu yg akan ditampilkan sebagai berikut:
Menu Utama Kasir:
1. Transaksi                        # akan memanggil fungsi transaksi()
2. Log in dengan posisi lain        # akan memanggil fungsi posisi_jabatan()    
3. Keluar Program                   # akan mengkonfirmasi ingin login kembali (memanggil fungsi posisi_jabatan()) atau exit (memanggil fungsi exit_program()

--------------------------------------------------------------------------------------------------------------------------
# def lanjut(menu)
- Fungsi lanjut(menu) -> fungsi ini akan mengkonfirmasi user untuk akses ke menu yg sedang diakses/ ke main_menu/ keluar dari program, sesuai kebutuhan user

- menu = berisi string sesuai dengan menu yg sedang diakses, sebagai konfirmasi keberlanjutan program
- posisi = variabel global yang berkaitan dengan fungsi lainnya berisi info jabatan user ('Owner' atau 'Kasir')

--------------------------------------------------------------------------------------------------------------------------
# def display_inventory (pilih_dict,teks): 
- Fungsi ini akan menampilkan tabel inventory berdasarkan dictionary yg dipilih dan nama dictionary tersebut.  Tabel tersebut berisi informasi calories, fat, protein, stock, harga, dan nama itemnya.

- pilih_dict = variabel dictionary yang ingin di tampilkan
- teks =  variabel nama dictionary dalam bentuk string, yang berguna untuk judul dan header tabel

--------------------------------------------------------------------------------------------------------------------------
# def exit_program()
- Fungsi ini akan mengakhiri program aplikasi Point of Sales, serta mencetak pesan "Anda telah keluar dari aplikasi Point of Sales ini. Terimakasih dan Sampai Jumpa"

--------------------------------------------------------------------------------------------------------------------------
# def read_program():
- Fungsi ini akan menampilkan menu terkait menampilkan inventory bahan baku di gudang.
- Tabel pada menampilkan inventory ini akan menggunakan fungsi display_inventory (pilih_dict,teks).
- Jika terdapat inputan index yang tidak sesuai/ inputan yang tidak valid, maka akan keluar pesan peringatan dan memanggil fungsi lanjut('menampilkan inventory').
- posisi = variabel global yang berkaitan dengan fungsi lainnya berisi info jabatan user ('Owner' atau 'Kasir'), yang digunakan untuk menu kembali ke main_menu.

- Menu yang tersedia pada fungsi ini sebagai berikut:
Menampilkan Inventory Gudang:
1. Menampilkan Inventory Bread      
    - menampilkan inventory bread di gudang
    - memanggil dictionary bread
2. Menampilkan Inventory Protein    
    - menampilkan inventory protein di gudang
    - memanggil dictionary protein
3. Menampilkan Inventory Cheese     
    - menampilkan inventory cheese di gudang
    - memanggil dictionary cheese
4. Menampilkan Inventory Sauce      
    - menampilkan inventory sauce di gudang
    -  memanggil dictionary sauce
5. Menampilkan Inventory Veggie     
    - menampilkan inventory veggie di gudang
    - memanggil dictionary veggie
6. Menampilkan Inventory Drink      
    - menampilkan inventory drink di gudang
    - memanggil dictionary drink
7. Menampilkan Seluruh Inventory    
    - menampilkan seluruh inventory di gudang
    - memanggil dictionary inventory_all
8. Menampilkan Inventory Dengan Stock Minimal 
    - menampilkan inventory sesuai dengan stock minimal yg diinputkan user. akan menampilkan 2 tabel. 1 tabel menampilkan invenroty dengan stock > inputan user, 1 tabel menampilkan inventory dengan stok <= inputan user
9. Kembali ke Main Menu             
    - memanggil fungsi main_menu(posisi)

--------------------------------------------------------------------------------------------------------------------------
# def create_program():
- Fungsi ini digunakan untuk menambah item di dalam inventory sesuai inputan user.
- Tabel dalam fungsi menambah inventory ini akan menggunakan fungsi display_inventory (pilih_dict,teks).

- Nama item dari bahan baku pada inventory merupakan primary key.
- Jika nama item yang diinputkan sudah ada dalam inventory, maka tidak bisa ditambahkan.
- Jika nama item yang diinputkan belum ada dalam inventory, maka akan diminta untuk menginputkan informasi mengenai item tersebut (stock, harga, fat, prot, dan kal), dengan aturan: int(tambah_stock)>=0, int(tambah_harga)>=0, float(tambah_fat)>=0, float(tambah_prot)>=0, dan float(tambah_kal)>=0.
- Jika nama item dan informasi terkaitnya valid, maka akan berhasil ditambahkan.
- Jika nama item atau minimal satu informasi terkaitnya tidak valid, maka akan gagal ditambahkan.

- Jika terdapat inputan index yang tidak sesuai/ inputan yang tidak valid, maka akan keluar pesan peringatan dan memanggil fungsi lanjut('menampilkan inventory').
 
- posisi = variabel global yang berkaitan dengan fungsi lainnya berisi info jabatan user ('Owner' atau 'Kasir'), yang digunakan untuk menu kembali ke main_menu.

- Menu yang tersedia pada fungsi ini sebagai berikut:
Menambah Inventory Gudang:
1. Menambah Inventory Bread     
    - akan membuat item bread baru berserta informasinya
    - memanggil dictionary bread
2. Menambah Inventory Protein   
    - akan membuat item protein baru berserta informasinya
    - memanggil dictionary protein
3. Menambah Inventory Cheese    
    - akan membuat item cheese baru berserta informasinya
    - memanggil dictionary cheese
4. Menambah Inventory Sauce     
    - akan membuat item sauce baru berserta informasinya
    - memanggil dictionary sauce
5. Menambah Inventory Veggie    
    - akan membuat item veggie baru berserta informasinya
    - memanggil dictionary veggie
6. Menambah Inventory Drink     
    - akan membuat item drink baru berserta informasinya
    - memanggil dictionary drink
7. Kembali ke Main Menu         
    - memanggil fungsi main_menu(posisi)

--------------------------------------------------------------------------------------------------------------------------
# def update_program():
- Fungsi ini digunakan untuk meng-update informasi stock atau harga pada inventory yang dipilih user.
- Tabel dalam fungsi mengupdate inventory ini akan menggunakan fungsi display_inventory (pilih_dict,teks).

- Informasi (stock atau harga) yang diinputkan user akan tersimpan pada variabel: info_update. info_update harus bilangan bulat positif.
- Jika semua inputan user valid, maka data info item yang dipilih akan berhasil di update dan akan ditampilkan dalam tabel yang sudah di update, dengan memanggil fungsi display_inventory (pilih_dict,teks). 
- Jika minimal satu inputan tidak valid, maka data tidak dapat di update.

- Jika terdapat inputan index yang tidak sesuai/ inputan yang tidak valid, maka akan keluar pesan peringatan dan memanggil fungsi lanjut('mengupdate inventory').

- posisi = variabel global yang berkaitan dengan fungsi lainnya berisi info jabatan user ('Owner' atau 'Kasir'), yang digunakan untuk menu kembali ke main_menu.


- Menu yang tersedia pada fungsi ini sebagai berikut:
User akan diminta untuk memilih menu yang tersedia dilanjutkan memilih update informasi stock atau harga dari item.

Mengupdate Inventory Gudang:
1. Mengupdate Inventory Bread
    - akan mengupdate info stock/ harga pada item bread yang ditentukan
    - memanggil dictionary bread
2. Mengupdate Inventory Protein
    - akan mengupdate info stock/ harga pada item protein yang ditentukan
    - memanggil dictionary protein
4. Mengupdate Inventory Cheese
    - akan mengupdate info stock/ harga pada item cheese yang ditentukan
    - memanggil dictionary cheese
5. Mengupdate Inventory Sauce
    - akan mengupdate info stock/ harga pada item sauce yang ditentukan
    - memanggil dictionary sauce
6. Mengupdate Inventory Veggie
    - akan mengupdate info stock/ harga pada item veggie yang ditentukan
    - memanggil dictionary veggie
7. Mengupdate Inventory Drink
    - akan mengupdate info stock/ harga pada item drink yang ditentukan
    - memanggil dictionary drink
8. Kembali ke main menu
    - memanggil fungsi main_menu(posisi)

Pilihan Update: 
1. Update Stock
    - akan mengupdate info stock pada item dalam dictionary terpilih
    - memanggil value 'stock' pada item dalam dictionary terpilih
2. Update Harga
    - akan mengupdate info stock pada item dalam dictionary terpilih
    - memanggil value 'harga' pada item dalam dictionary terpilih

--------------------------------------------------------------------------------------------------------------------------
# def delete_program():
- Fungsi ini digunakan untuk menghapus item satu persatu ataupun secara keseluruhan dalam dictionary yang dipilih user. Untuk setiap pilihan menu yang dipilih user, akan dikonfirmasi dahulu, untuk dihapus/ tidak jadi dihapus.

- Tabel dalam fungsi menghapus inventory ini akan menggunakan fungsi display_inventory (pilih_dict,teks).

- Jika terdapat inputan index yang tidak sesuai/ inputan yang tidak valid, maka akan keluar pesan peringatan dan memanggil fungsi lanjut('delete inventory').

- posisi = variabel global yang berkaitan dengan fungsi lainnya berisi info jabatan user ('Owner' atau 'Kasir'), yang digunakan untuk menu kembali ke main_menu.

- Menu yang tersedia pada fungsi ini sebagai berikut:
Menghapus Inventory Gudang:
1. Menghapus Inventory Bread
    - akan menghapus item pada dictionary bread yang ditentukan
    - memanggil dictionary bread
2. Menghapus Inventory Protein
    - akan menghapus item pada dictionary protein yang ditentukan
    - memanggil dictionary protein
3. Menghapus Inventory Cheese
    - akan menghapus item pada dictionary cheese yang ditentukan
    - memanggil dictionary cheese
4. Menghapus Inventory Sauce
    - akan menghapus item pada dictionary sauce yang ditentukan
    - memanggil dictionary sauce
5. Menghapus Inventory Veggie
    - akan menghapus item pada dictionary veggie yang ditentukan
    - memanggil dictionary veggie
6. Menghapus Inventory Drink
    - akan menghapus item pada dictionary drink yang ditentukan
    - memanggil dictionary drink
7. Menghapus Seluruh Inventory
    - akan menghapus seluruh item pada dictionary
    - memanggil semua dictionary untuk dihapus
8. Kembali ke main menu
    - memanggil fungsi main_menu(posisi)

--------------------------------------------------------------------------------------------------------------------------
# def transaksi():
- Fungsi ini digunakan untuk proses transaksi penjualan item dari inventory, yang dibagi menjadi jenis makanan atau minuman. Jenis makanan berupa costum dari bahan baku makanan yang tersedia. Ketika user sudah menginputkan dengan benar transaksi akan ditambahkan ke list keranjang[] dan akan dikalkulasikan totalnya dalam total_keseluruhan.

- Fungsi transaksi tidak akan berjalan ketika seluruh inventory kosong dan akan memberikan pesan tentang hal tersebut. Setelah itu user akan langsung kembali ke main menu dengan menanggil fungsi main_menu(posisi).

- Pada fungsi ini, user akan diarahkan ke pemesanan custom makanan terlebih dahulu, yang akan di looping berurutan sesuai dictionary dalam tuple berikut:
    opsi_opsi={ 
        1: (bread, 'Roti'),
        2: (protein, 'Protein'),
        3: (cheese, 'Keju'),
        4: (sauce, 'Saus'),
        5: (veggie, 'Sayur')}
        #dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
opsi_opsi akan menjadi variabel global yang akan digunakan pada fungsi transaksi_makanminum (makanan) untuk pemesanan makanan.

- Jika user telah selesai memesan makanan, akan ditawarkan untuk memesan minuman. jika user ingin memesan minuman, maka isi dictionary yang dipakai adalah minuman:
   opsi_opsi={ 
        1: (drink, 'Minuman')}
        # dict yg berisi tuple (nama_dict, dan nama_dict dlm string)
opsi_opsi akan menjadi variabel global yang akan digunakan pada fungsi transaksi_makanminum (minuman) untuk pemesanan minuman.
      
- Tabel dalam fungsi menghapus inventory ini akan menggunakan fungsi display_inventory (pilih_dict,teks).

- no_urut merupakan variabel yang diinisiasi awal = 1, guna menampilkan nomor urut pada struk list kerangjang    
    no_urut = 1 
- total_keseluran merupakan variabel yang diisiasi awal=0, untuk menyimpan total harga pada seluruh pembelian menu custom
    total_keseluruhan = 0 
- keranjang merupakan list kosong untuk menyompan barang yang akan dibeli dalam satu transaksi

--------------------------------------------------------------------------------------------------------------------------
# def transaksi_makanminum (makan_minum):
- Fungsi ini akan melakukan proses pemilihan dan penambahan item yang dipilih oleh user ke dalam keranjang belanja dalam transaksi penjualan.
- Tabel dalam fungsi ini akan menggunakan fungsi display_inventory (pilih_dict,teks).

- Cara penulisan index item yang dipilih:
    - Pisahkan dengan koma jika lebih dari 1 pilihan. Contoh:(1,2)
    - Input angka (index) berlaku kelipatan. Contoh:2,2,2 untuk pemesana 3 item yg sama
    - Input angka nol (0), untuk melewatkan item

- makan_minum merupakan string yg berisi jenis item yang akan dibeli: 'makanan' atau 'minuman'
- global keranjang merupakan list yang menyimpan item-item yang akan dibeli dalam satu transaksi
- global no_urut merupakan integer untuk menyimpan no urut dalam keranjang belanja
- global total_keseluruhan merupakan float untuk menyimpan total belanja keseluruhan
- global opsi_opsi  dictionary berisi tuple yang berisi jenis bahan baku yang dapat dibeli
