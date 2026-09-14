# import langchain

# print(langchain.__version__)

# import torch
# val=torch.cuda.is_available()
# print(f"CUDA available: {val}")

from ollama import chat, list as ollama_list, pull, ResponseError

MODEL = 'deepseek-ocr:latest'

try:
    available = [m.model for m in ollama_list().models]
    if MODEL not in available:
        print(f"Model '{MODEL}' not found locally. Pulling...")
        pull(MODEL)

    response = chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': 'Hello!'}],
    )
    print(response.message.content)
except ResponseError as e:
    print(f"Ollama ResponseError: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")