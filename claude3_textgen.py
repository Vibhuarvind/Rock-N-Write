import boto3
import json

# Your prompt
prompt_data = """
Give me pointwise ways to live life to fullest.
"""

# Create Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Correct payload for Claude 3 using Messages API
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,  # Required field at top level
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt_data}]
        }
    ],
    "temperature": 0.8,
    "top_p": 0.8
}

# Convert payload to JSON string
body = json.dumps(payload)

# Model ID (Claude 3 Sonnet)
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
accept = 'application/json'
contentType = 'application/json'

try:
    # Invoke the model
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=contentType
    )

    print("\nResponse: ")
    print(response)
    print("\n")

    # Read and parse the response body
    response_body = json.loads(response.get('body').read())
    print("Response Body: ")
    print(response_body)
    print("\n")

    # Extract the assistant's reply - correct path for Claude 3
    response_text = response_body['content'][0]['text']
    print("Response Text: ")
    print(response_text)

except Exception as e:
    print(f"Error: {e}")
    print("Make sure you have proper AWS credentials and permissions for Bedrock.")