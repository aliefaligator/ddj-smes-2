def berangkat_sekolah(pakaian, kit):
    if pakaian == "seragam" and kit == "buku":
        print("berangkat sekolah")
    else:
        print("pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("raihan"), berangkat_sekolah("seragam", "buku"))
print(nama_siswa("murti"), berangkat_sekolah("jeans", "tidak membawa buku"))
