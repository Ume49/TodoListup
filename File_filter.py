import os

# 渡されたファイルパスのリストから、特定の拡張子のものだけを抽出したリストを作成して返す
# 拡張子は完全一致するものだけを返す 
# 例：指定した拡張子".cs" .cs->OK .cs.meta->ダメ
def Filter_extension(file_list = ["",""] , extension = ".cs") :
    result = []
    
    for w in file_list:
        # 拡張子を取得
        current_extension = search_extension(w)

        if current_extension == extension:
            result.append(w)

    return result

# 渡されたファイル名の拡張子を返す
def search_extension(name="filename.extension"):
    index = name.rfind(".")

    return name[index :]

# デバッグ用
if __name__ == "__main__":
    fn="IReverseCommand.cs.meta"

    print(search_extension(fn))