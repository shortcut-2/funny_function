import streamlit as st
import time
import random

st.title('🔮나는 전생에 무엇이었을까?🔮')
st.subheader('이름을 입력하고 결과를 받아보세요!')
st.image("https://cdn.pixabay.com/photo/2021/10/26/19/03/moon-6744954_1280.jpg")


def past_world(*world):
    return random.choice(world)

world_list = ['원시', '중세', '근대', '근현대']

def past_reign(*reign):
    return random.choice(reign)

reign_list = ['유럽', '동아시아', '아프리카', '아메리카', '남극']

def past_job(*job):
    return random.choice(job)

job_list = ['펭귄', '사자', '호랑이', '토끼', '코끼리', '독수리', '고래', '늑대', '판다', '낙타', '기린', '부엉이', '농부', '대장장이', '의사', '광대', '사냥꾼', '기사', '음유시인', '성직자', '귀족', '호위무사', '학자', '요리사', '예술가', '학생', '수사관', '나무꾼', '상인', '전사', '일반인', '하인', '선생님', '왕']

def past_personal(*personal):
    return random.choice(personal)

personal_list = ['친절', '다정', '선량', '온화', '냉혹', '용맹', '비겁', '성실', '나태', '겸손', '오만', '신중', '경솔', '교활', '대범', '소심', '잔인', '정직', '냉철']

def past_die(*die):
    return random.choice(die)

die_list = ['발을 헛디딤', '전투 중 사망', '자다가 사망', '익사', '암살', '역병', '굶주림', '맹수의 습격', '노환', '저주', '독살', '낙뢰', '동사', '화형', '상심', '식도 폐쇄', '석화', '과로사', '실종', '과식', '화병', '반역으로 처벌', '웃다가 사망']


st.badge('🔍약 30만 개의 결과가 대기 중입니다!')

if 'my_past' not in st.session_state:
    st.session_state.my_past = ''

st.session_state.my_past = st.text_input('✍️이름 입력')

if st.button('✅ 입력 완료') and st.session_state.my_past != '':
    with st.spinner('🫳🫳🫳수정구슬이 당신의 전생을 탐색하고 있습니다...', show_time=True):
        time.sleep(5)
        st.success('찾았다‼️')
        st.markdown(f'**{st.session_state.my_past}**님의 결과는~')
        st.markdown(f'**{past_world(*world_list)} 시대**의 **{past_reign(*reign_list)}**에 태어난 **{past_personal(*personal_list)}**한 **{past_job(*job_list)}**였습니다.')
        st.markdown(f'사망 사유는 **{past_die(*die_list)}**입니다!')
        st.balloons()

    if st.button('🔮수정구슬 다시 보기'):
        st.session_state.my_past = ''
        
    
