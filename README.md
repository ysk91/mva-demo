# mva-demo

## Description

## 環境の準備

### .env ファイルの作成

```
$ cp .env.sample .env
```

必要なAPIキーは以下のリンクから取得してください。

- OPENAI_API_KEY
  - https://platform.openai.com/settings/profile?tab=api-keys
- GITHUB_TOKEN
  - https://github.com/settings/tokens


### 必要なパッケージのインストール

```
# 仮想環境の作成
$ python -m venv env

# 仮想環境の有効化（macOS/Linux）
$ source env/bin/activate

# 仮想環境の有効化（Windows）
$ .\env\Scripts\activate

# 必要なパッケージのインストール
$ pip install -r requirements.txt
```
