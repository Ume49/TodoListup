from tkinter import *
from tkinter import ttk
import Widget

root_window = Tk()

root_window.title("TODO ListUp forUnity")

directory_frame = ttk.Frame(root_window, padding=16).pack(side=BOTTOM)
option_frame    = ttk.Frame(root_window, padding=16).pack(side=BOTTOM)

Widget.Set_AskDirectory(frame = directory_frame)

ttk.Label(
    option_frame,
    text="エンコード"
).pack(side=LEFT)
ttk.Entry(
    option_frame,
).pack(side=LEFT)

# 使用予定
# list = Search_TODO.SearchString_behindTODO("directory")
# listには表示すべき文字列リストが返ってくる

root_window.mainloop()