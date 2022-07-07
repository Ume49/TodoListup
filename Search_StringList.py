

# "// TODO"という文字の後に続く行を探してリストアップする
# ファイルパスは絶対パス渡してね
def Search_behindTODO(file_path = "", find_tag = "", output_list = []):
    encode_option = "utf-8_sig"

    file_data = open(file_path, encoding=encode_option)

    # 行番号カウンタ
    line_num = 0

    # "// TODO"を検索して、該当コメントをリストに追加
    for line in file_data:
        line_num += 1

        # 検索アルゴリズム書く
        todo_index = line.find(find_tag)

        # 見つからん場合は次の行へ
        if todo_index == -1: continue

        # TODO以降の文章をリストに追加
        # TODO リストの形式が後で変わるので、その時に合わせてここも変える
        output_list.append(line[todo_index+len(find_tag) : ])

    file_data.close

    return

if __name__ == "__main__":
    dir = "D:\E_repos\Tumi_Dungeon\詰めダンジョン\Assets\Script\Charactor\Charactor_Paramater.cs"

    file_data = open(dir, "r", encoding="utf-8_sig")

    for line in file_data:
        index = line.find("using")
        if index != -1:
            print(line[index+5 : ])

    file_data.close()