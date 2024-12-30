import subprocess
import os

def convert_epub_to_markdown(input_file, output_file, media_dir="./media"):
    """
    EPUBファイルをMarkdown形式に変換する関数。

    :param input_file: 入力EPUBファイルのパス
    :param output_file: 出力Markdownファイルのパス
    :param media_dir: メディアファイルを抽出するディレクトリ（デフォルト: ./media）
    """
    # メディアディレクトリが存在しない場合は作成
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    # Pandocコマンドの構築
    command = [
        "pandoc",
        "-i", input_file,
        "-o", output_file,
        f"--extract-media={media_dir}",
        "--markdown-headings=atx"
    ]

    try:
        # Pandocコマンドの実行
        subprocess.run(command, check=True)
        print(f"変換が完了しました: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"エラーが発生しました: {e}")
    except FileNotFoundError:
        print("Pandocがインストールされていることを確認してください。")

# 使用例
input_epub = "example.epub"  # 入力EPUBファイル名
output_md = "example.md"     # 出力Markdownファイル名

convert_epub_to_markdown(input_epub, output_md)
