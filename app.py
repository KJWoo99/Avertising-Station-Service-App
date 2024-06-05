import streamlit as st
from pymongo import MongoClient
import requests
import os

# MongoDB 연결 설정
mongo_url = os.getenv('MONGO_URL', 'mongodb+srv://woo010487:Gqpalzmtgvb2@cluster0.rxdnyjg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
client = MongoClient(mongo_url)
database = client['aiproject']
collection = database['ads']

st.title('광고 문구 서비스앱')
generate_ad_url = 'http://127.0.0.1:8000/create_ad'

product_name = st.text_input('제품 이름')
details = st.text_input('주요 내용')
options = st.multiselect('광고 문구의 느낌', options=['기본', '재밌게', '차분하게', '과장스럽게', '참신하게', '고급스럽게'], default=['기본'])

if st.button("광고 문구 생성하기"):
    result_area = st.empty()
    if not product_name or not details:
        result_area.error("제품 이름과 주요 내용을 입력하세요.")
    else:
        result_area.info("문구 생성 중")
        try:
            ad_data = {
                "product_name": product_name,
                "details": details,
                "tone_and_manner": ", ".join(options),
            }

            response = requests.post(generate_ad_url, json=ad_data)
            response.raise_for_status()
            ad = response.json().get('ad', '생성 실패')

            result_area.success(ad)

            ad_data['ad_content'] = ad
            collection.insert_one(ad_data)

            st.success("광고 문구가 DB에 저장되었습니다.")
        except requests.exceptions.RequestException as e:
            result_area.error("광고 문구 생성 실패!")
            result_area.error(e)
        except Exception as e:
            result_area.error("DB 저장 실패!")
            result_area.error(e)

st.sidebar.title('저장된 광고 제품 이름')
products = collection.distinct("product_name")
if products:
    selected_product = st.sidebar.selectbox("제품 선택", products, index=0)

    if selected_product:
        ad_data = collection.find({"product_name": selected_product}).sort("_id", -1)
        st.subheader("저장된 광고 문구:")
        for ad in ad_data:
            st.info(ad['ad_content'])
            if st.button("삭제", key=str(ad["_id"])):
                collection.delete_one({"_id": ad["_id"]})
                st.success("광고 문구가 삭제되었습니다.")
                st.experimental_rerun()
else:
    st.sidebar.info("저장된 광고 문구가 없습니다.")
