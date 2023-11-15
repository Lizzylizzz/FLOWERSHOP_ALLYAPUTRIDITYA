Nama            : Allya Putri Ditya
NIM             : 2309116078
Tema Program    : Flower Shop

from prettytable import PrettyTable

# Dictionary
data_akun = {
    "Lizzy": {"pin": "1122", "saldo": 100000, "e-pay": 100000},
    "Lily": {"pin": "2899", "saldo": 7000000, "e-pay": 500000},
    "aabb": {"pin": "1234", "saldo": 3000000, "e-pay": 250000}
}

pin_vip = {"pin": "1234"}

voucher ={ "kode": "imarklee99", "nama voucher" : "watermelon", "diskon" : 0.30, "status" : 1}

# Tabel bunga
table_bunga = PrettyTable()
table_bunga.field_names = ["No", "Bunga", "Harga"] 
table_bunga.add_row([1, "Daisy", 30000])
table_bunga.add_row([2, "Rose", 40000])
table_bunga.add_row([3, "Lily", 90000])


# Fungsi

def transaksi_bunga():
    print("\n==================== Transaksi Bunga =====================\n")
    print(table_bunga)
    try:
        nomor_bunga = int(input("\nMasukkan nomor bunga yang ingin dibeli (0 untuk kembali): "))
        if 1 <= nomor_bunga <= len(table_bunga._rows):
            jumlah_bunga = int(input("Masukkan jumlah bunga yang ingin dibeli: "))
            harga_bunga = table_bunga._rows[nomor_bunga-1][2]
            total_harga = jumlah_bunga * harga_bunga
            print(f"\nTotal harganya adalah Rp. {total_harga} ")
            member(total_harga)
        elif nomor_bunga == 0:
            return
        else:
            print("Nomor bunga tidak valid, coba lagi\n")
    except:
        print("Inputan tidak valid, coba lagi\n")

def proses_pembayaran(total_harga):
    print("\n=================== Pembayaran ===================\n")
    print("1. E-pay\n2. Voucher\n3. Kembali")
    bayar = input("Pilih metode pembayaran : ")

    if bayar == "1":
        if data_akun[nama]["e-pay"] >= total_harga:
            data_akun[nama]["e-pay"] -= total_harga
            print("Pembayaran berhasil menggunakan e-pay.")
        else:
            print("e-pay tidak mencukupi untuk pembayaran.")
    elif bayar == "2":
        kode_voucher = input("Masukkan kode voucher anda : ")
        if voucher["kode"] == kode_voucher and voucher["status"] >= 1 :
            diskon = total_harga - (total_harga * 0.30)
            data_akun[nama]["e-pay"] -= diskon
            voucher["status"] = voucher["status"] - 1
            print(f"Selamat! anda mendapatkan diskon 30%, harga menjadi {diskon}\nVoucher berhasil digunakan")
        else :
            voucher["kode"] != kode_voucher and voucher["status"] < 1
            print("Kode voucher salah atau voucher habis")
    elif bayar == "3":
        return
    else:
        print("Metode pembayaran tidak valid.")


def member(total_harga):
    member = input("\nApakah anda memiliki member? (ya/tidak) : ")
    if member == "ya":
        pin = input("Masukkan pin anda : ")
        if pin_vip["pin"] == pin :
            if data_akun[nama]["e-pay"] >= total_harga:
                print("Anda mendapatkan diskon sebesar 30%")
                diskon = total_harga - (total_harga * voucher["diskon"])
                data_akun[nama]["e-pay"] -= diskon
                print(f"\ntotal harga menjadi {diskon} Pembayaran berhasil menggunakan e-pay.")
            else:
                print("e-pay tidak mencukupi untuk pembayaran.")
        else :
            print("Pin tidak terdaftar dalam member")
    elif member == "tidak":
        proses_pembayaran(total_harga)
    else :
        print("Inputan tidak valid, coba lagi")


def tambah_saldo():
    print("\n========================= Tambah Saldo =========================\n")
    try:
        uang = int(input("Masukkan nominal uang : "))
        if uang > 0:
            data_akun[nama]["saldo"] += uang
            print(f"Saldo anda sekarang: {data_akun[nama]['saldo']}")
        else:
            print("Masukkan nominal lebih dari 0")
    except:
        print("Inputan tidak valid, coba lagi\n")


def tambah_epay():
    print("\n===================== Tambah Saldo e-pay =====================")
    try:
        jumlah = int(input("Masukkan nominal e-pay : "))
        if data_akun[nama]["saldo"] >= jumlah and jumlah > 0:
            data_akun[nama]["e-pay"] += jumlah
            data_akun[nama]["saldo"] -= jumlah
            print(f"e-pay berhasil ditambahkan, e-pay anda sekarang: {data_akun[nama]['e-pay']}")
        elif jumlah <= 0 :
            print("Masukkan nominal lebih dari 0")
        else:
            print("Saldo anda tidak mencukupi")
    except :
        print("Inputan tidak valid, coba lagi\n")


def cek_saldo():
    print("\n======================= Cek Saldo ========================\n")
    print(f"Saldo anda saat ini : {data_akun[nama]['saldo']}")
    print(f"Saldo e-pay anda saat ini : {data_akun[nama]['e-pay']}")


def registrasi_vip():
    global pin_vip, data_akun
    print("\n====================== Registrasi VIP Member ======================\n")
    try:
        pin_member = input("Masukkan pin anda : ")
        pin_baru = "1234"
        if pin_member == data_akun[nama]["pin"] :
            data_akun[nama]["pin"] = pin_baru
            pin_vip["pin"] = pin_baru
            print(f"Registrasi VIP member berhasil. PIN diatur menjadi '1234'.")
        else :
            print("Pin tidak terdaftar atau sudah terdaftar menjadi member")
    except:
        print("Inputan tidak valid, coba lagi\n")


# Menu
def menu():
    while True:
        print("\n================================================================")
        print("                         Selamat Datang                         ")
        print("================================================================\n")
        print("1. Pesan Bunga")
        print("2. Tambah saldo")
        print("3. Tambah saldo e-pay")
        print("4. Cek saldo")
        print("5. Registrasi VIP")
        print("6. Kembali")
        pilihan = input("Masukkan pilihan menu : ")
        if pilihan == "1":
            transaksi_bunga()
        elif pilihan == "2":
            tambah_saldo()
        elif pilihan == "3":
            tambah_epay()
        elif pilihan == "4":
            cek_saldo()
        elif pilihan == "5":
            registrasi_vip()
        elif pilihan == "6":
            return
        else:
            print("Inputan tidak valid, coba lagi\n")


while True:
    try:
        print("================================ Flower Shop ================================\n")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan : ")
        if pilihan == "1":
            print("================================ Login ================================\n")
            nama = input("\nMasukkan Nama anda : ")
            if nama in data_akun and data_akun[nama]["pin"] == input("Masukkan Pin anda : "):
                menu()
            else:
                print("Nama atau pin anda salah, coba lagi\n")
        elif pilihan == "2":
            break
    except :
        print("Inputan tidak valid")

