import time
import random
import threading
from pynput import keyboard
import pyautogui
import string

# Tombol-tombol yang bisa memicu aksi jika mode aktif
trigger_keys = ['m', 'l']
# Tombol untuk mengaktifkan/menonaktifkan mode
toggle_key = 'o'

# Status aktif/tidaknya mode pengetikan
typing_enabled = False

def generate_random_word(length=5):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def type_random_words():
    end_time = time.time() + 5
    while time.time() < end_time:
        word = generate_random_word(random.randint(1, 5))
        pyautogui.write(word + "", interval=0)

def on_press(key):
    global typing_enabled
    try:
        if key.char == toggle_key:
            typing_enabled = not typing_enabled
            status = "ON" if typing_enabled else "OFF"
            print(f"[TOGGLE] Mode pengetikan sekarang: {status}")
        elif typing_enabled and key.char in trigger_keys:
            threading.Thread(target=type_random_words).start()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    print(f"Tekan '{toggle_key}' untuk ON/OFF mode pengetikan.")
    print(f"Jika aktif, tekan salah satu tombol ini {trigger_keys} untuk mengetik kata acak selama 5 detik.")
    listener.join()
