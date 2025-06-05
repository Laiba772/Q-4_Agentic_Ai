"""
Module demonstrating LiteLLM, a library for simplifying interactions with various Large Language Model (LLM) APIs.

LiteLLM provides a unified interface to call different AI models like OpenAI, Claude, and others with minimal configuration.
"""

# LiteLLM is a simple and fast way to call different LLM APIs (like OpenAI, Claude, etc.).


# 03_litellm_openai_agent/litellm_example.py

from litellm import completion

# To use LiteLLM, you need to install it first.
# You can install it using pip:
# pip install litellm


response = completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello from LiteLLM!"}],
    api_key="<YOUR_API_KEY>"
)

print(response['choices'][0]['message']['content'])
