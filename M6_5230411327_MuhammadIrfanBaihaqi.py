id_order = 1
id_delivery = 1
order = []  # DAFTAR AKUN PENGORDER
daftar_barang = []  # DAFTAR BARANG YANG TERSEDIA DI TOKO
pesanan = []  # DAFTAR PESANAN YANG DIPESAN PENGORDER
daftar_delivery = []  # DAFTAR DELIVERY YANG SEDANG DILAKUKAN
sku = 1
objekorder = []

from datetime import datetime
from tabulate import tabulate

class Barang:
    def __init__(self, nama, harga) -> None:
        global sku
        self._sku = sku
        self.namaBarang = nama
        self.harga = harga
        daftar_barang.append(self)
        sku += 1

    @staticmethod
    def displayall():
        headers = ["No.SKU", "Nama Barang", "Harga"]
        table = [[barang._sku, barang.namaBarang, barang.harga] for barang in daftar_barang]
        print("DAFTAR BARANG")
        print(tabulate(table, headers=headers, tablefmt="grid"))

class Order:
    def __init__(self, nama, details) -> None:
        global id_order
        self._id_order = id_order
        self.nama = nama  # nama pengorder
        self.details = details
        order.append(self)
        id_order += 1
        self.setOrder()
        self.delivery = self.createDelivery()  # Store the delivery object reference

    def setOrder(self):
        while True:
            Barang.displayall()
            no_sku = input("Masukkan No.SKU barang yang ingin dibeli: ")
            for i in daftar_barang:
                if no_sku == str(i._sku):
                    while True:
                        jumlahBeli = input("Masukkan Jumlah beli: ")
                        if jumlahBeli.isdigit():
                            jumlahBeliInt = int(jumlahBeli)
                            totalHarga = jumlahBeliInt * i.harga
                            pesanan.append([self._id_order, i.namaBarang, jumlahBeliInt, totalHarga])
                            return True
                        else:
                            print("Jumlah Beli berupa angka")
                    # break
            else:
                print("No.SKU tidak ada")

    def createDelivery(self):
        information = "Informasi detail pesanan"
        address = input("Masukkan alamat pengiriman: ")
        return Deliver(self.nama, information, address)

    @staticmethod
    def displayAllOrders():
        headers = ["ID Order", "Nama Pengorder", "Detail"]
        table = [[o._id_order, o.nama, o.details] for o in order]
        print("DAFTAR ORDER")
        print(tabulate(table, headers=headers, tablefmt="grid"))

class Deliver:
    def __init__(self, nama, information, address) -> None:
        global id_delivery
        self._id = id_delivery
        self.nama = nama
        self.information = information
        self.date = datetime.now().date()
        self.address = address
        self.status_pesanan = "Diproses Toko"  # STATUS DEFAULT
        daftar_delivery.append(self)
        id_delivery += 1

    def processDelivery(self):
        try:
            id_to_update = int(input("Masukkan id delivery untuk update status pesanan: "))
            for delivery in daftar_delivery:
                if id_to_update == delivery._id:
                    delivery.status_pesanan = input("Masukkan update status delivery terkini: ")
                    return True
            print("ID DELIVERY TIDAK ADA")
            return False
        except ValueError:
            print("ID BERUPA ANGKA")

# Contoh penggunaan
pensil = Barang("Pensil", 10000)
# order1 = Order("Nama Pengorder", "Detail Pesanan")

# Panggil processDelivery kapan saja
# order1.delivery.processDelivery()

def menuutama():
    while True:
        print("1. Tambahkan Barang")
        print("2. Buat Order")
        print("3. Update Pesanan Pengorder")
        print("4. Tampilkan Semua Order")
        print("5. Keluar Program")
        pilih = input('Masukkan Pilihan anda: ')
        if pilih == '1':
            tambahBarang()
        elif pilih == '2':
            buatOrder()
        elif pilih == '3':
            updatePesanan()
        elif pilih == '4':
            Order.displayAllOrders()
        elif pilih == '5':
            return True
        else:
            print("Pilihan anda salah")

def tambahBarang():
    namabarang = input("Masukan Nama Barang: ")
    while True:
        hargastr = input("Masukkan Harga Barang: ")
        cek = hargastr.isdigit()
        if cek:
            harga = int(hargastr)
            barang = Barang(namabarang, harga)
            break
        else:
            print("Harga harus berupa angka")

def buatOrder():
    namaPengorder = input("Masukkan nama pengorder: ")
    details = input("Masukan detail pengorderan: ")
    objek_order = Order(namaPengorder, details)
    objekorder.append(objek_order)

def updatePesanan():
    Order.displayAllOrders()
    id_order_to_update = int(input("Masukkan ID order yang ingin di-update: "))
    for obj_order in order:
        if obj_order._id_order == id_order_to_update:
            obj_order.setOrder()
            break
    else:
        print("ID order tidak ada")

# Menjalankan menu utama
menuutama()
