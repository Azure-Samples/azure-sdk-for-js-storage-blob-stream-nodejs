import logging
import time
import os

import azure.functions as func
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes


# Authentication
subscription_key = ""
endpoint = "https://eastus2.api.cognitive.microsoft.com/"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def preprocess(input):        
    nutrition_info = dict()
    desired_fields = ['Total Carbohydrate', 'Total Fat', 'Protein', 'Calories']
    
    for text_result in input:
        for i, line in enumerate(text_result.lines):
            for desired_field in desired_fields:
                if desired_field in line.text:         
                    if desired_field == 'Calories':
                        nutrition_info[desired_field] = text_result.lines[i+1].text
                    else:
                        nutrition_info[desired_field] = line.text.split[-1]
    
    return nutrition_info

def perform_ocr(blob_uri):
    print("===== Read File - remote =====")

    # Call API with URL and raw response (allows you to get the operation location)
    read_response = computervision_client.read(blob_uri, raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    return read_result


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    read_result = perform_ocr(myblob.uri)
    print(read_result.analyze_result.read_results)
    if read_result.status == OperationStatusCodes.succeeded:
        nutrition_data = preprocess(read_result.analyze_result.read_results)
        print(nutrition_data)