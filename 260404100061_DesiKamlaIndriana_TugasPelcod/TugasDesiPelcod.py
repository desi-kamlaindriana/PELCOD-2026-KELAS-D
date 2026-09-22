print("=== Sistem Penilaian dan Kelulusan Mahasiswa ===")
Nama_peserta = (input("Nama_peserta = "))
Nilai_tugas = float (input("Nilai_tugas = "))
Nilai_quiz = float (input("Nilai_quiz = "))
Nilai_ujian = float (input("Nilai_ujian = "))
Kehadiran = float (input("Kehadiran = "))
Bobot_Nilai_tugas = 30 / 100
Bobot_Nilai_quiz = 20 / 100
Bobot_Nilai_ujian = 50 / 100
Nilai_akhir = (Nilai_tugas * Bobot_Nilai_tugas ) + (Nilai_quiz * Bobot_Nilai_quiz) + (Nilai_ujian * Bobot_Nilai_ujian)
print("Nilai_akhir =", Nilai_akhir)
if Kehadiran < 75:
    print("Status = Tidak Lulus hihi")
elif Nilai_akhir >= 85 and Kehadiran >= 80:
    print("Status = Lulus dengan Predikat A") 
elif Nilai_akhir >= 75 and Kehadiran >= 80:
    print("Status = Lulus dengan Predikat B")
elif Nilai_akhir >= 65 and Kehadiran >= 75:
    print("Status = Lulus dengan Predikat C")  
else:
     print("Status = Tidak Lulus")
     

