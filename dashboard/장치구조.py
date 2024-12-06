import streamlit as st

# PDF를 이미지로 변환
st.title("장치 구조 📃")

# 상자 스타일 텍스트 삽입
st.markdown("""
    <div style="padding: 20px; border-radius: 15px; border: 2px solid #ccc;">
        <h3><b>밑면 :   </b></h3>   
        안쪽 약 20cm X 20cm<br>
        바깥쪽 약 22cm X 22cm<br><br>
        <h3><b>높이 :   </b></h3> 
        안쪽 약 24cm<br>
        바깥쪽 약 25cm<br>
    </div>
""", unsafe_allow_html=True)

st.write("\n")

# 상자 스타일 텍스트 삽입
st.markdown("""
    <div style="padding: 20px; border-radius: 15px; border: 2px solid #ccc;">
        <h3><b>문 :   </b></h3>   
        <b>문에 레일을 통해 톱니가 돌면서 문이 열린다.</b><br>
        약 10cm X 21cm<br><br>
        <h3><b>끈끈이 넣는 구멍 :   </b></h3> 
        <b>아래에 바퀴벌레  끈끈이를 넣어 바퀴벌레를 잡는 용도로도 사용할 수 있다.</b><br>
        약 14cm X 4cm<br><br>
        <h3><b>스프레이 놓는 공간 :   </b></h3> 
        <b>두 종류 이상의 스프레이를 넣어 여러 기능을 수행한다.</b><br>
        밑면 약 20cm X 5cm<br>
        높이 약 13cm<br>
    </div>
""", unsafe_allow_html=True)

