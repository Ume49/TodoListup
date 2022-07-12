from tkinter import Listbox, Tk
import Result_Component

# 得られた結果を表示するクラス
class Display:
    def __init__(this, component=[Result_Component.Result_Component()]):
        this.list = component
        
        # ウインドウを作成
        this.window = Tk()

        # リストを表示する場所を作成
        this.listbox = Listbox(this.window, listvariable = this.list)

        this.listbox.pack()