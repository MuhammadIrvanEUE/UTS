def Pelanggan():
    NIM = 20210801352
    NAMA =  "MUHAMMAD IRVAN"
    print("NIM : " ,NIM)
    print ("NAMA : ",NAMA)

def Produk():
    a = "Capuccino"
    b = "Teh"
    print("Pilihan")
    print("1. ",a)
    print("2. ",b)
    print("3. Exit")

def Capuccino():
    Capuc = "Memilih Capuccino"
    print(Capuc)    
    Capuccino = int(input("Masukkan Harga: "))
    PPN = 0.1
    Total = Capuccino + (Capuccino*PPN)
    print("Jumlah yang harus dibayarkan: ",Total)

def Teh():
    Tea = "Memilih Teh"
    print(Tea)    
    Tea = int(input("Masukkan Harga: "))
    PPN = 0.1
    Total = Tea + (Tea*PPN)
    print("Jumlah yang harus dibayarkan: ",Total)

while True:
    Pelanggan()
    Produk()
    Pilih = int(input("Masukkan Pilihan: "))
    if Pilih == 1:
        Capuccino()
    elif Pilih == 2:
        Teh()
    elif Pilih == 3:
        break