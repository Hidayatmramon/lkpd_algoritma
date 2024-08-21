for tahun in range(1600, 2025, 4):
    if tahun % 400 == 0:
        print(tahun, "Adalah Tahun Kabisat")
    elif tahun % 100 == 0:
        print(tahun, "Bukan Tahun Kabisat")
    elif tahun % 4 == 0:
        print(tahun, "Adalah Tahun Kabisat")
    else:
        print(tahun, "Bukan Tahun Kabisat")
