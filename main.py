from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.simpledialog import askfloat

root_window = Tk()

root_window.title("TODO ListUp forUnity")

frame = ttk.Frame(root_window, padding=16).pack()

ttk.Label(
    frame,
    text    = "root"
).pack(side = LEFT)

entry=ttk.Entry(
    frame

).pack(side = LEFT)

ttk.Button(
    frame,
    text    = "..."
).pack(side = LEFT)

# 使用予定
# list = Search_TODO.SearchString_behindTODO("directory")
# listには表示すべき文字列リストが返ってくる

root_window.mainloop()