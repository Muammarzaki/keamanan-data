from stegano import lsb
import os

def get_image_path():
    while True:
        image_path = input("Masukkan path gambar (e.g. D:\KAUSAR R\PAS POTO\PAS POTO 2.jpg: ")
        if os.path.exists(image_path):
            return image_path
        else:
            print("Path gambar tidak valid. Silakan coba lagi.")


def hide_message():
    image_path = get_image_path()
    message = input("Masukkan pesan yang ingin Anda sematkan: ")
    secret = lsb.hide(image_path, message)
    save_path = input("Masukkan path untuk menyimpan gambar stegano: ")
    try:
        secret.save(save_path)
        print(f"Pesan berhasil disematkan dalam gambar stegano: {save_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan gambar stegano: {e}")


def show_message():
    img_path = get_image_path()
    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            print(f"Pesan yang disematkan dalam gambar stegano: {clear_message}")
        else:
            print("Pesan tidak ditemukan dalam gambar stegano.")
    except Exception as e:
        print(f"Gagal mendapatkan pesan: {e}")


def main():
    while True:
        print("\nSteganography Tool - Terminal Version")
        print("1. Sembunyikan pesan")
        print("2. Tampilkan pesan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("Keluar dari program")
            break
        else:
            print("Opsi tidak valid")


if __name__ == "__main__":
    main()
