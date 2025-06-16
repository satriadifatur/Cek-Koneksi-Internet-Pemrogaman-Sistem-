import os
import platform

def cek_koneksi():
    parameter = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {parameter} 8.8.8.8 > nul 2>&1" if platform.system().lower() == "windows" else f"ping {parameter} 8.8.8.8 > /dev/null 2>&1")
    return response == 0

if __name__ == "__main__":
    if cek_koneksi():
        print("✅ Terhubung ke Internet.")
    else:
        print("❌ Tidak ada koneksi Internet.")
