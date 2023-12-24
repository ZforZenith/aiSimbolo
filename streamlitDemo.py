import streamlit as st 

st.header ("Zenith's Calculator")
ftnum = st.number_input ('Please enter your first number: ', value = None, placeholder='First number...')
opt = st.text_input ('What operator do you want: ', placeholder='Operator (+,  -,  *,  /)')
st.write("Don't worry if u get an error! when u enter ur opterator, enter the second number and u will get the correct answer :3")
sdnum = st.number_input ('Please enter your second number: ', value = None, placeholder='Second number...')
if opt=='+':
    ans = ftnum + sdnum
    st.write('The answer is: ', ans)
if opt=='-':
    ans = ftnum - sdnum
    st.write('The answer is: ', ans)
if opt=='*':
    ans = ftnum * sdnum
    st.write('The answer is: ', ans)
if opt=='/':
    ans = ftnum / sdnum
    st.write('The answer is: ', ans)
