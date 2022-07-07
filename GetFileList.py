import os

# ディレクトリからファイルの一覧を取得する 再帰的に動き、フォルダを全部見ていく
def GetFileList_fromRootDirectory( root_directory="" , output_list = []):
    # 現在のフォルダの直下に存在するファイル、フォルダの一覧を取得
    current_obj_list = os.listdir(root_directory)

    # ファイルの一覧を抽出
    current_file_list = [f for f in current_obj_list if os.path.isfile(os.path.join(root_directory, f))]

    # ファイルのリストを返す
    for w in current_file_list:
        output_list.append(os.path.join(root_directory, w))
    
    # 現在のフォルダの中にさらにフォルダがあるならその中も見ていく

    # とりあえずフォルダのリストを取得
    current_folder_list = [f for f in current_obj_list if os.path.isdir(os.path.join(root_directory, f))]

    # そもそもフォルダが一個もないなら終わり
    if len(current_folder_list) <= 0 :
        return
    
    # 全部のフォルダに再帰処理
    for w in current_folder_list:
        GetFileList_fromRootDirectory(os.path.join(root_directory, w), output_list = output_list)

    return


# デバッグ
if __name__ == "__main__" :
    dir = "D:\E_repos\Tumi_Dungeon\詰めダンジョン\Assets\Script"

    result = []

    GetFileList_fromRootDirectory(dir, result)

    for w in result:
        print(w)
    
    print(len(result))
