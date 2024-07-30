import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


# Membuat database dan tabel jika belum ada
def buat_database():
    conn = sqlite3.connect("gaji_guru.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS guru (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            pengalaman INTEGER NOT NULL,
            gaji_pokok REAL NOT NULL,
            tunjangan REAL NOT NULL,
            total_gaji REAL NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# Fungsi untuk menyimpan data guru ke database
def simpan_data():
    nama = entry_nama.get()
    pengalaman = entry_pengalaman.get()
    gaji_pokok = 5000000  # Gaji pokok tetap

    if not (nama and pengalaman):
        messagebox.showerror("Error", "Semua bidang harus diisi!")
        return

    pengalaman = int(pengalaman)
    if pengalaman < 5:
        tunjangan = 0.10 * gaji_pokok
    elif 5 <= pengalaman <= 10:
        tunjangan = 0.20 * gaji_pokok
    else:
        tunjangan = 0.30 * gaji_pokok

    total_gaji = gaji_pokok + tunjangan

    conn = sqlite3.connect("gaji_guru.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO guru (nama, pengalaman, gaji_pokok, tunjangan, total_gaji) VALUES (?, ?, ?, ?, ?)",
        (nama, pengalaman, gaji_pokok, tunjangan, total_gaji),
    )
    conn.commit()
    conn.close()
    messagebox.showinfo("Sukses", "Data berhasil disimpan!")
    bersihkan_form()
    tampilkan_data()


# Fungsi untuk membersihkan form input
def bersihkan_form():
    entry_nama.delete(0, tk.END)
    entry_pengalaman.delete(0, tk.END)


# Fungsi untuk menampilkan data guru dalam Treeview
def tampilkan_data():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect("gaji_guru.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM guru")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert(
            "",
            tk.END,
            values=(
                row[0],
                row[1],
                row[2],
                f"Rp {row[3]:,.2f}",
                f"Rp {row[4]:,.2f}",
                f"Rp {row[5]:,.2f}",
            ),
        )


# Fungsi untuk menghapus data guru dari database
def hapus_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Pilih data yang ingin dihapus!")
        return

    item = tree.item(selected_item)
    id_guru = item["values"][0]

    conn = sqlite3.connect("gaji_guru.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM guru WHERE id = ?", (id_guru,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sukses", "Data berhasil dihapus!")
    tampilkan_data()


# Fungsi untuk mengupdate data guru di database
def update_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Pilih data yang ingin diupdate!")
        return

    item = tree.item(selected_item)
    id_guru = item["values"][0]

    nama = entry_nama.get()
    pengalaman = entry_pengalaman.get()
    gaji_pokok = 5000000  # Gaji pokok tetap

    if not (nama and pengalaman):
        messagebox.showerror("Error", "Semua bidang harus diisi!")
        return

    pengalaman = int(pengalaman)
    if pengalaman < 5:
        tunjangan = 0.10 * gaji_pokok
    elif 5 <= pengalaman <= 10:
        tunjangan = 0.20 * gaji_pokok
    else:
        tunjangan = 0.30 * gaji_pokok

    total_gaji = gaji_pokok + tunjangan

    conn = sqlite3.connect("gaji_guru.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE guru SET nama = ?, pengalaman = ?, gaji_pokok = ?, tunjangan = ?, total_gaji = ? WHERE id = ?",
        (nama, pengalaman, gaji_pokok, tunjangan, total_gaji, id_guru),
    )
    conn.commit()
    conn.close()
    messagebox.showinfo("Sukses", "Data berhasil diupdate!")
    bersihkan_form()
    tampilkan_data()


# Membuat jendela utama
root = tk.Tk()
root.title("Program Penggajian Guru")
root.geometry("800x600")
root.configure(bg="#f0f0f0")
root.resizable(width=False, height=False)

# Membuat frame input data
frame_input = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama:", bg="#f0f0f0").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
entry_nama = tk.Entry(frame_input, width=100)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Pengalaman (tahun):", bg="#f0f0f0").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_pengalaman = tk.Entry(frame_input, width=100)
entry_pengalaman.grid(row=1, column=1, padx=5, pady=5)

btn_simpan = tk.Button(
    frame_input, text="Simpan", command=simpan_data, bg="#4caf50", fg="white"
)
btn_simpan.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

btn_update = tk.Button(
    frame_input, text="Update", command=update_data, bg="#2196f3", fg="white"
)
btn_update.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

btn_hapus = tk.Button(
    frame_input, text="Hapus", command=hapus_data, bg="#f44336", fg="white"
)
btn_hapus.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

# Mengatur kolom untuk tombol agar dapat merespons ukuran jendela
frame_input.grid_columnconfigure(0, weight=1)
frame_input.grid_columnconfigure(1, weight=1)
frame_input.grid_columnconfigure(2, weight=1)

# Membuat frame untuk menampilkan data
frame_output = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_output.pack(pady=2, fill="both", expand=True)

btn_tampilkan = tk.Button(
    frame_output,
    text="Tampilkan Data",
    command=tampilkan_data,
    bg="#607d8b",
    fg="white",
)
btn_tampilkan.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Membuat Treeview untuk menampilkan data dalam bentuk tabel
columns = ("ID", "Nama", "Pengalaman", "Gaji Pokok", "Tunjangan", "Total Gaji")
tree = ttk.Treeview(frame_output, columns=columns, show="headings")
tree.grid(row=1, column=0, sticky="nsew")

# Menambahkan kolom header
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER)

# Menambahkan scrollbar vertikal
scrollbar = ttk.Scrollbar(frame_output, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky="ns")

# Mengatur grid weights agar Treeview dan Scrollbar mengambil ruang yang tersedia
frame_output.grid_rowconfigure(1, weight=1)
frame_output.grid_columnconfigure(0, weight=1)

# Membuat database dan tabel jika belum ada
buat_database()

# Menjalankan aplikasi
root.mainloop()
