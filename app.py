import streamlit as st

st.title("ナップザック問題")
st.text("商品の価値と重さを入力してください")
st.text("重さ:")
weights = st.text_input("")
st.text("価値:")
values = st.text_input("")
st.text("ナップザックの最大重量を入力してください")
max_weight = st.text_input("")

if st.button("解く"):
    result = knapsack(weights, values, max_weight)
    st.success(f"最大価値は{result}です")
