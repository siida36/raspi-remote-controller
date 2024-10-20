import streamlit as st
import requests
import time

# FastAPIのエンドポイント
API_URL = "http://localhost:8000/gpio_status/"

st.title("Raspberry Pi GPIO Monitor")

# リアルタイムでGPIOの状態をモニタリング
status_placeholder = st.empty()

# 定期的にAPIを呼び出してGPIOの状態を更新
while True:
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            gpio_state = response.json().get("gpio_state")
            if gpio_state == 1:
                status_placeholder.success("GPIO is HIGH (ON)")
            else:
                status_placeholder.warning("GPIO is LOW (OFF)")
        else:
            status_placeholder.error("Failed to get GPIO status")
    except Exception as e:
        status_placeholder.error(f"Error: {e}")

    time.sleep(1)  # 1秒ごとに状態を更新

