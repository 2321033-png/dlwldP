
import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="AI 동화 메이커", page_icon="📖")

# 스타일 설정
st.title("📖 AI 맞춤형 동화 창작기")
st.write("아이의 이름과 좋아하는 소재만 넣으면 하나뿐인 동화를 만들어드려요.")

# API 키 설정 (Streamlit Secrets용)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("설정에서 GEMINI_API_KEY를 등록해주세요!")
    st.stop()

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    child_name = st.text_input("주인공 이름", placeholder="예: 민수")
with col2:
    theme = st.text_input("동화 소재", placeholder="예: 공룡, 우주, 숲속 과자집")

genre = st.selectbox("동화 분위기", ["교훈적인", "유머러스한", "모험 가득한", "잠들기 전 읽어주는"])

if st.button("동화 생성하기 ✨"):
    if child_name and theme:
        prompt = f"주인공 이름은 '{child_name}'이고 소재는 '{theme}'이야. '{genre}' 분위기의 짧은 어린이 동화를 한 편 써줘. 마지막에는 아이에게 주는 짧은 메시지도 포함해줘."
        
        with st.spinner("이야기를 짓고 있습니다..."):
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader(f"제목: {child_name}의 {theme} 이야기")
                st.write(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("이름과 소재를 모두 입력해주세요!")
    