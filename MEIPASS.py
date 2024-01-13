def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# window|root
root = ttk.Window(themename='darkly')
iconPath = resource_path('key.ico')
root.iconbitmap(iconPath)
root.title('Password Generator')
root.geometry('700x600')
root.maxsize(700, 650)
root.minsize(700, 650)


'''
replace lines 25-31 in passwordgenerator.py with the above code

run command:
pyinstaller -w --onefile --icon=key.ico --add-data=key.ico:. passwordgenerator.py
'''
