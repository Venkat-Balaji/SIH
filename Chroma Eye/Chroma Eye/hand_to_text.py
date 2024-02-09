import os
import io
import time
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import  OperationStatusCodes, VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont


API_KEY = "afc7729a5b164a6c990b64d3bb00409d"
ENDPOINT = "https://ocr-reader-krish.cognitiveservices.azure.com/"

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))


response = cv_client.read_in_stream(open("C:/Users/skk12/Downloads/WhatsApp Image 2022-03-29 at 4.51.27 PM (1).jpeg", 'rb'),language='en', raw=True)
operationLocation = response.headers['Operation-Location']
operation_id = operationLocation.split('/')[-1]
time.sleep(7)
result = cv_client.get_read_result(operation_id)

print(result)
print(result.status)
print(result.analyze_result) 

with open("offline.txt", 'a') as fileobject:
    if result.status == OperationStatusCodes.succeeded:
        read_results = result.analyze_result.read_results
        for analyzed_result in read_results:
            for line in analyzed_result.lines:
                fileobject.write(line.text)
                fileobject.write("\n")