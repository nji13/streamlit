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

with open('secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

## ローカルファイルに対応させる

local_image_path = 'sample01.jpg'
local_image = open(local_image_path, "rb")

print("===== Detect Objects - local =====")
detect_objects_results = computervision_client.detect_objects_in_stream(local_image)

print("Detecting objects in local image:")
if len(detect_objects_results.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results.objects:
        print("object at location {}, {}, {}, {}".format( \
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))