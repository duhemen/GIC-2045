from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import hashlib
import json
import time

class Block:
    def __init__(self, index, data, previous_hash, kategori="RKT", ref_id=None, anggaran=0):
        self.index = index
        self.data = data
        self.tahun = data.get("tahun", 2024) # Hanya perlu satu baris ini
        self.previous_hash = previous_hash
        self.kategori = kategori
        self.ref_id = ref_id
        self.anggaran = anggaran # Pastikan ini ada
        self.timestamp = time.time()
        
        self.signatures = {
            "eksekutif": None, "legislatif": None, "yudikatif": None,
            "akademisi": None, "privat": None
        }
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Mengubah signature ke format string untuk keperluan hash
        # Karena signature adalah bytes, kita ubah ke str agar bisa digabungkan
        sig_string = str({k: (v.hex() if v else None) for k, v in self.signatures.items()})
        
        payload = (str(self.index) + 
                   str(self.timestamp) + 
                   json.dumps(self.data, sort_keys=True) + 
                   self.previous_hash + 
                   sig_string)
        
        return hashlib.sha256(payload.encode()).hexdigest()

    def sign_block(self, authority, private_key):
        """Menandatangani hash blok dengan private key masing-masing pilar."""
        # Gunakan hash saat ini sebagai pesan untuk ditandatangani
        message = self.hash.encode()
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        self.signatures[authority] = signature
        # Update ulang hash karena tanda tangan baru saja ditambahkan
        self.hash = self.calculate_hash()