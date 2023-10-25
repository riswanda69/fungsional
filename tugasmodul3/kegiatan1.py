def konversi(minggu=0, hari=0, jam=0, menit=0):
    return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)

# Data input dalam format "minggu hari jam menit"
data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk mengkonversi data menjadi jumlah menit
def konversi_data(data):
    hasil_konversi = []
    for item in data:
        # Membagi data menjadi komponen-komponen waktu
        components = item.split()
        
        # Mengambil nilai dari masing-masing komponen
        minggu = int(components[0])
        hari = int(components[2])
        jam = int(components[4])
        menit = int(components[6])
        
        # Menghitung total menit menggunakan fungsi konversi
        total_menit = konversi(minggu, hari, jam, menit)
        hasil_konversi.append(total_menit)
    
    return hasil_konversi

# Mengkonversi data dan mencetak hasilnya
hasil_konversi = konversi_data(data)
print(hasil_konversi)