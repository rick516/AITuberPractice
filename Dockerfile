
# 使い方
# ビルドコマンド
# docker build -t python-docker .


# 使用するベースイメージの指定
FROM python:3.11.4

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# 必要なファイルをコンテナ内にコピー
# 例えば、requirements.txtがあれば以下のように追加します
# COPY requirements.txt ./

# 依存関係のインストール
# RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# コンテナが起動する際に実行されるコマンド
CMD [ "python", "./your-script.py" ]
