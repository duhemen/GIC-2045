from blockchain import GoldenIndonesiaChain
from database import init_db
import database
from aspirasi import filter_usulan
from aspirasi import rekam_vote, cek_lolos_voting, filter_usulan

init_db()

def ajukan_usulan_rakyat(data_usulan):
    print(f"\n[RAKYAT]: Mengajukan usulan pembangunan: {data_usulan}")
    # Simpan usulan di "Memori Sementara" atau file usulan.txt
    with open("aspirasi.txt", "a") as f:
        f.write(data_usulan + "\n")
    print("[SISTEM]: Usulan diterima dan sedang dalam proses verifikasi publik.")

# Simulasi rakyat mengajukan usulan
ajukan_usulan_rakyat("Pembangunan Infrastruktur Digital Desa")

def tampilkan_transparansi_bangsa(chain):
    print("\n--- TRANSPARANSI GIC 2045 ---")
    for block in chain:
        print(f"Periode {block.data.get('periode', 'N/A')} | Fokus: {block.data.get('fokus', 'N/A')}")
        print(f"Sidik Jari Digital (Hash): {block.hash}")
        # Menampilkan status tanda tangan agar rakyat tahu ini sudah disahkan atau belum
        status_tanda_tangan = all(block.signatures.values())
        print(f"Status Sah: {'SAKRAL (Tervalidasi 3 Pilar)' if status_tanda_tangan else 'PENDING'}")
        print("-" * 40)

# --- EKSEKUSI UTAMA ---
gic = GoldenIndonesiaChain()

# Menambahkan milestone dan langsung disahkan
blok1 = gic.add_block({"periode": "2025-2029", "fokus": "SDM"})
for auth in ["eksekutif", "legislatif", "yudikatif"]: blok1.sign_block(auth)

blok2 = gic.add_block({"periode": "2030-2034", "fokus": "Ekonomi"})
for auth in ["eksekutif", "legislatif", "yudikatif"]: blok2.sign_block(auth)

blok3 = gic.add_block({"periode": "2035-2039", "fokus": "Teknologi"})
for auth in ["eksekutif", "legislatif", "yudikatif"]: blok3.sign_block(auth)

# Panggil fungsi tampilannya
tampilkan_transparansi_bangsa(gic.chain)

# --- SKENARIO MANIPULASI (Uji Ketangguhan) ---
print("\n--- TEST: Skenario Manipulasi Data ---")
print("PERINGATAN: Oknum mencoba mengubah data periode 2025-2029...")
gic.chain[1].data['fokus'] = "KORUPSI DANA" 

# Cek dengan aturan baru
is_valid, pesan = gic.is_chain_valid()
print(f"Status Integritas Nasional: {'AMAN' if is_valid else 'BAHAYA!'}")
print(f"Pesan Audit: {pesan}")

if not is_valid:
    print("Sistem mendeteksi ketidakcocokan Hash. Manipulasi diblokir!")

# --- SKENARIO ASPIRASI RAKYAT ---
usulan_rakyat = "Pembangunan Infrastruktur Digital Desa"
is_layak, pesan = filter_usulan(usulan_rakyat)

if is_layak:
    print(f"\n[SISTEM]: {pesan}")
    print("[SISTEM]: Usulan masuk ke tahap VOTING PUBLIK...")
    # Di sini nanti kita akan tambahkan logic voting
else:
    print(f"\n[SISTEM]: DITOLAK. {pesan}")

# 1. Rakyat mengusulkan
usulan = "Pembangunan Infrastruktur Digital Desa"
is_layak, msg = filter_usulan(usulan)

if is_layak:
    # 2. Simulasi Rakyat Voting (Anggap ada 5 orang yang voting)
    print(f"\n[VOTING]: Usulan '{usulan}' sedang divoting...")
    rekam_vote("ya")
    rekam_vote("ya")
    rekam_vote("tidak")
    rekam_vote("ya")
    rekam_vote("ya")
    
    # 3. Cek hasil
    if cek_lolos_voting():
        print("[SISTEM]: Voting menang! Menginisiasi pembuatan blok baru...")
        
        # 4. Otomatis buat block baru & tanda tangan
        blok_baru = gic.add_block({"periode": "2040-2044", "fokus": usulan})
        for auth in ["eksekutif", "legislatif", "yudikatif"]: 
            blok_baru.sign_block(auth)
        print("[SISTEM]: Blok berhasil disahkan oleh 3 Pilar!")
    else:
        print("[SISTEM]: Voting gagal, usulan tidak disahkan.")