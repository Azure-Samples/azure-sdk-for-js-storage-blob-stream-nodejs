import logging
import time
import uuid

import azure.functions as func
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cosmos import CosmosClient, PartitionKey


# Azure Computer Vision Authentication
computervision_subscription_key = ""
computervision_endpoint = "https://eastus2.api.cognitive.microsoft.com/"
computervision_client = ComputerVisionClient(computervision_endpoint, CognitiveServicesCredentials(computervision_subscription_key))

# Azure CosmosDB Authentication
cosmosdb_subscription_key = ""
cosmosdb_endpoint = "https://nutrition-info.documents.azure.com:443/"
cosmosdb_client = CosmosClient(url=cosmosdb_endpoint, credential=cosmosdb_subscription_key)


def db_write(nutrition_data):
    database = cosmosdb_client.create_database_if_not_exists(id="nutrition_data")
    partitionKeyPath = PartitionKey(path="/id")
    container = database.create_container_if_not_exists(id="label-images", partition_key=partitionKeyPath)
    container.create_item(nutrition_data)


def preprocess(input):        
    nutrition_info = {'id' : str(uuid.uuid4())}
    desired_fields = ['Total Carbohydrate', 'Total Fat', 'Protein', 'Calories']
    
    for text_result in input:
        for i, line in enumerate(text_result.lines):
            for desired_field in desired_fields:
                if desired_field in line.text:         
                    if desired_field == 'Calories':
                        nutrition_info[desired_field] = text_result.lines[i+1].text
                    else:
                        nutrition_info[desired_field] = line.text.split()[-1]
    
    return nutrition_info


def perform_ocr(blob_uri):
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
    
    # Perform OCR
    read_result = perform_ocr(myblob.uri)    
    
    # If OCR is successful, preprocess result and write to CosmosDB
    if read_result.status == OperationStatusCodes.succeeded:
        nutrition_data = preprocess(read_result.analyze_result.read_results)
        nutrition_data['timestamp'] = read_result.created_date_time
        
        db_write(nutrition_data)