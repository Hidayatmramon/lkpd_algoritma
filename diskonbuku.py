    # Seorang penjual buku pelajar smk berusaha menarik pembeli dengan ketentuan sbb:
    # - jika jumlah buku yang dibeli lebih kecil atau sama dengan 100 eksemplar, maka tidak ada diskon,
    # - jika jumlah buku yang dibeli lebih besar dari 100 dan kurang dari atau sama dengan 200 eksemplar maka untuk 100 eksemplar yang pertama dapat diskon 5% sedangkan sisanya mendapat diskon 15%
    # - jika jumlah buku ynag dibeli lebih besar dari 200 eksemplar maka 100 eksemplar pertama diskon 7% 100 eksemplar kedua diskon 17% dan sisanya diskon 27%
    # - jika harga satu eksemplar buku Rp. 5000, buatlah program untuk menentukan Harga total yang Harga dibayar dengan inputan berupa jumlah buku yang di beli
    # - 10 eksemplar =  1 buku


buku = int(input("jumlah buku: "))
harga_per_eksemplar = 5000
eksemplar = buku * 10

if buku <= 100:
    hasil = eksemplar * harga_per_eksemplar
    print(f"Total harga : {hasil:,}")

elif buku > 100 and buku <= 200:
    diskon_pertama = 100 * harga_per_eksemplar * 0.95
    diskon_kedua = (eksemplar - 100) * harga_per_eksemplar * 0.85
    hasil = diskon_pertama + diskon_kedua
    print(f"Total harga : {hasil:,}")

else:  
    diskon_pertama = 100 * harga_per_eksemplar * 0.93

    diskon_kedua = 100 * harga_per_eksemplar * 0.83

    diskon_ketiga = (eksemplar - 200) * harga_per_eksemplar * 0.73
    hasil = diskon_pertama + diskon_kedua + diskon_ketiga
    print(f"Total harga : {hasil:,}")
