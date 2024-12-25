Nama  : Muammar Zaki \
NIM   : 220705045

Struktur File dalam Repo
```
/ --.
    |-- chipergui.py
    |-- desgui.py
    |-- enigmagui.py
    |-- steganogui.py
    |-- README.md
    
``` 

### Penjelasan singkat dari file di atas:

1. **chipergui.py**:  
   GUI untuk melakukan enkripsi dan dekripsi teks menggunakan algoritma cipher sederhana seperti **Caesar Cipher**. Metode mencakup penggeseran huruf, penggantian karakter berdasarkan kunci, dan operasi modular.

2. **desgui.py**:  
   GUI untuk implementasi algoritma **DES (Data Encryption Standard)**. Metode mencakup pembagian data menjadi blok 8-bit atau per karakter untuk menghasilkan ciphertext.

3. **enigmagui.py**:  
   GUI untuk simulasi mesin **Enigma**. Metode meliputi pengaturan rotor, reflektor, dan plugboard untuk mengenkripsi dan mendekripsi teks menggunakan logika rotasi rotor dan substitusi karakter.

4. **steganogui.py**:  
   GUI untuk steganografi. Metode umum seperti **Least Significant Bit (LSB)** digunakan untuk menyembunyikan data dalam media digital (misalnya, mengganti bit terakhir piksel gambar dengan data pesan).

### Cara menjalankannya
```shell
python <nama file>
```