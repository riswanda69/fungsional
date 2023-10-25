# Data input dalam format "minggu hari jam menit"
data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk mengambil hanya nilai integer dari setiap elemen dalam data
def ambil_integer(data):
    integer_data = []
    for item in data:
        # Membagi data menjadi komponen-komponen waktu
        components = item.split()
        
        # Menggunakan filter untuk mengambil hanya nilai integer dari setiap komponen
        int_values = list(filter(str.isdigit, components))
        
        integer_data.append(int_values)
    
    return integer_data

# Mengambil hanya nilai integer dari data dan mencetak hasilnya
hasil_integer = ambil_integer(data)
for item in hasil_integer:
    print(item)
