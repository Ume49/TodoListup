# ウィジェットの配置をまとめたパッケージ
from tkinter import *
from tkinter import ttk

def Set_AskDirectory(frame):
    ttk.Label(
        frame,
        text="検索するフォルダ"
    ).pack(side=LEFT)

    ttk.Entry(
        frame,
        width = 32
    ).pack(side=LEFT)

    ttk.Button(
        frame,
        text  = "...",
        width = 3
    ).pack(side=LEFT)
    return

if __name__ == "__main__":
    root_window = Tk()

    main_frame = ttk.Frame(
        root_window,
        padding=16
    ).pack()

    ttk.Entry(
        main_frame
    ).pack(side=LEFT)

    ttk.Button(
        main_frame,
        text="ボタンだよ"
    ).pack(side=LEFT)

    ttk.Checkbutton(
        main_frame,
        text="チェックボックスだよ"
    ).pack()

    root_window.mainloop()