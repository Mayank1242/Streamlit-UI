import streamlit as st

st.header("chatbot")

prompt= st.chat_input("enter your prompt")

if prompt:
    st.write(prompt)


with st.sidebar:
    st.header("this is header")
    st.write("this is write")
    st.button("this is button ")
    
st.markdown(
    "<p style='color:green;'>Application is running!</p>",
    unsafe_allow_html=True
)

