from models import Block
from database import save_block

class GoldenIndonesiaChain:
    def __init__(self):
        # Genesis block langsung dianggap sah
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        block = Block(0, {"periode": "2024", "fokus": "Genesis"}, "0")
        # Genesis otomatis ditandatangani oleh konstitusi
        for auth in block.signatures: block.sign_block(auth)
        return block

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), data, last_block.hash)
        self.chain.append(new_block)
        
        # Otomatis simpan ke database setiap ada blok baru
        save_block(new_block) 
        return new_block
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            # Tambahan: Cek apakah semua sudah tanda tangan
            if not all(current.signatures.values()):
                return False, "Blok belum ditandatangani 3 pilar!"
            if current.hash != current.calculate_hash():
                return False, "Hash tidak valid!"
        return True, "Rantai Sah & Sakral"