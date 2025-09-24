import boto3
import json

prompt_data = """
Give me pointwise ways to live life to fullest.
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {

    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

body = json.dumps(payload)
model_id="meta.llama3-70b-instruct-v1:0"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

print("\n")
print("Response: ")
print(response)
print("\n")



response_body = json.loads(response.get("body").read())
print("Response Body: ")
print(response_body)
print("\n")


response_text = response_body['generation']
print("Response Text Part: ")
print(response_text)