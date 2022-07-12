from tkinter import *
from tkinter import ttk
import Widget

root_window = Tk()

root_window.title("TODO ListUp forUnity")

root_window.geometry("400x300")


# ウィジェット配置

widgets = []

widgets.append(Widget.Ask_Directory_Form (root_window))
widgets.append(Widget.Ask_FindTag_Form   (root_window))
widgets.append(Widget.Ask_file_exstension(root_window))
widgets.append(Widget.Ask_Encode         (root_window))

for w in widgets:
    w.Pack()

# 使用予定
# list = Search_TODO.SearchString_behindTODO("directory")
# listには表示すべき文字列リストが返ってくる

root_window.mainloop()