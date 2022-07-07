# 表示リストに使用するクラスというか構造体
# 使用例： 後で中身を記述する (sentence) TestCode.py (file_name) 32行目 (line)
class Result_Component:
    def __init__(self, sentence="", file_name="", line=0) :
        self.sentence   = sentence      # コメント
        self.file_name  = file_name     # ファイル名
        self.line       = line          # そのファイルの何行目にあるコメントなのか