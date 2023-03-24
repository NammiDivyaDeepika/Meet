import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')
with col2:
    image = Image.open("Saje.png")
    st.image(image)
with col3:
    st.write(' ')

st.success("Congratulations…! You are just one step away from solving the mystery. Your persistence and analytical skills have led you to this point, and there is no doubt that you will be successful in completing this final task.")
col4, col5, col6, col7, col8,= st.columns(3)

with col4:
    st.write(' ')
with col5:
    st.write(' ')
with col6:  
    if st.button('Scan Me'):
             qr_image = Image.open('QR.jpg')
             st.image(qr_image, width=200)
    else:
             st.write('Click the button to scan the QR code')
with col7:
    st.write(' ')
with col8:
    st.write(' ')
    
    

st.subheader("The Fresenians")
