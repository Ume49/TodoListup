# ウィジェットの配置をまとめたパッケージ
# ここのクラスを使うときは、インスタンスを生成 → インスタンス.root.pack(オプション) → インスタンス.Member_Pack()の順番で呼んでね

from sys import displayhook
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# ディレクトリを聞くためのフォーム
class Ask_Directory_Form:
    def __init__(this, root):
        # 根元のフレーム
        this.root = ttk.Frame(root)

        # ラベル
        this.label = ttk.Label(
            this.root,
            text="検索するフォルダ"
        )

        # 入力フォームとボタンを横に並べたいのでそれをまとめるフレーム
        this.entry_frame = ttk.Frame(
            this.root
        )

        # 入力内容
        this.entry_value = StringVar()

        # 入力フォーム
        this.entry = ttk.Entry(
            this.entry_frame,
            textvariable = this.entry_value,
            width=60
        )
        
        # 入力フォームの横のボタン
        this.button = ttk.Button(
            this.entry_frame,
            text    = "...",
            width   = 5,
            command = this.Button_Directory
        )

    def Member_Pack(this):
        # メンバを配置
        this.label      .pack(side=TOP, anchor="nw")
        this.entry_frame.pack(side=TOP)
        this.entry      .pack(side=LEFT)
        this.button     .pack(side=LEFT)

    # ボタンを押したときのディレクトリ取得処理
    def Button_Directory(this):
        # ディレクトリを取得
        result_directory = filedialog.askdirectory()

        # 入力ボックスの中に内容を記述
        this.entry_value.set(result_directory)

# 検索キーワードを聞くためのフォーム
class Ask_FindTag_Form:
    def __init__(this, root):
        # このクラスで扱うウィジェットの受け皿
        this.root = ttk.Frame(root)
        
        # ラベル
        this.label = ttk.Label(
            this.root,
            text    = "検索ワード"
        )

        # 入力フォーム
        this.entry = ttk.Entry(
            this.root
        )
    def Member_Pack(this):
        this.label.pack(anchor="nw")
        this.entry.pack()

# エンコード形式の入力フォーム
class Ask_Encode:
    def __init__(this, root):
        # 受け皿
        this.root = ttk.Frame(root)

        # ラベル
        this.label = ttk.Label(
            this.root,
            text = "エンコード"
        )

        # 入力候補
        encode_list = [
            "utf-8",
            "shift_jis",
            "utf-8_sig"
        ]

        # 入力リスト
        this.list = ttk.Combobox(
            this.root,
            values = encode_list
        )

        # 先頭のやつを事前に登録しておく
        this.list.set(encode_list[0])

    def Member_Pack(this):
        this.label.pack(anchor="w")
        this.list .pack(anchor="w")

# 拡張子の入力フォーム
class Ask_file_exstension:
    def __init__(this, root):
        # 受け皿
        this.root = ttk.Frame(root)

        this.label = ttk.Label(
            this.root,
            text = "拡張子"
        )

        # 入力候補
        ex_list = [
            ".cs",
            ".cpp",
            ".h",
            ".py",
            ".txt"
        ]

        this.list = ttk.Combobox(
            this.root,
            values=ex_list
        )

        # 候補の先頭を事前に表示しておく
        this.list.set(ex_list[0])

    def Member_Pack(this):
        this.label.pack(anchor="w")
        this.list .pack(anchor="w")

# 実行ボタン
class Execute_Button:
    def __init__(this, root):
        this.root = Frame(root, pady = 10)

        this.button = ttk.Button(
            this.root,
            text = "実行！",
            command = this.Execute
        )
    
    def Member_Pack(this):
        this.button.pack(anchor="e")
    
    def Execute(this):
        import Display
        list = ["a", "b", "100", "200"]
        this.extra_window = Display.Display(list)

if __name__ == "__main__":
    t = Tk()

    widgets = Ask_Directory_Form(t)
    
    widgets.root.pack()
    widgets.Member_Pack()

    t.mainloop()