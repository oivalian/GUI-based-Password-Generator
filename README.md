# Password Generator

This is a small project I created in January 2024 using Python, Tkinter and Ttkbootstrap.
 do plan to add some other features eventually, maybe even a set of combined tools.

### Creating the executable
1) Ensure you have the prerequiste packages installed (pyperclip, tkinter, ttkbootstrap, pyinstaller)
2) ```import os```, ```import sys```
3) Access the ```MEIPASS.py``` file. Replace the lines in the original .py file.
4) Ensure the .ico file is saved in the root dir
5) Run the following command:
   
``` pyinstaller -w --onefile --icon=key.ico --add-data=key.ico:. passwordgenerator.py ```

6) Your executable will be saved under the ```./dist``` dir
   
> [!NOTE]
> Below is a helpful 'what does' on each argument

```-w``` launches program without terminal

```--onefile``` makes a single .exe file

```--icon-key=FILE``` sets the window icon

```--add-data=FILE:LOCATION``` compiles key.ico into program
