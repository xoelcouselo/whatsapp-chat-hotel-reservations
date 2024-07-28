import boto3
import requests
import json

# Set your API keys for Calendly
calendly_api_key = "YOUR_API_KEY"
calendly_api_secret = "YOUR_API_SECRET"

def lambda_handler(event, context):
    # Event data (replace with your own)
    event_data = {
        'type': 'call',
        'title': event['titulo'],
        'description': '',
        'start_time': event['fecha_y_hora'].replace('Z', ''),  # Start time in ISO format
        'end_time': event['fecha_y_hora'].replace('Z', ''),  # End time in ISO format
        'timezone': 'America/Bogota',
        'guest_access': True,
        'notify': True,
        'reminder': 'none'
    }

    # Make a POST request to create an event
    url = f"https://api.calendly.com/r/{calendly_api_key}/events"
    response = requests.post(url, headers={'Content-Type': 'application/json'}, json=event_data)

    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Event created successfully. ID of the event: ' + response.json()['id']})
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error creating the event: ' + response.text})
        }

# Configure the Lambda function
def lambda_handler(event, context):
    # This is an infinite loop that will cause the function to run indefinitely
    return lambda_handler(event, context)