import tkinter as tk
from tkinter import messagebox

#fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <=100):
                raise ValueError("Nilai haarus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

#label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)

#frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Times New Roman", 12), bg ="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Times New Roman", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Times New Roman", 12, "bold"), bg="#4C4F50", fg="white")
prediksi_button.pack(pady=30)

hasil_label = tk.Label(root, text="", font=("Times New Roman", 14, "italic", "bold"), fg="white", bg="#f0f0f0")
hasil_label.pack(pady=20)

root.mainloop()
