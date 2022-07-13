from GetFileList import GetFileList_fromRootDirectory
from File_filter import Filter_extension
from Search_StringList import Search_behindTODO
from Display import Display
from Widget import *

# 最終的な実行関数
# 実行ボタンを押したときの処理
def Execute(directory : str, tag : str , extension : str, encode : str, output_display : Display):
    # ファイルを検索して欲しい文章リストを取得する

    # 入力要素の中に空項目があった場合は処理をスキップ
    if (len(directory) * len(tag) * len(extension) * len(encode)) == 0:
        print("入力されていない項目があります")
        return
    
    # ファイルの一覧を取得
    file_list = []
    GetFileList_fromRootDirectory(root_directory = directory, output_list = file_list)

    # 指定した拡張子のファイルだけを抽出したリストを作成
    filterd_file_list = []
    Filter_extension(
        file_list   = file_list,
        output_list = filterd_file_list,
        extension   = extension
        )

    # 表示する文章リストを抽出したファイルから検索
    result_list = []
    for path in filterd_file_list:
        Search_behindTODO(file_path=path, find_tag=tag, encode_option=encode, output_list=result_list)

    # ディスプレイに結果を投げる
    output_display.Add_list(result_list)


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk

    _window = Tk()

    _display = Display(_window)

    Execute("D:/E_repos/Tumi_Dungeon/詰めダンジョン/Assets/Script", "// ", ".cs", "utf-8_sig", _display)

    _window.mainloop()