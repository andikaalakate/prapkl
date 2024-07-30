import random
from tabulate import tabulate

# Gaji pokok setiap guru
gaji_pokok = 5000000  # Contoh: Rp 5.000.000

# Data pengalaman mengajar setiap guru (dalam tahun)
pengalaman_guru = []

# Randomisasi pengalaman mengajar setiap guru hingga sampai 10 index dalam list
for i in range(10):
    pengalaman = random.randint(
        1, 20
    )  # Ubah rentang sesuai kebutuhan, di sini dari 1 hingga 20 tahun
    pengalaman_guru.append(pengalaman)

# Inisialisasi daftar untuk menyimpan total gaji setiap guru
total_gaji_guru = []
tunjangan_guru = []

# Perulangan untuk menghitung gaji setiap guru
for pengalaman in pengalaman_guru:
    if pengalaman < 5:
        tunjangan = 0.10 * gaji_pokok
    elif 5 <= pengalaman <= 10:
        tunjangan = 0.20 * gaji_pokok
    elif pengalaman > 10:
        tunjangan = 0.40 * gaji_pokok
    elif pengalaman == 0:
        tunjangan = 0
    elif pengalaman >= 20:
        tunjangan = 0.60 * gaji_pokok
    else:
        tunjangan = 1.0 * gaji_pokok
    total_gaji = gaji_pokok + tunjangan
    total_gaji_guru.append(total_gaji)
    tunjangan_guru.append(tunjangan)

# Menyiapkan data untuk ditampilkan
data = []
for i, (pengalaman, tunjangan, total_gaji) in enumerate(
    zip(pengalaman_guru, tunjangan_guru, total_gaji_guru)
):
    data.append(
        [
            i + 1,
            pengalaman,
            f"Rp {gaji_pokok:,.2f}",
            f"Rp {tunjangan:,.2f}",
            f"Rp {total_gaji:,.2f}",
        ]
    )

# Menampilkan hasil perhitungan gaji dalam format tabel
headers = ["Guru ke-", "Pengalaman (tahun)", "Gaji Pokok", "Tunjangan", "Total Gaji"]
print(tabulate(data, headers=headers, tablefmt="grid", numalign="right"))