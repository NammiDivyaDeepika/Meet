import streamlit as st
from PIL import Image

st. set_page_config(layout="wide") 
image = Image.open("1.JPG")
st.header('Dear International Students in Cologne. Are you following the Saje Mystery? We’ve glad you’ve found us.')
st.subheader('Here’s the next part of the story:')
st.markdown("[Voice message left at 22:16]")
st.markdown("Hey Nadia, this is Jake. Just checking in after my Saje interview. Went pretty smoothly, spoke to a guy at the Fresenius “Pioneer Lab” it’s called. It’s like a start-hub at the university that supports students or founders to develop their ideas. Anyway, they’ve been supporting Sanvi Sharma and Jeremy Okana-Cole from, like, the beginning, giving them lots of advice and guidance and the like, and also put them in touch with a big-name mentor from Silicon Valley whose been working closely with them for a while. Her name is…Lynn Barker..Lynn..wait a moment, no that’s right, Lynn Barker. Yeah, so she’s apparently a big deal over in LA working as a consultant with all the big-name companies but also likes to give back and support start-ups on this side of the pond for free. You know, like pro-bono work. Been listening around, some people are saying that she’s super good and it’s mainly because of her that the Saje thing has taken off.

st.markdown("And I know what you’re going to ask, miss editor, am I going to contact Lynn Barker and get an interview as well? I’m one step ahead of you, managed to get her on the phone straight away. She was in a meeting so didn’t have much time to talk but seemed really nice. We’ve set up a call for tomorrow morning to go over her involvement with Saje and how she’s helped them out. I think that’ll add a nice touch to the story.")

st.markdown("So, I’ll work on that and send you a first draft of the article by Thursday. Don’t worry, we’ll still get it in next week’s copy.")

st.markdown("Alright, talk to you soon.")

st.markdown("[End of message]")

st. write('***')
st.success("Curious to find out what happens next? You’ll find out more when we meet on campus on Thursday.")
st.subheader("The Fresenians")
