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

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def detect_objects(filepath):
    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    print(objects[0].rectangle.x)
    return objects

filepath = 'sample01.jpg'
detect_objects(filepath)