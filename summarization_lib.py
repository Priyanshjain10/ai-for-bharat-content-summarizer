"""Core Summarization Library using Amazon Bedrock

This module provides the core functionality for text summarization
using AWS Bedrock's Claude AI models.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Initialize Bedrock Runtime client
try:
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1'
    )
except Exception as e:
    print(f"Error initializing Bedrock client: {e}")
    bedrock_runtime = None


def get_text_summary(text_content: str) -> str:
    """
    Generate a summary of the provided text using Amazon Bedrock Claude.
    
    Args:
        text_content (str): The text content to summarize
        
    Returns:
        str: The generated summary
        
    Raises:
        Exception: If there's an error in the summarization process
    """
    
    if not bedrock_runtime:
        raise Exception("Bedrock Runtime client not initialized. Please check your AWS credentials.")
    
    if not text_content or len(text_content.strip()) == 0:
        raise ValueError("Text content cannot be empty")
    
    # Prepare the prompt for Claude
    prompt = f"""Human: Please provide a comprehensive summary of the following text. 
Focus on the key points, main ideas, and important details. 
Keep the summary concise but informative.

Text to summarize:
{text_content}

Assistant:"""
    
    # Configure the request body for Claude
    request_body = {
        "prompt": prompt,
        "max_tokens_to_sample": 1000,
        "temperature": 0.5,
        "top_p": 0.9,
        "top_k": 250,
        "stop_sequences": ["\n\nHuman:"]
    }
    
    try:
        # Invoke the Bedrock model
        response = bedrock_runtime.invoke_model(
            modelId='anthropic.claude-v2',
            contentType='application/json',
            accept='application/json',
            body=json.dumps(request_body)
        )
        
        # Parse the response
        response_body = json.loads(response['body'].read())
        summary = response_body.get('completion', '').strip()
        
        if not summary:
            raise Exception("Empty response from Bedrock")
        
        return summary
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        raise Exception(f"AWS Bedrock Error ({error_code}): {error_message}")
        
    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing Bedrock response: {str(e)}")
        
    except Exception as e:
        raise Exception(f"Unexpected error during summarization: {str(e)}")


def get_summarization_stats(original_text: str, summary: str) -> dict:
    """
    Calculate statistics about the summarization.
    
    Args:
        original_text (str): The original text
        summary (str): The generated summary
        
    Returns:
        dict: Dictionary containing summarization statistics
    """
    
    original_words = len(original_text.split())
    summary_words = len(summary.split())
    reduction_percentage = round((1 - summary_words / original_words) * 100, 2) if original_words > 0 else 0
    
    return {
        'original_word_count': original_words,
        'summary_word_count': summary_words,
        'reduction_percentage': reduction_percentage,
        'original_char_count': len(original_text),
        'summary_char_count': len(summary)
    }


def summarize_with_custom_params(text_content: str, max_tokens: int = 500, temperature: float = 0.5) -> str:
    """
    Generate a summary with custom parameters.
    
    Args:
        text_content (str): The text content to summarize
        max_tokens (int): Maximum tokens for the summary (default: 500)
        temperature (float): Temperature for response randomness (default: 0.5)
        
    Returns:
        str: The generated summary
    """
    
    if not bedrock_runtime:
        raise Exception("Bedrock Runtime client not initialized")
    
    prompt = f"""Human: Summarize this text concisely:

{text_content}

Assistant:"""
    
    request_body = {
        "prompt": prompt,
        "max_tokens_to_sample": max_tokens,
        "temperature": temperature,
        "top_p": 0.9
    }
    
    try:
        response = bedrock_runtime.invoke_model(
            modelId='anthropic.claude-v2',
            contentType='application/json',
            accept='application/json',
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response['body'].read())
        return response_body.get('completion', '').strip()
        
    except Exception as e:
        raise Exception(f"Error in custom summarization: {str(e)}")


# Model information
MODEL_INFO = {
    'model_id': 'anthropic.claude-v2',
    'provider': 'Anthropic',
    'model_name': 'Claude v2',
    'description': 'Advanced language model for text analysis and generation'
}
