from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import json

# subscription_key = "55616db4725f4e1494ad4f219c9ed4c0"
# endpoint = "https://udemy-20211014.cognitiveservices.azure.com/"
# ↑keyとendpointを直接入れる。見られたくない場合は、↓jsonファイルに記述して読み込みする
with open('secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY'] # JSONファイルに入っているAPI Key情報
ENDPOINT = secret['ENDPOINT'] # JSONファイルに入っているAPI endpointを取得

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def get_tags(filepath):
    local_image = open(filepath, "rb")

    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

def detect_objects(filepath):
    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects

import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont

st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg','png'])

if uploaded_file is not None:   # uploaded_file に何か入っていたら起動する
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    #描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype(font='./Helvetica 400.ttf', size=50)
        text_w, text_h = draw.textsize(caption, font=font)
        
        draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=5)
        draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
        draw.text((x, y), caption, fill='white', font=font)

    st.image(img)

    st.markdown('**認識されたコンテンツタグ**')
    st.markdown('>apple')
