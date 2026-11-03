import modul_evaluasi

TOTAL_PERTEMUAN = 14
LEBAR_GARIS = 45


def input_angka_valid(prompt, min_val, max_val):
    """Meminta angka dalam rentang [min_val, max_val] hingga valid.
    Mengembalikan nilai bertipe float."""
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("Error: input harus berupa angka, bukan huruf/teks. Silakan ulangi.")
            continue

        if not (min_val <= nilai <= max_val):
            print(f"Warning: nilai harus antara {min_val:g} sampai {max_val:g}. Silakan ulangi.")
            continue

        return nilai


def tampilkan_hasil(nama, nim, hadir, persentase, nilai_akhir, status):
    """Menampilkan hasil evaluasi dengan format rapi."""
    garis = "=" * LEBAR_GARIS
    print(f"\n{garis}")
    print("HASIL EVALUASI KELAYAKAN ASLAB".center(LEBAR_GARIS))
    print(garis)
    print(f"{'Nama':<20}: {nama}")
    print(f"{'NIM':<20}: {nim}")
    print(f"{'Kehadiran':<20}: {hadir:g} dari {TOTAL_PERTEMUAN} pertemuan")
    print(f"{'Persentase Presensi':<20}: {persentase:.2f}%")
    print(f"{'Nilai Akhir':<20}: {nilai_akhir:.2f}")
    print(f"{'Status':<20}: {status}")
    print(garis)


def proses_kelayakan():
    """Meminta data, menghitung kelayakan, lalu menampilkan hasilnya."""
    print("\n--- Input Data Calon Asisten Laboratorium ---")
    nama = input(f"{'Nama':<26}: ").strip()
    nim = input(f"{'NIM':<26}: ").strip()
    hadir = input_angka_valid(f"{'Jumlah kehadiran (0-14)':<26}: ", 0, TOTAL_PERTEMUAN)
    tugas = input_angka_valid(f"{'Nilai Tugas (0-100)':<26}: ", 0, 100)
    ucp1 = input_angka_valid(f"{'Nilai UCP 1 (0-100)':<26}: ", 0, 100)
    ucp2 = input_angka_valid(f"{'Nilai UCP 2 (0-100)':<26}: ", 0, 100)

    persentase = modul_evaluasi.hitung_persentase_presensi(hadir, TOTAL_PERTEMUAN)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)

    tampilkan_hasil(nama, nim, hadir, persentase, nilai_akhir, status)


def main():
    """Menjalankan menu interaktif sampai pengguna memilih keluar."""
    while True:
        print("\n===== SISTEM EVALUASI ASISTEN LAB AI =====")
        print("1. Hitung Kelayakan")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print("Error: pilihan menu harus berupa angka 1 atau 2.")
            continue

        if pilihan == 1:
            proses_kelayakan()
        elif pilihan == 2:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Warning: pilihan tidak tersedia. Pilih 1 atau 2.")


if __name__ == "__main__":
    main()