def convert_markdown_to_text(input_file_path, output_file_path):
  """
  Markdownファイルをテキストファイルに変換する関数。

  Args:
    input_file_path: 入力Markdownファイルのパス。
    output_file_path: 出力テキストファイルのパス。
  """

  try:
    # 入力ファイルを開いて読み込む
    with open(input_file_path, 'r', encoding='utf-8') as md_file:
      markdown_content = md_file.read()

    # 出力ファイルを開いて書き込む
    with open(output_file_path, 'w', encoding='utf-8') as txt_file:
      txt_file.write(markdown_content)

    print(f"Markdownファイル '{input_file_path}' をテキストファイル '{output_file_path}' に変換しました。")

  except FileNotFoundError:
    print(f"エラー: 入力ファイル '{input_file_path}' が見つかりません。")

  except Exception as e:
    print(f"エラー: ファイルの変換中にエラーが発生しました: {e}")
