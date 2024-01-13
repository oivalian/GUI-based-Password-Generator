# Password Generator

Generates a random string of chars from a standard keyboard based on user input (Max 30 chars)

## Required libraries
Password Generator uses the following libraries:
`random`
`string`
`tkinter`
`ttkbootstrap`
`pyperclip`
`pillow`
`sys`
`os`

### Creating the executable
1) Ensure you have the prerequisite libraries imported
2) Access the ```MEIPASS.py``` file. Replace the lines in the original .py file
3) Ensure the .ico file is saved in the root dir
4) Run the following command:
   
``` pyinstaller -w --onefile --icon=key.ico --add-data=key.ico:. passwordgenerator.py ```

6) Your executable will be saved under the ```./dist``` dir
   
> [!NOTE]
> Below is a helpful 'what does' on each argument

```-w``` launches program without terminal

```--onefile``` makes a single .exe file

```--icon-key=FILE``` sets the window icon

```--add-data=FILE:LOCATION``` compiles key.ico into program
