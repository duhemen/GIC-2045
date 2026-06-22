from blockchain import GoldenIndonesiaChain
from konstitusi_digital import cek_konstitusi_luca
from aspirasi import filter_usulan, cek_lolos_voting
from audit_akademik import verifikasi_akademik
from audit_ekonomi import verifikasi_privat
from pilar import sign_all_pillars # Import dari pilar.py
from cryptography.hazmat.primitives.asymmetric import rsa

# Inisialisasi Kunci
keys = {
    "eksekutif": rsa.generate_private_key(65537, 2048),
    "legislatif": rsa.generate_private_key(65537, 2048),
    "yudikatif": rsa.generate_private_key(65537, 2048),
    "akademisi": rsa.generate_private_key(65537, 2048),
    "privat":    rsa.generate_private_key(65537, 2048)
}

def tampilkan_transparansi_bangsa(chain):
    kategori_map = {"RPJP": [], "RPJM": [], "RKT": []}
    for block in chain:
        kat = getattr(block, 'kategori', 'RKT')
        if kat in kategori_map:
            kategori_map[kat].append(block)
    for kat, blocks in kategori_map.items():
        print(f"\n--- KATEGORI: {kat} ---")
        for b in blocks:
            print(f"[{b.tahun}] - Fokus: {b.data.get('fokus', 'N/A')}")

def skenario_nasional():
    print("\n--- INISIALISASI NEGARA DIGITAL GIC 2045 ---")
    print("--- MEMULAI SKENARIO ---")
    gic = GoldenIndonesiaChain()
    
    # 1. Fondasi & Tanda Tangan
    rpjp = gic.add_block({"tahun": 2045, "fokus": "Indonesia Emas 2045"}, kategori="RPJP")
    sign_all_pillars(rpjp, keys)
    
    # 2. Menambah blok dengan anggaran
    rpjm = gic.add_block({"tahun": 2030, "fokus": "Infrastruktur Digital"}, kategori="RPJM", anggaran=500000000)
    sign_all_pillars(rpjm, keys)
    gic.arsip_ke_json() # <--- Arsip blok RPJM
    
    # 3. Skenario Aspirasi (RKT)
    usulan = "Pembangunan Infrastruktur Digital Desa"
    rkt = gic.add_block({"tahun": 2026, "fokus": usulan}, kategori="RKT", anggaran=500000, ref_id=rpjm.hash)
    sign_all_pillars(rkt, keys)
    gic.arsip_ke_json() # <--- Arsip blok RKT
    
    # 4. Audit & Keamanan
    gic.trace_corruption()
    
    # 5. Uji Coba Emergency Freeze
    gic.freeze_chain(True)
    gic.add_block({"tahun": 2031, "fokus": "Proyek Fiktif"}, kategori="RKT", anggaran=100)
    
    # Tampilkan Hasil
    tampilkan_transparansi_bangsa(gic.chain)

if __name__ == "__main__":
    skenario_nasional()