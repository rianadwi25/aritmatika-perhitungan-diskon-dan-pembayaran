import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung nilai, biaya, diskon, dan bayar
def hitung_nilai():
    try:
        nim = entry_nim.get()
        nama = entry_nama.get()
        nilai = float(entry_nilai.get())
        jurusan = entry_jurusan.get().upper()  # Mengambil input jurusan dan mengubah menjadi huruf besar

        if not nim or not nama or not jurusan:
            messagebox.showerror("Error", "NIM, Nama, dan Jurusan harus diisi!")
            return

        # Menentukan hasil penilaian berdasarkan nilai
        if nilai >= 80:
            hasil = "Lulus dengan Pujian"
        elif 60 <= nilai < 80:
            hasil = "Lulus"
        elif 40 <= nilai < 60:
            hasil = "Remedial"
        else:
            hasil = "Tidak Lulus"

        # Menentukan biaya berdasarkan jurusan
        if jurusan == "SI":
            biaya = 5000000
        elif jurusan == "SK":
            biaya = 6000000
        elif jurusan == "MI":
            biaya = 7000000
        else:
            messagebox.showerror("Error", "Jurusan tidak valid! Masukkan SI, SK, atau MI.")
            return

        # Menghitung diskon 10% dari biaya
        diskon = biaya * 0.10
        bayar = biaya - diskon

        # Menampilkan hasil melalui messagebox
        messagebox.showinfo("Hasil Perhitungan", f"NIM: {nim}\nNama: {nama}\nHasil: {hasil}\nBiaya: Rp {biaya:,}\nDiskon 10%: Rp {diskon:,}\nBayar: Rp {bayar:,}")
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka nilai yang valid!")

# Fungsi untuk membersihkan input
def bersihkan():
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_nilai.delete(0, tk.END)
    entry_jurusan.delete(0, tk.END)

# Fungsi untuk menutup aplikasi
def tutup_aplikasi():
    window.quit()

# Membuat jendela utama
window = tk.Tk()
window.title("Penghitung Nilai, Biaya, Diskon, dan Pembayaran")

# Mengatur latar belakang jendela
window.configure(bg="lightblue")

# Label dan input untuk NIM
label_nim = tk.Label(window, text="Masukkan NIM:", width=25, anchor="w", bg="lightblue")
label_nim.grid(row=0, column=0, padx=10, pady=5)

entry_nim = tk.Entry(window)
entry_nim.grid(row=0, column=1, padx=10, pady=5)

# Label dan input untuk Nama
label_nama = tk.Label(window, text="Masukkan Nama:", width=25, anchor="w", bg="lightblue")
label_nama.grid(row=1, column=0, padx=10, pady=5)

entry_nama = tk.Entry(window)
entry_nama.grid(row=1, column=1, padx=10, pady=5)

# Label dan input untuk Nilai
label_nilai = tk.Label(window, text="Masukkan Nilai (0-100):", width=25, anchor="w", bg="lightblue")
label_nilai.grid(row=2, column=0, padx=10, pady=5)

entry_nilai = tk.Entry(window)
entry_nilai.grid(row=2, column=1, padx=10, pady=5)

# Label dan input untuk Jurusan
label_jurusan = tk.Label(window, text="Masukkan Jurusan (SI/SK/MI):", width=25, anchor="w", bg="lightblue")
label_jurusan.grid(row=3, column=0, padx=10, pady=5)

entry_jurusan = tk.Entry(window)
entry_jurusan.grid(row=3, column=1, padx=10, pady=5)

# Lebar tombol yang sama
button_width = 15

# Tombol untuk menghitung nilai, biaya, diskon, dan bayar
tombol_hitung = tk.Button(window, text="Hitung", command=hitung_nilai, width=button_width, bg="blue", fg="white")
tombol_hitung.grid(row=4, column=0, columnspan=2, pady=5)

# Tombol untuk membersihkan input
tombol_bersih = tk.Button(window, text="Bersih", command=bersihkan, width=button_width, bg="blue", fg="white")
tombol_bersih.grid(row=5, column=0, columnspan=2, pady=5)

# Tombol untuk menutup aplikasi
tombol_tutup = tk.Button(window, text="Tutup", command=tutup_aplikasi, width=button_width, bg="blue", fg="white")
tombol_tutup.grid(row=6, column=0, columnspan=2, pady=5)

# Menjalankan jendela utama
window.mainloop()
