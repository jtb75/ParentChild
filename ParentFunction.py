import json
import boto3
 
# Define the client to interact with AWS Lambda
client = boto3.client('lambda')
 
def lambda_handler(event,context):
 
    # Define the input parameters that will be passed
    # on to the child function
    inputParams = {
        "ProductName"   : "iPhone SE",
        "Quantity"      : 2,
        "UnitPrice"     : 499
    }
 
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-2:184001509516:function:ChildFunction',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
 
    responseFromChild = json.load(response['Payload'])
 
    print('\n')
    print(responseFromChild)