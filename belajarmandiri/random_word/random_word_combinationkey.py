import time
import random
import threading
from pynput import keyboard
import pyautogui
import string

# Variabel untuk melacak status tombol modifier
ctrl_pressed = False
alt_pressed = False

# Fungsi untuk membuat kata acak
def generate_random_word(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

# Fungsi untuk mengetik selama 5 detik
def type_random_words():
    end_time = time.time() + 4
    while time.time() < end_time:
        word = generate_random_word(random.randint(1, 5))
        pyautogui.write(word + "", interval=0)

# Handler untuk penekanan tombol
def on_press(key):
    global ctrl_pressed, alt_pressed
    try:
        # Cek tombol modifier
        if key in [keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            ctrl_pressed = True
        elif key in [keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r]:
            alt_pressed = True
        elif key == keyboard.KeyCode.from_char('W'):
            if ctrl_pressed and alt_pressed:
                threading.Thread(target=type_random_words).start()
    except AttributeError:
        pass

# Handler untuk pelepasan tombol
def on_release(key):
    global ctrl_pressed, alt_pressed
    try:
        if key in [keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            ctrl_pressed = False
        elif key in [keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r]:
            alt_pressed = False
    except AttributeError:
        pass

# Konfigurasi listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Tekan dan TAHAN Ctrl + Alt, lalu tekan W untuk mengaktifkan...")
    listener.join()