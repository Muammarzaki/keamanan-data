import tkinter as tk
from tkinter import messagebox


def encrypt_text():
    plain_text = entry_plain.get()
    key = entry_key.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key harus berupa angka!")
        return

    encrypted = ''.join(chr((ord(char) + int(key)) % 256) for char in plain_text)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encrypted)


def decrypt_text():
    encrypted_text = entry_plain.get()
    key = entry_key.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key harus berupa angka!")
        return

    decrypted = ''.join(chr((ord(char) - int(key)) % 256) for char in encrypted_text)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted)


window = tk.Tk()
window.title("DES GUI")

label_plain = tk.Label(window, text="Input Text:")
label_plain.grid(row=0, column=0, padx=10, pady=5)
entry_plain = tk.Entry(window, width=30)
entry_plain.grid(row=0, column=1, padx=10, pady=5)

label_key = tk.Label(window, text="Key:")
label_key.grid(row=1, column=0, padx=10, pady=5)
entry_key = tk.Entry(window, width=30)
entry_key.grid(row=1, column=1, padx=10, pady=5)

label_result = tk.Label(window, text="Result:")
label_result.grid(row=2, column=0, padx=10, pady=5)
entry_result = tk.Entry(window, width=30)
entry_result.grid(row=2, column=1, padx=10, pady=5)

button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_text)
button_encrypt.grid(row=3, column=0, padx=10, pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_text)
button_decrypt.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
