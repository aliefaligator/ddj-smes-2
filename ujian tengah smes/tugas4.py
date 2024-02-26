belanjaan= {
    "apel":{"harga": 5000, "jumlah": 10},
     "jeruk":{"harga": 3000, "jumlah": 5},
     "mangga":{"harga": 7000, "jumlah": 7},
      "pisang":{"harga": 2000, "jumlah": 20},
     "semangka":{"harga": 15000, "jumlah": 1},
}

total_belanja = 0
for buah , info in belanjaan.items():
    total_harga = info ["harga"]* info["jumlah"]
    total_belanja += total_harga
    print("total harga {buah} : rp{total_harga}")
     
print("total belanjaan inbu sari adalah: rp", total_belanja)