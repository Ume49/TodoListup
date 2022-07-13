from tkinter import *
from tkinter import ttk

# 得られた結果を表示するクラス
class Display:
    def __init__(this, root_window):
        # ウインドウを作成
        this.window = Toplevel(root_window)

        this.window.geometry("640x480")

        # リストを表示する場所を作成
        this.listbox = Listbox(this.window, selectbackground="#00bfff", width=103, height=28)

        this.listbox.pack()

    # 表示する内容を追加
    def Add_list(this, list=[]):
        for w in list:
            this.listbox.insert(END, w)

# デバッグ用コード
if __name__ == "__main__":
    _root = Tk()

    _disp = Display(_root)

    _disp.Add_list(["あいうえお", "かきくけこ"])

    _root.mainloop()