import streamlit as st
from PIL import Image

st. set_page_config(layout="wide") 
#image = Image.open("C:\\Users\\divya\\OneDrive\\Desktop\\me\\AKKA\\Us.JPG")
image = Image.open("/home/meet/app/Us.JPG")

st.image(image, caption='Just The Four Of Us')
st.markdown("My heart blooms with joy having you as my sister in my life. One sister to another, one woman to another- you are the best! I know that at the end of the day, my sister will always look up to me and make sure my comfort and journey are smooth. I love you so much. Thank you for being with me. They say having a best friend is the best thing one can ask for. I say having a best friend in a sister is the most blessing thing for one. You are the best, my sister. Take care. You may think I am happy to share my clothes and makeup with you. The truth is, I love sharing my childhood with you the most. Thank you for being my sister. I sometimes wonder how God knew that I needed a sister exactly like you. Strong, passionate, and kind- all in one body. Take my unlimited love and respect, sissy. I am put in this world because you are here for me, standing strong to support your sister against and for everything. Thank you, love.")
st. write('***')
