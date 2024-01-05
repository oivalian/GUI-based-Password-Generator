import random as r
import string as st
import tkinter as tk
import ttkbootstrap as ttk
import pyperclip as pc
from PIL import ImageTk, Image
import os

chars = st.ascii_letters + st.digits + st.punctuation


def generator():
    try:
        password = ''.join(r.choice(chars) for _ in range(password_length.get()))   # This will concatenate the loop.
        output_string.set(password[:30])
        output_button.pack(side='bottom')     # packs copy button and makes visible
    except tk.TclError:     # error if value not int return false
        return False


def copy_to_clipboard():
    pc.copy(output_string.get())


# window|root
root = ttk.Window(themename='darkly')
root.iconbitmap('key.ico')
root.title('Password Generator')
root.geometry('700x600')
root.maxsize(700, 650)
root.minsize(700, 650)


# title
title_frame = ttk.Frame(master=root)
title_img = ImageTk.PhotoImage(Image.open("key.ico").resize((150, 150)))
img_label = ttk.Label(master=title_frame, image=title_img)
title_label = ttk.Label(master=title_frame, text='Password Generator', font='Verdana 14 bold')
img_label.pack(side='top')
title_label.pack()
title_frame.pack(pady=50)

# input area
input_frame = ttk.Frame(master=root)
password_length = tk.IntVar()
length_label = ttk.Label(master=input_frame, text='  Password length:')
input_field = ttk.Entry(master=input_frame, textvariable=password_length, width=22)
button_action = ttk.Button(master=input_frame, text='Generate', command=generator)
prompt_label = ttk.Label(master=input_frame, text='Recommended Minimum: 15\nMax: 30')
length_label.grid(row=0, column=0, sticky='w')
input_field.grid(row=1, column=0, padx=10, pady=10)
button_action.grid(row=1, column=1)
prompt_label.grid(row=2, column=0)
input_frame.pack(pady=10)


# output
output_frame = ttk.Frame(master=root)
output_string = tk.StringVar()
output_label = ttk.Label(master=output_frame, text='Output', font='Helvetica 16', textvariable=output_string)
output_button = ttk.Button(master=output_frame, text='Copy to Clipboard', command=copy_to_clipboard, width=30)
output_button.pack_forget()     # makes button invisible initially
output_label.pack(pady=20, padx=10)
output_frame.pack(pady=10, padx=10)


# main
root.mainloop()
