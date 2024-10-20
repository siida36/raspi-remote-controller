import streamlit as st
import requests

# FastAPIのエンドポイント
API_URL = "http://localhost:8000/control_led/"
API_URL2 = "http://localhost:8000/process_number/"

st.title("Raspberry Pi LED Controller")

# ボタンとアクションのリスト
buttons = ["Button 2", "Button 3", "Button 4", "Button 5", "Button 6"]
# input
number = st.number_input("input:",min_value=0, max_value=100, value=50)
# botton
if st.button("send"):
    response = requests.post(API_URL2, json={"number": number})

    if response.status_code == 200:
        result = response.json().get("result")
        st.write("result", result)
    else:
        st.write("error", response.status_code)

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

