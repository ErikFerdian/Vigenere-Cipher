# Fungsi untuk enkripsi dengan Vigenère Cipher
def encrypt(plaintext, key):
    result = []
    key = key.upper()
    plaintext = plaintext.upper()
    key_length = len(key)
    key_index = 0   # counter manual untuk key
    
    for char in plaintext:
        if char.isalpha():  # hanya huruf diproses
            shift = ord(key[key_index % key_length]) - ord('A')
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)  # karakter non-huruf tetap
    
    return "".join(result)


# Fungsi untuk dekripsi dengan Vigenère Cipher
def decrypt(ciphertext, key):
    result = []
    key = key.upper()
    ciphertext = ciphertext.upper()
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    
    return "".join(result)


# --- Program Utama ---
plaintext = input("Masukkan teks (plaintext): ")
key = input("Masukkan key: ")
mode = input("Pilih mode (enkripsi/dekripsi): ").lower()

if mode == "enkripsi":
    hasil = encrypt(plaintext, key)
    print("Hasil enkripsi:", hasil)
elif mode == "dekripsi":
    hasil = decrypt(plaintext, key)
    print("Hasil dekripsi:", hasil)
else:
    print("Mode tidak valid! Pilih 'enkripsi' atau 'dekripsi'.")
