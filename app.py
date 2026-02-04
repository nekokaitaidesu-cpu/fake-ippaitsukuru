import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker("ja_JP")

st.set_page_config(
    page_title="🎭 Faker Playground",
    page_icon="🎭",
    layout="centered"
)

st.title("🎭 Faker Playground")
st.caption("それっぽい架空データを生成するGUIツール")

st.markdown("---")

data_type = st.selectbox(
    "🧩 生成するデータを選んでね",
    [
        "人名",
        "住所",
        "メール",
        "会社名",
        "文章",
        "日付"
    ]
)

count = 1
if data_type == "人名":
    count = st.slider("👥 何名出力する？", 1, 50, 5)

if st.button("✨ 生成する"):
    results = []

    if data_type == "人名":
        results = [fake.name() for _ in range(count)]

    elif data_type == "住所":
        results = [fake.address()]

    elif data_type == "メール":
        results = [fake.email()]

    elif data_type == "会社名":
        results = [fake.company()]

    elif data_type == "文章":
        results = [fake.text(max_nb_chars=120)]

    elif data_type == "日付":
        results = [str(fake.date())]

    st.markdown("### 📋 生成結果")

    # テキスト表示
    output_text = "\n".join(results)
    st.text_area(
        "👇 コピー用",
        value=output_text,
        height=150
    )

    # 人名だけExcelコピー対応
    if data_type == "人名":
        df = pd.DataFrame(results, columns=["name"])
        st.markdown("### 📊 Excel用（そのままコピペOK）")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ CSVダウンロード",
            csv,
            "fake_names.csv",
            "text/csv"
        )

    st.caption("※ 全て架空データです。実在しません 🎭")
