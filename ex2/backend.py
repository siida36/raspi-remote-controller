from fastapi import FastAPI
import RPi.GPIO as GPIO

# FastAPIのインスタンスを作成
app = FastAPI()

# GPIOの設定
GPIO.setmode(GPIO.BCM)  # GPIOの番号をBCM形式で指定
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # GPIO21を入力モードに設定（他のピンを使う場合は適宜変更）

@app.get("/gpio_status/")
async def gpio_status():
    # GPIOの入力状態を取得（0または1）
    input_state = GPIO.input(21)
    return {"gpio_state": input_state}

# アプリ終了時にGPIOをクリーンアップ
@app.on_event("shutdown")
def cleanup_gpio():
    GPIO.cleanup()

