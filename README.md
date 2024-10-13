# raspi-remote-controller

## つかいかた

1. [環境構築](#環境構築)の手順を実行してください。
2. ターミナルを開いて[バックエンドの実行](#バックエンドの実行)の手順に従ってください。
3. 新しくターミナルを開いて[フロントエンドの実行](#フロントエンドの実行)の手順に従ってください。

## 環境構築

次のコマンドを実行してください。

### （初回のみ）仮想環境を作成する

```bash
python -m venv raspi-remote-controller
```

### 仮想環境を実行する

```bash
source raspi-remote-controller/bin/activate
```

### （初回のみ）仮想環境内で必要なパッケージをインストールする

```bash
pip install uvicorn fastapi streamlit RPi.GPIO
```

## バックエンドの実行

次のコマンドを実行してください。

```bash
sudo env "PATH=$PATH" uvicorn backend:app --reload --host 0.0.0.0 --port 8000
```

## フロントエンドの実行

次のコマンドを実行してください。

```bash
streamlit run frontend.py
```
