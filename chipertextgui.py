import tkinter as tk
from tkinter import messagebox

from caesar import Caesar

class Caesar:
    def __init__(self, shift):
        self.shift = shift

    def encryption(self, plain_text):
        cipher_text = ""
        for char in plain_text:
            if char.isupper():
                cipher_text += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                cipher_text += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                cipher_text += char
        return cipher_text

    def decryption(self, cipher_text):
        plain_text = ""
        for char in cipher_text:
            if char.isupper():
                plain_text += chr((ord(char) - self.shift - 65) % 26 + 65)
            elif char.islower():
                plain_text += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                plain_text += char
        return plain_text


def main():
    with Caesar(3) as cs:
        print("Selamat datang!")
        plain_text = input("Masukkan teks asli (plain text): ")
        shift = int(input("Masukkan nilai pergeseran (1-25): "))

        # Panggil fungsi enkripsi
        cipher_text = cs.encryption(plain_text)
        print("Teks terenkripsi: ", cipher_text)

        # Panggil fungsi deskripsi
        deskripsi_text = cs.decryption(cipher_text)
        print("Teks terdekripsi: ", deskripsi_text)


def process_text():
    shift = shift_entry.get()

    # Validate the shift input
    if not shift.isdigit():
        messagebox.showerror("Input Error", "Shift must be a number.")
        return

    shift = int(shift)
    algo = Caesar(shift)
    # Check mode: encryption or decryption
    if mode_var.get() == "enc":
        text = encrypted_text.get("1.0", "end-1c")
        result = algo.encryption(text)
        decrypted_text.delete("1.0", "end")
        decrypted_text.insert("1.0", f"{result}")
    elif mode_var.get() == "dec":
        text = decrypted_text.get("1.0", "end-1c")
        result = algo.decryption(text)
        encrypted_text.delete("1.0", "end")
        encrypted_text.insert("1.0", f"{result}")


# Create the main window
root = tk.Tk()
root.title("Encryption and Decryption")
root.configure(bg="#87CEEB")  # Sky blue background color
root.resizable(0, 0)

#  input/output area
frame = tk.Frame(root, bg="#87CEEB")
frame.grid(row=0, column=0, padx=20, pady=20)

# Label and entry for shift input
tk.Label(frame, text="Enter Shift Value:", bg="#87CEEB", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10,
                                                                                  sticky="w")
shift_entry = tk.Entry(frame, font=("Arial", 12), width=5)
shift_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

#  text input and output
text_frame = tk.Frame(root, bg="#87CEEB")
text_frame.grid(row=1, column=0, padx=20, pady=20)

# Text area for input
tk.Label(text_frame, text="Decrypted Text:", bg="#87CEEB", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10,
                                                                                    sticky="w")
encrypted_text = tk.Text(text_frame, height=10, width=50, font=("Arial", 12), wrap="word")
encrypted_text.grid(row=1, column=0, padx=10, pady=10)

mode_var = tk.StringVar(value="enc")


# Arrow separator for encryption and decryption
def set_arrow():
    if mode_var.get() == "enc":
        arrow_label = tk.Label(text_frame, text=">", bg="#87CEEB", font=("Arial", 20))
    else:
        arrow_label = tk.Label(text_frame, text="<", bg="#87CEEB", font=("Arial", 20))
    arrow_label.grid(row=1, column=1, padx=10, pady=10)


arrow_label = tk.Label(text_frame, text=">", bg="#87CEEB", font=("Arial", 20))
arrow_label.grid(row=1, column=1, padx=10, pady=10)

# Mode selection (Encryption or Decryption)
enc_radio = tk.Radiobutton(frame, text="Encrypt", variable=mode_var, value="enc", bg="#87CEEB", font=("Arial", 12),
                           command=set_arrow)
enc_radio.grid(row=1, column=0, padx=10, pady=10, sticky="w")
dec_radio = tk.Radiobutton(frame, text="Decrypt", variable=mode_var, value="dec", bg="#87CEEB", font=("Arial", 12),
                           command=set_arrow)
dec_radio.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Text area for output
tk.Label(text_frame, text="Encrypted Text:", bg="#87CEEB", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10,
                                                                                    sticky="w")
decrypted_text = tk.Text(text_frame, height=10, width=50, font=("Arial", 12), wrap="word")
decrypted_text.grid(row=1, column=2, padx=10, pady=10)

# Button to process encryption or decryption
process_button = tk.Button(root, text="Process", command=process_text, font=("Arial", 12), bg="#4682B4", fg="white")
process_button.grid(row=2, column=0, padx=20, pady=20)

# Run the application
root.mainloop()
