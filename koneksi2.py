import requests

def cek_koneksi():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

if __name__ == "__main__":
    if cek_koneksi():
        print("✅ Terhubung ke Internet.")
    else:
        print("❌ Tidak ada koneksi Internet.")
