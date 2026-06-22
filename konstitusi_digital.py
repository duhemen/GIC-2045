# C:\gic\konstitusi_digital.py

def cek_konstitusi_luca(data_usulan):
    """
    LUCA: Landasan Utama Cita-cita Abangsa
    Setiap usulan harus merefleksikan semangat Indonesia Emas.
    """
    # Nilai-nilai dasar (Core Values)
    nilai_luca = {
        "keadilan": "Pembangunan harus merata hingga pelosok desa.",
        "keberlanjutan": "Tidak merusak lingkungan untuk generasi mendatang.",
        "kedaulatan": "Mengutamakan kemandirian teknologi dan ekonomi dalam negeri.",
        "kemanusiaan": "SDM harus menjadi subjek utama pembangunan."
    }
    
    # Simulasi AI: Mengecek apakah usulan mengandung semangat LUCA
    usulan_lower = data_usulan.lower()
    if any(kata in usulan_lower for kata in ["desa", "lingkungan", "mandiri", "sdm"]):
        return True, "Usulan sesuai dengan semangat LUCA."
    else:
        return False, "Usulan melenceng dari konstitusi LUCA."