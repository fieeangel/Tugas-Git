data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

def print_harvest_summary(data):
    """Menampilkan ringkasan hasil panen untuk semua lokasi"""
    print(" Soal Nomor 1 ")
    for lokasi, info in data.items():
        print(f"Lokasi {info['nama_lokasi']}\nHasil Panen:")
        for komoditas, jumlah in info['hasil_panen'].items():
            print(f"  {komoditas.capitalize()}: {jumlah}")
        print()

def print_specific_location(data, lokasi_id):
    """Menampilkan hasil panen untuk lokasi tertentu"""
    print(f"\n Soal Nomor 2 ({lokasi_id}) ")
    if lokasi_id in data:
        info = data[lokasi_id]
        print(f"Lokasi {info['nama_lokasi']}\nHasil Panen:")
        for komoditas, jumlah in info['hasil_panen'].items():
            print(f"  {komoditas.capitalize()}: {jumlah}")
    else:
        print(f"Lokasi {lokasi_id} tidak ditemukan.")
    print()

def print_location_name(data, lokasi_id):
    """Menampilkan nama lokasi untuk ID tertentu"""
    print("\n Soal Nomor 3 ")
    if lokasi_id in data:
        print(f"Nama Lokasi dari {lokasi_id} adalah {data[lokasi_id]['nama_lokasi']}")
    else:
        print(f"Lokasi {lokasi_id} tidak ditemukan.")
    print()

def print_total_harvest(data):
    """Menghitung total hasil panen untuk semua lokasi"""
    print("\nIni Nomor 4 ")
    total_padi = sum(info['hasil_panen']['padi'] for info in data.values())
    total_kedelai = sum(info['hasil_panen']['kedelai'] for info in data.values())
    print(f"Hasil Panen Total - Padi: {total_padi}, Kedelai: {total_kedelai}\n")

def print_all_locations(data):
    """Menampilkan hasil panen untuk semua lokasi dalam format baru"""
    print(" Nomor 5 ")
    for lokasi, info in data.items():
        print(f"Lokasi {info['nama_lokasi']}")
        for komoditas, jumlah in info['hasil_panen'].items():
            print(f"  {komoditas.capitalize()}: {jumlah}")
        print()

def print_attention_needed(data):
    """Menandai lokasi yang membutuhkan perhatian khusus"""
    print(" Nomor 6 ")
    for lokasi, info in data.items():
        padi = info['hasil_panen']['padi']
        jagung = info['hasil_panen']['jagung']
        status = "memerlukan perhatian khusus" if padi > 1300 or jagung > 800 else "dalam kondisi baik"
        print(f"Lokasi {info['nama_lokasi']} {status}")
    print()

def harvest_list(data):
    print_harvest_summary(data)
    print_specific_location(data, "lokasi2")
    print_location_name(data, "lokasi3")
    print_total_harvest(data)
    print_all_locations(data)
    print_attention_needed(data)

harvest_list(data_panen)
