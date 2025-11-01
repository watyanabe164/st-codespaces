import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sample Streamlit App", layout="centered")

st.title("Sample Streamlit App")
st.markdown("簡単なインタラクティブなデモです。左のサイドバーでパラメータを変えてみてください。")

# サイドバーでパラメータ調整
n = st.sidebar.slider("観測数 (n)", 10, 2000, 200)
mean = st.sidebar.slider("平均 (mean)", -10.0, 10.0, 0.0, step=0.1)
std = st.sidebar.slider("標準偏差 (std)", 0.1, 10.0, 1.0, step=0.1)

# データ生成
np.random.seed(42)
data = np.random.normal(loc=mean, scale=std, size=n)
df = pd.DataFrame({"value": data})

# 表示
st.subheader("最初の10行")
st.dataframe(df.head(10))

st.subheader("値の分布")
st.line_chart(df)

st.subheader("要約統計")
st.write(df.describe())

# CSV ダウンロード
csv = df.to_csv(index=False)
st.download_button("CSV をダウンロード", csv, file_name="sample_data.csv", mime="text/csv")

# 簡単な説明
st.info("このサンプルは Streamlit の使い方の一例です。実際のアプリでは他の入力コンポーネントやレイアウトを組み合わせてください。")
