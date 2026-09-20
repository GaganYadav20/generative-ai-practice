from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

class Review(BaseModel):
    summary: str = Field(description="A concise summary of the review")
    sentiment: str = Field(description="The sentiment expressed in the review")
    
structured_output=model.with_structured_output(Review)

result=structured_output.invoke(""" the hardware is great . but the software feels bloated . there are too many pre-installed apps that I can't remove . Also the UI looks outeted campare to other brands Hoping for a software Update  to fix this""")

print(result)
print(result['summ'])