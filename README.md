# Code Merger

This program is a Python script that reads all .js, .html, and .py files in the same directory and combines their content into a single markdown format string. This result is written to a new markdown file and is also copied to the clipboard.

このプログラムは、同じディレクトリにある全ての.js、.html、.pyファイルを読み込み、その内容を一つのマークダウン形式の文字列にまとめるPythonスクリプトです。この結果は、新たなマークダウンファイルに書き込まれ、同時にクリップボードにもコピーされます。

## Usage | 使い方

When you run the program, the contents of all .js, .html, and .py files in the same directory are combined, and a new markdown file is created. The name of the generated file will be the current timestamp ('YYYYMMDDHHMMSS_merged_code.md').

プログラムを実行すると、同じディレクトリにある全ての.js、.html、.pyファイルの内容が結合され、新しいマークダウンファイルが生成されます。生成されるファイルの名前は現在のタイムスタンプ（'YYYYMMDDHHMMSS_merged_code.md'）となります。

## Installation | インストール方法

1. Install Python. This project has been tested on Python 3.8 and above.
2. Install the necessary libraries. Use the following command: `pip install pyperclip`

1. Pythonをインストールします。このプロジェクトはPython 3.8以上でテストされています。
2. 必要なライブラリをインストールします。次のコマンドを使用してください: `pip install pyperclip`

## Execution | 実行方法

This script can be run from the command line. Run it as follows:
このスクリプトはコマンドラインから実行できます。以下のように実行してください:

```bash
python main.py
```
When you run the above command, the script scans .js, .html, and .py files in the current directory and combines their content to create a new markdown file. This file is named with the current timestamp.

上記コマンドを実行すると、スクリプトは現在のディレクトリにある.js、.html、.pyファイルをスキャンし、その内容を結合して新しいマークダウンファイルを作成します。このファイルは、現在のタイムスタンプで名付けられます。

## Note | 注意事項

This script reads all existing .js, .html, and .py files. If there are a large number of files in the directory, the script execution time may be long. Also, the generated markdown file may become very large.

このスクリプトは、存在する全ての.js、.html、.pyファイルを読み込みます。ディレクトリ内に大量のファイルが存在する場合、スクリプトの実行時間が長くなる可能性があります。また、生成されるマークダウンファイルも非常に大きくなる可能性があります。
