import time
import random
import threading
from pynput import keyboard
import pyautogui

# List kata-kata random (bisa diganti sesuai keinginan)
words = ["hello", "world", "python", "keyboard", "autotype", "random", "chatgpt", "fast", "code", "fun"]

typing = False  # Flag untuk mulai/berhenti mengetik

def type_random_words():
    global typing
    end_time = time.time() + 5  # 5 detik dari sekarang
    while time.time() < end_time and typing:
        word = random.choice(words)
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
    pass  # Tidak melakukan apa-apa saat tombol dilepas

# Mulai listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Tekan '/' untuk mengetik random word selama 5 detik.")
    listener.join()
