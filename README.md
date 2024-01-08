_+_+_+_+_+_+_+_+_+_
Password Generator
_+_+_+_+_+_+_+_+_+_

This is a small project I created in January 2024 using Python, Tkinter and Ttkbootstrap.
 do plan to add some other features eventually, maybe even a set of combined tools.

Enjoy. (let me know if you have any recommendations!)

**Creating an exe (My assumption is that you understand how this works):**
1) Ensure you havew the prerequiste packages installed (pyperclip, tkinter, ttkbootstrap, pyinstaller)
2) Access the MEIPASS .py file. Replace the lines in the original .py file.
3) Ensure the .ico file is saved in the root dir
4) Run the following command in SH or CMD:
   _pyinstaller -w --onefile --icon=key.ico --add-data=key.ico:. passwordgenerator.py_
5) Your executable will be saved under the ./dist dir
   
**cmd notes:**
_-w_ launches program without terminal
_--onefile_ makes a single .exe file
_--icon-key=FILE_ sets the window icon
_--add-data=FILE:LOCATION_ compiles key.ico into program.
