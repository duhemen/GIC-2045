from blockchain import GoldenIndonesiaChain
from konstitusi_digital import cek_konstitusi_luca
from aspirasi import filter_usulan, cek_lolos_voting
from audit_akademik import verifikasi_akademik
from audit_ekonomi import verifikasi_privat
from pilar import sign_all_pillars
from cryptography.hazmat.primitives.asymmetric import rsa

# Pastikan keys tetap diinisialisasi
keys = {
    "eksekutif": rsa.generate_private_key(65537, 2048),
    "legislatif": rsa.generate_private_key(65537, 2048),
    "yudikatif": rsa.generate_private_key(65537, 2048),
    "akademisi": rsa.generate_private_key(65537, 2048),
    "privat":    rsa.generate_private_key(65537, 2048)
}

# Inisialisasi sistem di memori (akan digunakan GUI nanti)
gic = GoldenIndonesiaChain()

def tambah_kebijakan(data_input, kategori, anggaran):
    """Fungsi ini nanti akan dipanggil oleh Tombol 'Simpan' di GUI"""
    blok = gic.add_block(data_input, kategori=kategori, anggaran=anggaran)
    if blok:
        sign_all_pillars(blok, keys)
        gic.arsip_ke_json()
        return True, "Berhasil ditambahkan"
    return False, "Ditolak oleh sistem"

def jalankan_demo_awal():
    """Hanya untuk mengisi data awal jika sistem baru dimulai"""
    tambah_kebijakan({"tahun": 2045, "fokus": "Indonesia Emas 2045"}, "RPJP", 0)
    print("Sistem siap menerima input dari GUI.")

if __name__ == "__main__":
    jalankan_demo_awal()