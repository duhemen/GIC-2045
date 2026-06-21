import hashlib
import json
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        # Kita tambahkan status tanda tangan
        self.signatures = {
            "eksekutif": False,
            "legislatif": False,
            "yudikatif": False
        }
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Hash sekarang mencakup tanda tangan agar tidak bisa diubah setelah ditandatangani
        payload = str(self.index) + str(self.timestamp) + json.dumps(self.data) + \
                  self.previous_hash + json.dumps(self.signatures)
        return hashlib.sha256(payload.encode()).hexdigest()

    def sign_block(self, authority):
        if authority in self.signatures:
            self.signatures[authority] = True
            # Recalculate hash setelah tanda tangan ditambahkan
            self.hash = self.calculate_hash()