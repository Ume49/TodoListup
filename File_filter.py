import os

# 渡されたファイルパスのリストから、特定の拡張子のものだけを抽出したリストを作成して返す
# 拡張子は完全一致するものだけを返す 
# 例：指定した拡張子".cs" .cs->OK .cs.meta->ダメ
def Filter_extension(file_list : list, output_list =[], extension = ".cs") :
    for w in file_list:
        # 拡張子を取得
        current_extension = search_extension(w)

        if current_extension == extension:
            output_list.append(w)

# 渡されたファイル名の拡張子を返す
def search_extension(name="filename.extension"):
    index = name.rfind(".")

    return name[index :]

# デバッグ用
if __name__ == "__main__":
    list = [
        "D:\\E_repos\\Tumi_Dungeon\\詰めダンジョン\\Assets\\Script\\Undo\\ReverseCommand\\IReverseCommand.cs",
        "D:\\E_repos\\Tumi_Dungeon\\詰めダンジョン\\Assets\\Script\\Undo\\ReverseCommand\\ReverseCommand_Executer.cs.meta",
        "D:\\E_repos\\Tumi_Dungeon\\詰めダンジョン\\Assets\\Script\\Undo\\ReverseCommand\\ReverseCommand_Executer.cs"
    ]

    result = Filter_extension(list, ".cs")

    for w in result:
        print(w)