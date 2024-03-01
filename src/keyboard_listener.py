from pynput import keyboard
from main_window import launch_main_window

def on_activate():
    print("Shortcut CTRL+OPTION+T activated")
    launch_main_window()
    # Here you will call your function to activate the GUI

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+t'),
    on_activate
)

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
