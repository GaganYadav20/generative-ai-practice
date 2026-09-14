# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India")

# print(result.content)

import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()
client = InferenceClient(
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
)

completion = client.chat.completions.create(
    model="zai-org/GLM-OCR:zai-org",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one sentence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
                    }
                }
            ]
        }
    ],
)

print(completion.choices[0].message)