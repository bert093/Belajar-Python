import time
import random
import threading
from pynput import keyboard
import pyautogui
import string

pyautogui.FAILSAFE = False

trigger_keys = ['m', 'l']
toggle_key = 'o'

typing_enabled = False
is_typing = False  # Flag untuk mencegah typing dobel

def generate_random_word(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def type_random_words():
    global is_typing # flag is_typing untuk mengecek apakah proses pengetikan sedang berjalan.
    is_typing = True
    end_time = time.time() + 4  # ⏱️ hanya 4 detik
    while time.time() < end_time:
        word = generate_random_word(random.randint(1, 5))
        pyautogui.write(word + "", interval=0)
    is_typing = False  # 🔁 reset agar bisa dijalankan lagi

def on_press(key):
    global typing_enabled, is_typing
    try:
        if key.char == toggle_key:
            typing_enabled = not typing_enabled
            status = "ON" if typing_enabled else "OFF"
            print(f"[TOGGLE] Mode pengetikan sekarang: {status}")
        elif typing_enabled and key.char in trigger_keys and not is_typing:
            threading.Thread(target=type_random_words).start()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    print(f"Tekan '{toggle_key}' untuk ON/OFF mode pengetikan.")
    print(f"Jika aktif, tekan salah satu tombol ini {trigger_keys} untuk mulai mengetik selama 4 detik.")
    listener.join()
