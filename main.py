from tkinter import *
from tkinter import * 
from tkinter import ttk
from Display import Display
import Widget
from Execute import Execute

_root_window = Tk()

_root_window.title("TODO ListUp forUnity")

_root_window.geometry("480x240")

# ウィジェット配置

_root_frame = Frame(_root_window, pady= 10)

_directory   = Widget.Ask_Directory_Form (_root_frame)
_findtag     = Widget.Ask_FindTag_Form   (_root_frame)
_file_ex     = Widget.Ask_file_exstension(_root_frame)
_encode      = Widget.Ask_Encode         (_root_frame)
_display     = Display(_root_window)

_button = ttk.Button(
    _root_frame,
    text="検索！",
    command = lambda:
        Execute(_directory.get(), _findtag.get(), _file_ex.get(), _encode.get(), _display)
)

# 配置
_root_frame.pack()

_directory.root.pack(anchor="w")
_directory.Member_Pack()

_findtag.root.pack(anchor="w")
_findtag.Member_Pack()

_file_ex.root.pack(anchor="w")
_file_ex.Member_Pack()

_encode.root.pack(anchor="w")
_encode.Member_Pack()

_button.pack()

_root_window.mainloop()
