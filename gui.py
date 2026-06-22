import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from main import tambah_kebijakan
import json
import os

def muat_data_ke_tabel():
    # Pastikan variabel tree sudah ada secara global
    for i in tree.get_children():
        tree.delete(i)
    
    if os.path.exists("arsip_kebijakan.json"):
        with open("arsip_kebijakan.json", "r") as f:
            try:
                data_arsip = json.load(f)
                for item in data_arsip:
                    # Pastikan key di sini sesuai dengan struktur JSON Anda
                    # Jika JSON Anda adalah objek yang dibungkus, sesuaikan aksesnya
                    tree.insert('', 'end', values=(
                        item.get('tahun', '-'), 
                        item.get('fokus', '-'), 
                        item.get('kategori', '-')
                    ))
            except (json.JSONDecodeError, AttributeError):
                pass

def tombol_kirim():
    try:
        data = {"tahun": int(entry_tahun.get()), "fokus": entry_fokus.get()}
        kategori = combo_kategori.get()
        anggaran = int(entry_anggaran.get())
        
        status, pesan = tambah_kebijakan(data, kategori, anggaran)
        
        if status:
            messagebox.showinfo("Berhasil", pesan)
            tree.insert('', 'end', values=(data['tahun'], data['fokus'], kategori))
            entry_fokus.delete(0, 'end')
            entry_anggaran.delete(0, 'end')
        else:
            messagebox.showerror("Ditolak", pesan)
    except ValueError:
        messagebox.showwarning("Error", "Tahun & Anggaran harus angka!")

# Setup Utama
root = tb.Window(themename="superhero") 
root.title("GIC 2045: Dashboard Digital Nasional")
root.geometry("800x700")

# Header
tb.Label(root, text="NEGARA DIGITAL GIC 2045", font=("Helvetica", 24, "bold"), bootstyle="inverse-primary").pack(pady=20)

# --- 1. Frame Input ---
frame_input = tb.LabelFrame(root, text="Input Kebijakan Baru")
frame_input.pack(fill=X, padx=30, pady=10)

row1 = tb.Frame(frame_input)
row1.pack(fill=X, padx=10, pady=10)

tb.Label(row1, text="Tahun:").pack(side=LEFT, padx=5)
entry_tahun = tb.Entry(row1, width=10)
entry_tahun.pack(side=LEFT, padx=5)

tb.Label(row1, text="Kategori:").pack(side=LEFT, padx=5)
combo_kategori = tb.Combobox(row1, values=["RPJP", "RPJM", "RKT"], width=10)
combo_kategori.current(2)
combo_kategori.pack(side=LEFT, padx=5)

tb.Label(frame_input, text="Fokus Kebijakan:").pack(fill=X, padx=10)
entry_fokus = tb.Entry(frame_input)
entry_fokus.pack(fill=X, padx=10, pady=5)

tb.Label(frame_input, text="Anggaran (IDR):").pack(fill=X, padx=10)
entry_anggaran = tb.Entry(frame_input)
entry_anggaran.pack(fill=X, padx=10, pady=5)

btn_kirim = tb.Button(frame_input, text="Simpan Kebijakan Negara", command=tombol_kirim, bootstyle="success", width=20)
btn_kirim.pack(pady=15)

# --- 2. Frame Tabel ---
frame_tabel = tb.LabelFrame(root, text="Log Kebijakan Publik")
frame_tabel.pack(fill=BOTH, expand=YES, padx=30, pady=20)

columns = ('tahun', 'fokus', 'kategori')
tree = tb.Treeview(frame_tabel, columns=columns, show='headings', bootstyle="info")
tree.heading('tahun', text='Tahun')
tree.heading('fokus', text='Fokus Kebijakan')
tree.heading('kategori', text='Kategori')
tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

root.mainloop()