# Password Generator

 This generator uses the random and string library to generate a defined length of random letters, digits and symbols.

## Required libraries
Password Generator uses the following libraries:
`random`
`string`
`tkinter`
`ttkbootstrap`
`pyperclip`
`pillow`
`os`

## The Application

| Before Generation  | Upon Generation |
| ------------- | ------------- |
| ![image](https://github.com/user-attachments/assets/dd74f5ef-8af1-4331-8050-267f0145a526) | ![image](https://github.com/user-attachments/assets/524c67c7-a178-48d4-a863-b20012792b52)  |

> [!IMPORTANT]
> A strong password should be over 16 characters in length and avoid common phrases or words. That is why I use a complex randomised key.

### Creating the executable
1) Ensure you have the prerequisite libraries imported
2) `import sys`
3) Access the ```MEIPASS.py``` file. Replace the lines in the original .py file
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
