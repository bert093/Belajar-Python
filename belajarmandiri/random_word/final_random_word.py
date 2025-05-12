import time
import random
import threading
from pynput import keyboard
from pynput.keyboard import GlobalHotKeys
import pyautogui
import string

# Fungsi untuk membuat kata acak
def generate_random_word(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

# Fungsi untuk mengetik selama 4 detik
def type_random_words():
    end_time = time.time() + 4
    while time.time() < end_time:
        word = generate_random_word(random.randint(1, 5))
        pyautogui.write(word + "", interval=0)

# Fungsi callback untuk hotkey
def on_activate():
    threading.Thread(target=type_random_words).start()

# Konfigurasi hotkey
hotkey_combination = '<ctrl>+<alt>+<shift>+w'
hotkeys = GlobalHotKeys({hotkey_combination: on_activate}) # Menggunakan GlobalHotKeys yang lebih andal untuk deteksi kombinasi tombol

# Jalankan listener
print("Tekan Ctrl+Alt+Shift+W untuk memulai...")
try:
    hotkeys.start()
    hotkeys.join()
except KeyboardInterrupt:
    hotkeys.stop()