# .gitignoreに下記のコードを追加してください
# code_merger.py
# merged_codes

import os
from datetime import datetime
import pyperclip

# マージの対象となるの拡張子を指定
extensions = ['.js', '.html', '.py']

# 除外するファイル名のリスト
# マージする対象から外したいコードが有る場合は、ここに追加してください。
exclude_files = ['code_merger.py', 'merged_codes']

# カレントディレクトリの全ファイルとディレクトリの名前をリストで取得
all_items = os.listdir('.')

# ファイルのみをリストアップ（ディレクトリは除外）
files_only = [item for item in all_items if os.path.isfile(item)]

# 拡張子がextensionsリストに含まれ、除外リストに含まれていないファイルをフィルタリング
files = [file for file in files_only if file not in exclude_files and any(file.endswith(ext) for ext in extensions)]

merged_content = '' 

# 各ファイルを読み込み、内容を一つの文字列にまとめる
for file in files:
    # ファイルの拡張子によって、言語を決定
    lang = file.split('.')[-1]

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # マークダウンのコードブロックに変換
    merged_content += f'## {file}\n```{lang}\n{content}\n```\n\n'

# 現在のタイムスタンプを取得
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# `merged_codes` フォルダが存在しない場合は作成
if not os.path.exists('merged_codes'):
    os.makedirs('merged_codes')

# 結果を新たなファイルに書き込む
output_filename = f'merged_codes/{timestamp}_merged_code.md'
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(merged_content)

# マージしたテキストをクリップボードにコピー
pyperclip.copy(merged_content)
