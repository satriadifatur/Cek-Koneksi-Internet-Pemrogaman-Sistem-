import socket

def cek_koneksi(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

if __name__ == "__main__":
    if cek_koneksi():
        print("✅ Terhubung ke Internet.")
    else:
        print("❌ Tidak ada koneksi Internet.")
