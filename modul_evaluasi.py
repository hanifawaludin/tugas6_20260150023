BATAS_LULUS = 75.0  # batas minimum presensi (%) dan nilai akhir


def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Mengembalikan persentase kehadiran (0-100)."""
    return (hadir / total_pertemuan) * 100


def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Mengembalikan nilai akhir: Tugas 20%, UCP 1 40%, UCP 2 40%."""
    return (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)


def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Mengembalikan status kelayakan calon asisten laboratorium."""
    if persentase_presensi < BATAS_LULUS:
        return "DITOLAK (Kehadiran di bawah 75%)"
    if nilai_akhir >= BATAS_LULUS:
        return "DITERIMA (Memenuhi Syarat)"
    return "DITOLAK (Nilai Akhir Kurang)"