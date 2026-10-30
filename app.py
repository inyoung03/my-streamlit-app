
import os
import base64
import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 생성
client =

# 페이지 설정
st.set_page_config(page_title="텍스트 음성 변환 서비스", page_icon="🤖")
st.title"("🤖 음성 변환 서비스")
st.write("음성을 변환해드릴게옹")

# 텍스트 입력
text = st.text_area(
    "읽을 텍스트를 입력하세요",
    "안녕하세요. OpenAI 텍스트 음성 변환 실습입니다."
)

# 버튼
if st.button("입력"):
    if text.strip() == "":
        st.warning("텍스트를 입력하세요")
    else:
        # TTS 생성
        speech = client.audio.speech.create(
            model="whisper-1",
            voice="nova",
            input=text
        )
        audio_bytes = speech.content

        # 음성 출력
        st.markdown("### 🔊 음성 재생")
        st.audio(speech.content, format="audio/mp3")
