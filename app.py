import streamlit as st 

print(st.header("Hello this is Streamlit Page"))

print(st.title("This is Maxhine learning page"))

print(st.write("hello my name is Alok kumar verma i`m your Data Science Trainner."))


name = st.text_input("enter your name")
num = st.number_input("enter number: ")

salary = st.slider("your salary range ",0,1000)

st.markdown("# markdown")

st.chat_message("start hare: ")
agree = st.checkbox("I agree")

st.selectbox("Gemder",["Male","Female"])

st.multiselect("skill",["python","ml","dl","Agentic ai","genAi"])


st.date_input("DOB")

st.time_input("time")