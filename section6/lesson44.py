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

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

print("===== Describe an image - remote =====")
description_results = computervision_client.describe_image(remote_image_url)

print("Description of remote image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))