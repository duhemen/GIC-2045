# C:\gic\audit_akademik.py
def verifikasi_akademik(usulan):
    # Simulasi: Cek apakah usulan relevan dengan data riset 2045
    # Dalam sistem nyata, ini akan terhubung ke database riset nasional
    kata_kunci_riset = ["infrastruktur", "digital", "ekonomi", "sdm", "teknologi"]
    
    skor_eviden = 0
    for kata in kata_kunci_riset:
        if kata in usulan.lower():
            skor_eviden += 20
            
    if skor_eviden >= 40:
        return True, f"Riset Valid (Skor Eviden: {skor_eviden}/100)"
    else:
        return False, "Usulan kurang didukung data riset empiris."