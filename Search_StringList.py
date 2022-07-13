import os

# "// TODO"という文字の後に続く行を探してリストアップする
# ファイルパスは絶対パス渡してね
def Search_behindTODO(file_path = "", find_tag = "// TODO ", encode_option = "utf-8_sig", output_list = []):
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

        # TODO以降の文章を取得
        sentence = line[todo_index + len(find_tag) : ]
        
        # パスからファイル名を抽出
        file_name = os.path.basename(file_path)

        # 返却用リストに項目を追加
        output_list.append(Format_File_Info(sentence=sentence, file_name=file_name, line=line_num))

    file_data.close()

    return

# 文章、ファイル名、何行目という情報を1行の文章に結合する
def Format_File_Info(sentence="", file_name="", line=0):
    return sentence + " " + file_name + " " + str(line) + "行目"

if __name__ == "__main__":
    dir = "D:\E_repos\Tumi_Dungeon\詰めダンジョン\Assets\Script\Charactor\Charactor_Paramater.cs"