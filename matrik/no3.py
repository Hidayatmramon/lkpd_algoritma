print("Masukkan jam, menit, detik: ")
jam = int(input())
menit = int(input())
detik = int(input())

dj = jam * 3600
dm = menit * 60
totaldetik = dj + dm + detik

print(f"{totaldetik}")
