from models import Block
from database import save_block
# 1. Tambahkan import ini agar fungsi verifikasi bekerja
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class GoldenIndonesiaChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.is_frozen = False

    def create_genesis_block(self):
        # Genesis block bisa kita tandai sebagai "Sistem" atau lewat jalur khusus
        block = Block(0, {"periode": "2024", "fokus": "Genesis"}, "0")
        # Catatan: Karena genesis bersifat khusus, kita bisa mengosongkan signature-nya 
        # atau menandatanganinya dengan sistem kunci root khusus jika diperlukan.
        return block

    def add_block(self, data, kategori="RKT", ref_id=None):
        # Dapatkan hash blok sebelumnya sebagai previous_hash
        previous_hash = self.chain[-1].hash
    
        # Buat objek Block baru dengan parameter tambahan
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_hash,
            kategori=kategori,
            ref_id=ref_id
        )
    
        # Tambahkan ke dalam rantai
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self, public_keys):
        """
        public_keys: dictionary berisi public key dari eksekutif, legislatif, yudikatif
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
        
            # Cek apakah semua pilar sudah tanda tangan
            for authority, signature in current.signatures.items():
                if signature is None:
                    return False, f"Blok {i} belum ditandatangani oleh {authority}!"
                
                # Verifikasi kriptografi
                try:
                    public_keys[authority].verify(
                        signature,
                        current.hash.encode(),
                        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                        hashes.SHA256()
                    )
                except Exception as e:
                    return False, f"Tanda tangan {authority} pada blok {i} tidak valid! Error: {e}"
                
        return True, "Rantai Sah & Sakral secara Kriptografis"
    
    def validasi_sinkronisasi(self, blok_baru):
        # Logika sederhana: Cek apakah tahun blok baru valid
        # RKT harus berada dalam rentang RPJM 5 tahunan
        if blok_baru.tipe == "RKT":
            print("[AUDIT]: Memeriksa keselarasan RKT dengan RPJM & RPJP...")
            # Di sini kita bisa menambahkan logika perbandingan data
            return True
        return False
    
    def freeze_chain(self, status=True):
        self.is_frozen = status
        print(f"[STATUS SISTEM]: Chain telah {'DIBEKUKAN' if status else 'DIBUKA'}!")

    def add_block(self, data, kategori="RKT", ref_id=None, anggaran=0):
        # Dapatkan hash blok sebelumnya sebagai previous_hash
        previous_hash = self.chain[-1].hash
    
        # Buat objek Block baru dengan parameter yang lengkap
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_hash,
            kategori=kategori,
            ref_id=ref_id,
            anggaran=anggaran  # Tambahkan ini
        )
    
        # Tambahkan ke dalam rantai
        self.chain.append(new_block)
        return new_block
    
    def trace_corruption(self):
        print("\n--- LAPORAN AUDIT FORENSIK ---")
        for block in self.chain:
            print(f"Audit Blok {block.index} [Kategori: {block.kategori}]:")
            for pilar, sig in block.signatures.items():
                status = "DITANDATANGANI" if sig else "TIDAK VALID/KOSONG"
                print(f" - {pilar.upper()}: {status}")