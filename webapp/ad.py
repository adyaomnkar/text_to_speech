import streamlit as st
import os
from gtts import gTTS

language = 'en'

 
st.title("Text to Speech converter🤖")
st.subheader("Give Voice to Your Text")
st.header("Text to Speech converter🔉")


st.write("Behold, an extraordinary Text to Speech alchemist!")
st.write("Made with ❤️ by [Adya]")
st.markdown("---")
user=st.text_area("Enter the text you want to convert to speech")

output = gTTS(text=user, lang=language, slow=False)
print(user)
output.save("output.mp3")
os.system("start output.mp3")
st.audio("output.mp3", format='audio/mp3')
st.markdown("---")
st.write("©️Adya : licensed under adya_personal_License.All rights reserved under the syntax slayers.")



