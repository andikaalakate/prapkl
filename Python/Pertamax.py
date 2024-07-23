hw = "Halo Dunia"
hit = 1

print("<================================>")

for i in range(1, 11):
    print(i)

print("<================================>")

while hit < 11:
    print(hw, "=====>")
    print("Halo Dunia ke: ", hit)
    hit = hit + 1

print("<================================>")
print("Selamat Tinggal!")
print("<================================>")


def fibonacci(n):
    c = []
    a, b = 0, 1

    while len(c) < n:
        c.append(a)
        a, b = b, a + b

    return c


nJumlah = int(input("Masukkan angka: "))
c_fibonacchi = fibonacci(nJumlah)
print(c_fibonacchi)


def pola_bintang(baris):
    spasi = baris
    for i in range(1, baris + 1):
        for j in range(1, spasi + 1):
            print(" ", end="")

        for k in range(1, i + 1):
            print("* ", end="")

        print()
        spasi = spasi - 1


baris = int(input("Masukkan jumlah baris: "))
pola_bintang(baris)
