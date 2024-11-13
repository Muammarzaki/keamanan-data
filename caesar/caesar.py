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


if __name__ == '__main__':
    main()
