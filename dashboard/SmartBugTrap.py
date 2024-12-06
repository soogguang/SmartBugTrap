import streamlit as st
import qrcode
from PIL import Image

# Streamlit 페이지 설정
st.set_page_config(page_title="Smart Bug Trap", layout="wide")
st.title("Smart Bug Trap 🦟")
st.write("딥러닝 기반의 해충 탐지 및 제거 시스템")
st.markdown('<pre># 지속성  # 정돈된 외관      # 편리함       # 쉬운 관리</pre>', unsafe_allow_html=True)

st.image("/Users/jangsooin/Library/Mobile Documents/com~apple~CloudDocs/숭실대학교/숭실대학교(1-2)/프로그래밍및실습2/프로젝트_프밍2/대시보드/flowchart_ras.png", caption="Smart Bug Trap flow chart", use_container_width=True)


for i in range(8):
    st.write("\n")

st.header("장치 특징 👾")
st.markdown('<span style="font-size: 20px; color: MediumPurple;"><b>전통적인 벌레 박멸 방법</b></span><span style="font-size: 20px; color: black;"><b>인 업체를 부르거나 끈끈이, 살충제 등을 사용하는 방식은 벌레가 주로 활동하는 특정 지역을</b></span> <span style="font-size: 20px; color: MediumPurple;"><b>효율적으로 타겟팅하기 어렵다.</b></span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px; color: black;"><b>보다 간편하고 지속 가능한 해결책을 찾고자,</b></span><span style="font-size: 20px; color: MediumPurple;"><b> 라즈베리파이를 활용하여 벌레를 유인하고 살충제를 뿌린 뒤</b></span> <span style="font-size: 20px; color: black;"><b>손쉽게 처리할 수 있는 장치를 고안하게 되었다.</b></span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px; color: black;"><b>이 장치는 집 안 뿐만 아니라 캠핑장고 같은 외부 환경에서도 </b></span><span style="font-size: 20px; color: MediumPurple;"><b> 전원만 있다면</b></span> <span style="font-size: 20px; color: black;"><b> 자유롭게 사용할 수 있도록 설계되었다.</b></span>', unsafe_allow_html=True)

for i in range(8):
    st.write("\n")

# 주의 사항
st.header("주의 사항 🛑")
st.markdown('<span style="font-size: 20px; color: black;"><b> 1. 장치에 손을 넣으면 안됩니다.</b></span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px; color: black;"><b> 2. 어두운 곳에서는 작동이 잘 되지 않을 수 있습니다.</b></span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px; color: black;"><b> 3. 살충제와 유인제를 다 사용했을 경우 리필해줘야 합니다.</b></span>', unsafe_allow_html=True)

for i in range(8):
    st.write("\n")

# 장치 사진 업로드 섹션
st.header("장치 모습 📸")



st.header("QR 코드 📸")
dashboard_url = "http://localhost:8502" 
qr = qrcode.make(dashboard_url)
qr_image = qr.convert('RGB')
st.image(qr_image, caption="대시보드 QR 코드", use_column_width=True)