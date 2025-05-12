import time
import random
import threading
from pynput import keyboard
import pyautogui
import string

typing = False  # Flag untuk mulai/berhenti mengetik

def generate_random_word(length=5):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def type_random_words():
    global typing
    end_time = time.time() + 5  # 5 detik dari sekarang
    while time.time() < end_time and typing:
        word = generate_random_word(random.randint(3, 8))  # Panjang kata antara 3-8
        pyautogui.write(word + " ", interval=0.05)
        time.sleep(0.2)

def on_press(key):
    global typing
    try:
        if key.char == "/":
            if not typing:
                typing = True
                threading.Thread(target=type_random_words).start()
    except AttributeError:
        pass

def on_release(key):
    pass

# Mulai listener keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Tekan '/' untuk mengetik random word (tanpa list) selama 5 detik.")
    listener.join()
