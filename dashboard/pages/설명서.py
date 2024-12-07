import streamlit as st

st.title("설명서 📖")

st.markdown('<p style="font-size: 20px;"><b>1. 벌레(모기)를 잡고 싶은 공간에 장치를 둡니다.</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px;"><b><br>2. 9V정도의 전원을 연결합니다.</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px;"><b><br>3. 장치를 실행시킵니다.</b></p>', unsafe_allow_html=True)
             
           
for i in range(8):
    st.write("\n")            

st.title("알아 두면 좋은 정보 ℹ️")
st.markdown('<p style="font-size: 20px;"><b>1. 장치 부품은 스프레이 분사 시 닿지 않는 곳에 배치하였기 때문에 걱정하지 않아도 됩니다!</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px;"><b><br>2. 장치 위 뚜껑은 열 수 있도록 제작되어있습니다. 살충제 및 유인제는 뚜껑을 열어 손쉽게 리필이 가능합니다!</b></p>', unsafe_allow_html=True)         
st.markdown('<p style="font-size: 20px;"><b><br>3. 아래 구멍에는 바퀴벌레용 끈끈이를 넣을 수 있습니다. 끈끈이를 통해 모기 사체 처리와 바퀴벌레 제거를 동시에 할 수 있습니다!</b></p>', unsafe_allow_html=True)  
