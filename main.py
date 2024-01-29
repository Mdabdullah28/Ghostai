import streamlit as st import google.generativeai as genai genai.configure(api_key=st.secrets["gemini_api"]) def ai(txt):
for m in genai.list_models():
if 'generateContent' in m.supported_generation_methods:
print(m.name)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("from now your name is ghost and your a ethical hacker and cloud data engineer, your real name is abdullah r and reply to this in short: "+txt)
return response.text
st.title("Ghost Al assistant")
command=st.chat_input("HOW CAN I HELP YOU?")
if "message" not in st.session_state: st.session_state.message=[]
for chat in st.session_state.message: with st.chat_message(chat["role"]): st.write(chat["message"])
if command: with st.chat_message("user"):
st.write(command)
st.session_state.message.append({"role":"user","message" :command})
if "hello" in command: with st.chat_message("bot"): st.write("Hi How can i help you.")
st.session_state.message.append({"role":"bot","message":" Hi How can i help you."}) elif "who" in command: with st.chat_message("bot"): st.write("Im ghost ai assistant")
st.session_state.message.append({"role":"bot","message":" Im ghost ai assistant")) elif "hi" in command:
with st.chat_message("bot"): st.write("hello good morning")
st.session_state.message.append({"role":"bot","message":" hello good morning"})
st.session_state.message.append({"role":"bot","message":" hello good morning"})
else:
with st.chat_message("bot"):
data=ai(command)
st.write(data)
st.session_state.message.append({"role":"bot","message": data})
print(st.session_state.message)
