from tkinter import ttk
from tkinter import *

root = Tk()
root.geometry("560x380")
root.title("Lyric Getter")

label = Label(root, text="Hi, please enter a lyric", font=("Courier 22"))
label.pack(pady=25)

lyric_entry_box = Entry(root, width=50)
lyric_entry_box.focus_set()
lyric_entry_box.pack(pady=10)


def print_button_clicked():
    print("Button has been clicked")
    print(lyric_entry_box.get())
    lyric_entry_box.delete(0, END)


ttk.Button(root, text="Find Song", width=20,
           command=print_button_clicked).pack(pady=20)

root.mainloop()  # 560 x 380
