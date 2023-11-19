
# python 環境構築

## Makeコマンドでpythonをインストールする
Makeコマンド2回で環境構築を行えます。

```bash
$ make setup-pyenv
$ make setup-python
```

## venvで仮想環境の立ちあげる(macの場合)
```bash
source venv/bin/activate
```

* 閉じる場合は```deactivate```を実行する


# 依存関係のインストール
```bash
$ pip install -r requirements.txt
```

- 依存関係を追加する場合
```bash
$ pip freeze > requirements.txt
```

# VOICEVOX環境構築

## インストール
現在M1 Macでは動作しません。
[起動時に「cannot load library 'libsndfile.so'」と出て終了する](https://github.com/VOICEVOX/voicevox_engine/issues/770)で対応中の模様です
```bash
$ docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
$ docker run --rm -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
```

その代わりにappを[公式](https://github.com/VOICEVOX/voicevox_engine)からダウンロードするか、[homebrew](https://github.com/VOICEVOX/homebrew-voicevox)でインストールします。

```bash
$ brew tap VOICEVOX/voicevox
$ brew install --cask --no-quarantine voicevox
```

## GUIを立ち上げて、APIのdocsを開く
ローカルのPORT: `http://127.0.0.1:50021`
- `http://127.0.0.1:50021/docs`にアクセスするとAPIのdocsが見れます。

- スピーカーIDは`http://127.0.0.1:50021/speakers`をブラウザで開いたりAPI叩くと見れます。
- 例: 冥鳴ひまりちゃんは`14`

