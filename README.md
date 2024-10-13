# raspi-remote-controller

## つかいかた

1. [環境構築](#環境構築)の手順を実行してください。
2. [ハードウェアの設定](#ハードウェアの設定)の手順を実行してください。
3. ターミナルを開いて[バックエンドの実行](#バックエンドの実行)の手順に従ってください。
4. 新しくターミナルを開いて[フロントエンドの実行](#フロントエンドの実行)の手順に従ってください。
5. スマートフォンやPCのWebブラウザから、4.の手順で表示されたURLにアクセスしてください。

## 環境構築

Raspberry Piで次のコマンドを実行してください。

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

## ハードウェアの設定

1. Raspberry Piを立ち上げてください
2. GPIOピンを適切な箇所に挿してください
    - デフォルトでは、ポート左下部の次の七本のピンに挿しています
        - GND
        - GPIO 13
        - GPIO 16
        - GPIO 19
        - GPIO 20
        - GPIO 21
        - GPIO 26
    - ピン配置図: https://qiita.com/Erytheia/items/f362a3d68e57cd088713

## バックエンドの実行

Raspberry Piで次のコマンドを実行してください。

```bash
sudo env "PATH=$PATH" uvicorn backend:app --reload --host 0.0.0.0 --port 8000
```

## フロントエンドの実行

Raspberry Piで次のコマンドを実行してください。

```bash
streamlit run frontend.py
```
