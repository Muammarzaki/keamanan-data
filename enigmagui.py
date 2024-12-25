import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os


def get_image_path():
    file_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if file_path:
        return file_path
    else:
        messagebox.showerror("Error", "Tidak ada gambar yang dipilih!")
        return None


def save_image_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    return save_path


def hide_message():
    image_path = get_image_path()
    if image_path:
        message = message_entry.get()
        if message:
            secret = lsb.hide(image_path, message)
            save_path = save_image_path()
            if save_path:
                try:
                    secret.save(save_path)
                    messagebox.showinfo("Sukses", f"Pesan berhasil disematkan dalam gambar: {save_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan gambar: {e}")
        else:
            messagebox.showwarning("Input pesan", "Masukkan pesan yang ingin disematkan!")


def show_message():
    image_path = get_image_path()
    if image_path:
        try:
            secret_message = lsb.reveal(image_path)
            if secret_message:
                messagebox.showinfo("Pesan ditemukan", f"Pesan yang disematkan: {secret_message}")
            else:
                messagebox.showinfo("Pesan tidak ditemukan", "Pesan tidak ditemukan dalam gambar.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mendapatkan pesan: {e}")


# Set up the main window
root = tk.Tk()
root.title("Steganography GUI")

# Set up the UI elements
message_label = tk.Label(root, text="Masukkan pesan untuk disematkan:")
message_label.pack(pady=10)

message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=10)

hide_button = tk.Button(root, text="Sembunyikan Pesan", command=hide_message)
hide_button.pack(pady=10)

show_button = tk.Button(root, text="Tampilkan Pesan", command=show_message)
show_button.pack(pady=10)

exit_button = tk.Button(root, text="Keluar", command=root.quit)
exit_button.pack(pady=10)

# Run the main window loop
root.mainloop()
