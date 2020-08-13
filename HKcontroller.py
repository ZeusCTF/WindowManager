from pynput import keyboard
from pynput.keyboard import Key, Listener
from subprocess import Popen, PIPE
from UserInput import InputWindow


def HK_controller():
    def on_activate():
        x = InputWindow()

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(keyboard.HotKey.parse('<cmd>+<enter>'), on_activate)

    with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
        l.join()

    def on_release(key):
        if key == Key.esc:
            return False
    on_release()

HK_controller()


