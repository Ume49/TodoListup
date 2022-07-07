# 表示リストに使用するクラスというか構造体

class Result_Component:
    def __init__(self, sentence="", file_name="", line=0) :
        self.sentence   = sentence
        self.file_name  = file_name
        self.line       = line