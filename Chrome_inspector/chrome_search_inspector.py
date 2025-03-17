
import os
os.chdir('F:\python_programs\Chrome_inspector')
try:
    from pynput import keyboard
except ModuleNotFoundError:
    try:
        with open(os.path.join(os.getcwd(), 'requirements.txt')) as file:
            package = [pack.strip('\n') for pack in file.readlines()]
        for pack in package:
            os.system(f'pip install {pack}')
            # os.system('pip freeze > requirements.txt')
            from pynput import keyboard
    except FileNotFoundError:
        print('requirements.txt not found')
        os._exit(0)

BLOCKED_WORDLIST = os.path.join(os.getcwd(), 'blocked_wordlist.txt')

with open(BLOCKED_WORDLIST, 'r+') as file:
    adult_words = [word for word in file.read().split(',')]

keys_pressed = []


def on_press(key):
    try:
        keys_pressed.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            keys_pressed.append(" ")
        elif key == keyboard.Key.enter:
            keys_pressed.append("\n")
    text = ''.join(keys_pressed)
    for word in adult_words:
        if word in text:
            print(f"Adult word '{word}' detected. Shutting down...")
            keys_pressed.clear()
            # os.system("shutdown /s /f /t 0")
            return False


def main():
    while True:
        print("Starting keylogger...")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == "__main__":
    main()
