# ウィジェットの配置をまとめたパッケージ
from tkinter import *
from tkinter import ttk

# ディレクトリを聞くためのフォーム
class Ask_Directory_Form:
    def __init__(self, root_tkobj):
        # 根元のフレーム
        self.root = ttk.Frame(
            root_tkobj
        )

        # ラベル
        self.label = ttk.Label(
            self.root,
            text="検索するフォルダ"
        )

        # 入力フォームとボタンを横に並べたいのでそれをまとめるフレーム
        self.entry_frame = ttk.Frame(
            self.root
        )

        # 入力フォーム
        self.entry = ttk.Entry(
            self.entry_frame
        )
        
        # 入力フォームの横のボタン
        self.button = ttk.Button(
            self.entry_frame,
            text    = "...",
            width   = 5
        )

    def Pack(self):
        # メンバを配置
        self.root       .pack()
        self.label      .pack(side=TOP, anchor="nw")
        self.entry_frame.pack(side=TOP)
        self.entry      .pack(side=LEFT)
        self.button     .pack(side=LEFT)

# 検索キーワードを聞くためのフォーム
class Ask_FindTag_Form:
    def __init__(self, root):
        # このクラスで扱うウィジェットの受け皿
        self.frame = ttk.Frame(
            root
        )
        
        # ラベル
        self.label = ttk.Label(
            self.frame,
            text    = "検索ワード"
        )

        # 入力フォーム
        self.entry = ttk.Entry(
            self.frame
        )
    def Pack(self):
        self.frame.pack()
        self.label.pack(side=TOP, anchor="nw")
        self.entry.pack(side=LEFT)

# エンコード形式の入力フォーム
class Ask_Encode:
    def __init__(this, root):
        # 受け皿
        this.frame = ttk.Frame(
            root
        )

        # ラベル
        this.label = ttk.Label(
            this.frame,
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
            this.frame,
            values = encode_list
        )

        # 先頭のやつを事前に登録しておく
        this.list.set(encode_list[0])

    def Pack(this):
        this.frame.pack()
        this.label.pack(anchor="w")
        this.list .pack(anchor="w")

# 拡張子の入力フォーム
class Ask_file_exstension:
    def __init__(this, root):
        # 受け皿
        this.frame = ttk.Frame(
            root
        )

        this.label = ttk.Label(
            this.frame,
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
            this.frame,
            values=ex_list
        )

        # 候補の先頭を事前に表示しておく
        this.list.set(ex_list[0])

    def Pack(this):
        this.frame.pack()
        this.label.pack(anchor="w")
        this.list .pack(anchor="w")

if __name__ == "__main__":
    t = Tk()

    widgets = Ask_file_exstension(t)
    
    widgets.Pack()

    t.mainloop()