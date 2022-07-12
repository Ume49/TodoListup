from tkinter import *
from tkinter import ttk
import Widget

root_window = Tk()

root_window.title("TODO ListUp forUnity")

root_window.geometry("480x240")


# ウィジェット配置

root_frame = Frame(root_window, pady= 10)

directory   = Widget.Ask_Directory_Form (root_frame)
findtag     = Widget.Ask_FindTag_Form   (root_frame)
file_ex     = Widget.Ask_file_exstension(root_frame)
encode      = Widget.Ask_Encode         (root_frame)
button      = Widget.Execute_Button     (root_frame)

# 配置
root_frame.pack()

directory.root.pack(anchor="w")
directory.Member_Pack()

findtag.root.pack(anchor="w")
findtag.Member_Pack()

file_ex.root.pack(anchor="w")
file_ex.Member_Pack()

encode.root.pack(anchor="w")
encode.Member_Pack()

button.root.pack(expand=1)
button.Member_Pack()

# 使用予定
# list = Search_TODO.SearchString_behindTODO("directory")
# listには表示すべき文字列リストが返ってくる

root_window.mainloop()