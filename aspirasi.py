# Simulasi AI Auditor untuk menyaring usulan
def filter_usulan(usulan):
    kata_terlarang = ["korupsi", "rusak", "jual negara"]
    # AI mengecek apakah usulan masuk akal
    for kata in kata_terlarang:
        if kata in usulan.lower():
            return False, "Usulan mengandung unsur destruktif!"
    
    if len(usulan) < 10:
        return False, "Usulan terlalu singkat, tidak informatif!"
    
    return True, "Usulan layak untuk voting publik."

# Simulasi penyimpanan hasil voting sementara
hasil_voting = {"ya": 0, "tidak": 0}

def rekam_vote(pilihan):
    if pilihan.lower() == "ya":
        hasil_voting["ya"] += 1
    elif pilihan.lower() == "tidak":
        hasil_voting["tidak"] += 1
    return hasil_voting

def cek_lolos_voting():
    # Syarat: Suara "Ya" harus lebih dari "Tidak"
    if hasil_voting["ya"] > hasil_voting["tidak"]:
        return True
    return False

def verifikasi_akademik(usulan):
    # Simulasi AI/Sistem mengecek data riset
    skor_riset = 85 # Simulasi hasil riset
    if skor_riset > 70:
        return True, "Usulan didukung oleh bukti empiris."
    return False, "Usulan kurang didukung data riset."