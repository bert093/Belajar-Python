import time
import random
import threading
from pynput import keyboard
import pyautogui
import string
#* Download terlebih dahulu library pyautogui dan pynput:
#* contoh: pip install pynput pyautogui

trigger_keys = ['m, l']

# Fungsi untuk membuat kata acak
def generate_random_word(length):
    characters = string.ascii_lowercase + string.digits #* string.ascii= semua huruf a-z huruf kecil. ///// string.digits= 0-9
    return ''.join(random.choices(characters, k=length)) #* pilih n karakter acak dari kumpulan karakter

# Fungsi untuk mengetik selama 5 detik nonstop
def type_random_words():
    end_time = time.time() + 4  # batas waktu 5 detik
    while time.time() < end_time:
        word = generate_random_word(random.randint(1, 5)) #* membuat panjang kata bervariasi antara 3 sampai 8 karakter
        pyautogui.write(word + "", interval=0)  #* Tidak ada delay antar huruf,
        #* memberikan tanda petik " " sehingga ada jarak antara karakternya (spasi)

# Listener keyboard

def on_press(key):
    try:
        if key.char in trigger_keys:
            threading.Thread(target=type_random_words).start()
    except AttributeError:
        pass
# def on_press(key):
#     try:
#         if key.char in trigger_keys:
#             threading.Thread(target=type_random_words).start()
#     except AttributeError:
#         pass # Ini buat abaikan tombol khusus seperti Shift, Ctrl, dll

# Jalankan listener
with keyboard.Listener(on_press=on_press) as listener: #* tidak ada on_release sehingga bisa diulang.
    print("Tekan 'm' atau 'l' untuk mengetik kata acak selama 4 detik (tanpa delay dan bisa diulang).")
    listener.join()