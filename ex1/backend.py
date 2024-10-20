from fastapi import FastAPI
from pydantic import BaseModel
import RPi.GPIO as GPIO
import time

# FastAPIのインスタンスを作成
app = FastAPI()

# GPIOの設定
GPIO.setmode(GPIO.BCM)  # ピンの指定方式 (BCM)
GPIO.setwarnings(False)  # 警告を無視

LED_PINS = {
    "Button 1": 13,
    "Button 2": 19,
    "Button 3": 26,
    "Button 4": 16,
    "Button 5": 20,
    "Button 6": 21
}

# 各GPIOピンを出力モードに設定
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # 初期状態は消灯

# リクエストのデータ形式
class ButtonClick(BaseModel):
    button_name: str
    action: str  # "on" または "off"

# LEDを制御するエンドポイント
@app.post("/control_led/")
async def control_led(data: ButtonClick):
    pin = LED_PINS.get(data.button_name)
    if pin is None:
        return {"error": "Invalid button name"}

    if data.action == "on":
        GPIO.output(pin, GPIO.HIGH)  # LEDを点灯
    elif data.action == "off":
        GPIO.output(pin, GPIO.LOW)  # LEDを消灯
    else:
        return {"error": "Invalid action"}

    return {"message": f"LED for {data.button_name} turned {data.action}"}

# アプリ終了時にGPIOのクリーンアップ
@app.on_event("shutdown")
def cleanup_gpio():
    GPIO.cleanup()
