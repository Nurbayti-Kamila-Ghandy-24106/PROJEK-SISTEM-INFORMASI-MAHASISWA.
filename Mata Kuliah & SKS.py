
def tampilkan_matkul(matkul, sks):
    print("Mata Kuliah Diambil")
    print(f"Nama Mata Kuliah : {matkul}")
    print(f"Jumlah SKS      : {sks}")

def hitung_total_sks(sks_list):
    return sum(sks_list)

# Data mata kuliah mahasiswa
mata_kuliah = ["Pemograman Berorientasi Objek", "Basis Data", "Desain Web"]
sks = [3, 3, 3]

# Menampilkan mata kuliah
for i in range(len(mata_kuliah)):
    tampilkan_matkul(mata_kuliah[i], sks[i])
    print("-" * 25)

total_sks = hitung_total_sks(sks)
print(f"Total SKS yang diambil : {total_sks}")

def cek_beban_sks(total):
    if total > 24:
        return "Beban SKS Terlalu Banyak"
    else:
        return "Beban SKS Normal"

print(f"Keterangan : {cek_beban_sks(total_sks)}")

print("\n" + "=" * 50 + "\n")


# Akhir Program
