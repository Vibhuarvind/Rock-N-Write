# AWS Bedrock Claude 3 Demo

This repository demonstrates how to use **AWS Bedrock** to interact with **Anthropic Claude 3** using Python (`boto3`). The script sends a prompt as a conversation and retrieves the model’s response using the **Messages API**, which is required for Claude 3.


## Features
- Send prompts to Claude 3 via **Messages API**
- Set inference parameters like `max_tokens`, `temperature`, and `top_p`
- Extract and print assistant responses in Python
- Compatible with AWS Bedrock models once access is granted

## Requirements
- Python 3.8+
- `boto3` installed (`pip install boto3`)
- AWS account with Bedrock access and permissions for Claude 3 and llama 3

## Notes
Claude 3 requires Messages API, not the old prompt/completion style.
Ensure your AWS IAM user/role has Bedrock model access.
