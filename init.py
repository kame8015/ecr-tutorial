"""
コンテナを立ち上げたときにpythonで実行したい処理
- nltk の punkt ライブラリ(単語分解用)をダウンロード
    (app.handler実行の度にダウンロードするより高速化できる)
- ダウンロード先を /var/task に指定
    (他のディレクトリだと Lambda 上で読み込まれない可能性有)
"""

import nltk
import os
nltk.download("punkt", download_dir=os.environ["LAMBDA_TASK_ROOT"])