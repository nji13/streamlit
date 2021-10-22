import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Intaractive Widgets')

text = st.text_input('あなたの趣味を教えてください。')
'あなたが好きな趣味は', text, 'です。'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('39832.jpg')
#     st.image(img, caption='PunPun', use_column_width=True)
