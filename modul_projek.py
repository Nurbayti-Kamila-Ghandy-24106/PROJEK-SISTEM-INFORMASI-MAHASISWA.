# PROJEK SISTEM INFORMASI MAHASISWA SEDERHANA
# =========================================
# Projek ini menggunakan fungsi-fungsi Python
# untuk mengelola data mahasiswa
# =========================================


# Fungsi 1: Menampilkan identitas mahasiswa
def tampilkan_mahasiswa(nama, nim, jurusan):
    print("Data Mahasiswa 1")
    print(f"Nama    : {nama}")
    print(f"NIM     : {nim}")
    print(f"Jurusan : {jurusan}")


tampilkan_mahasiswa("Gita Sari", "121055520124101", "Informatika")


# Fungsi 2: Menghitung nilai akhir
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai_akhir

nilai = hitung_nilai(95, 93, 95)
print(f"Nilai Akhir Mahasiswa: {nilai}")


# Fungsi 3: Menentukan grade
def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 75:
        return "C"
    else:
        return "D"

print(f"Grade Mahasiswa: {tentukan_grade(nilai)}")



# Fungsi 4: Cek kelulusan
def cek_kelulusan(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "LULUS"
    else:
        return "TIDAK LULUS"

status = cek_kelulusan(tentukan_grade(nilai))
print(f"Status Kelulusan: {status}")

# Akhir Program



#-------------------------------
print("-"*50)


# Fungsi 1: Menampilkan identitas mahasiswa
def tampilkan_mahasiswa(nama, nim, jurusan):
    print("Data Mahasiswa 2")
    print(f"Nama    : {nama}")
    print(f"NIM     : {nim}")
    print(f"Jurusan : {jurusan}")

tampilkan_mahasiswa("nurbayti Kamila Ghandy","121055520124106","Informatika")




# Fungsi 2: Menghitung nilai akhir
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai_akhir

nilai = hitung_nilai(99, 90, 95)
print(f"Nilai Akhir Mahasiswa: {nilai}")


# Fungsi 3: Menentukan grade
def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 75:
        return "C"
    else:
        return "D"

print(f"Grade Mahasiswa: {tentukan_grade(nilai)}")


# Fungsi 4: Cek kelulusan
def cek_kelulusan(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "LULUS"
    else:
        return "TIDAK LULUS"

status = cek_kelulusan(tentukan_grade(nilai))
print(f"Status Kelulusan: {status}")


#-------------------------------
print("-"*50)


# Fungsi 1: Menampilkan identitas mahasiswa
def tampilkan_mahasiswa(nama, nim, jurusan):
    print("Data Mahasiswa 3")
    print(f"Nama    : {nama}")
    print(f"NIM     : {nim}")
    print(f"Jurusan : {jurusan}")

tampilkan_mahasiswa("Sofia Pratiwi L.R","121055520124095","Informatika")




# Fungsi 2: Menghitung nilai akhir
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai_akhir

nilai = hitung_nilai(90, 93, 95)
print(f"Nilai Akhir Mahasiswa: {nilai}")


# Fungsi 3: Menentukan grade
def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 75:
        return "C"
    else:
        return "D"

print(f"Grade Mahasiswa: {tentukan_grade(nilai)}")


# Fungsi 4: Cek kelulusan
def cek_kelulusan(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "LULUS"
    else:
        return "TIDAK LULUS"

status = cek_kelulusan(tentukan_grade(nilai))
print(f"Status Kelulusan: {status}")

# Akhir Program
