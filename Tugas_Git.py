data_panen = {
    'lokasi1': {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    'lokasi2': {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    'lokasi3': {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    'lokasi4': {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    'lokasi5': {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}

# Soal no 1: Menampilkan semua data
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    print(f"Hasil Panen: {data['hasil_panen']}")
    print()

# Soal no 2: Menampilkan hasil panen jagung di lokasi 2
print("Hasil panen jagung di lokasi 2:", data_panen['lokasi2']['hasil_panen']['jagung'])
print()

# Soal no 3: Menampilkan nama lokasi 3
print("Nama lokasi 3:", data_panen['lokasi3']['nama_lokasi'])
print()

# Soal no 4: Menghitung total hasil panen padi dan kedelai
total_padi = 0
total_kedelai = 0

for lokasi, data in data_panen.items():
    total_padi += data['hasil_panen']['padi']
    total_kedelai += data['hasil_panen']['kedelai']

print(f"Total hasil panen padi: {total_padi} kg")
print(f"Total hasil panen kedelai: {total_kedelai} kg")
print()

# Soal no 5: Jumlah hasil panen per lokasi
padi_per_lokasi = {}
kedelai_per_lokasi = {}

for lokasi, data in data_panen.items():
    padi_per_lokasi[lokasi] = data['hasil_panen']['padi']
    kedelai_per_lokasi[lokasi] = data['hasil_panen']['kedelai']

print("Jumlah Hasil Panen Padi Per Lokasi:")
for lokasi, padi in padi_per_lokasi.items():
    print(f"{lokasi}: {padi} kg")

print("\nJumlah Hasil Panen Kedelai Per Lokasi:")
for lokasi, kedelai in kedelai_per_lokasi.items():
    print(f"{lokasi}: {kedelai} kg")
print()

# Soal no 6: Pemeriksaan kondisi lokasi
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
