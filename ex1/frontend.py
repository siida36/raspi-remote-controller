import streamlit as st
import requests

# FastAPIのエンドポイント
API_URL = "http://localhost:8000/control_led/"

st.title("Raspberry Pi LED Controller")

# ボタンとアクションのリスト
buttons = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5", "Button 6"]

# 各ボタンに対してLEDのON/OFFを制御
for button_name in buttons:
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"{button_name} ON"):
            response = requests.post(API_URL, json={"button_name": button_name, "action": "on"})
            if response.status_code == 200:
                st.success(response.json().get("message", "Success!"))
            else:
                st.error(f"Error: {response.status_code}")
    with col2:
        if st.button(f"{button_name} OFF"):
            response = requests.post(API_URL, json={"button_name": button_name, "action": "off"})
            if response.status_code == 200:
                st.success(response.json().get("message", "Success!"))
            else:
                st.error(f"Error: {response.status_code}")

