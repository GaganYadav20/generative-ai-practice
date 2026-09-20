from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash")

out=StrOutputParser()

prompts=ChatPromptTemplate([
    {"role":"system","content":"You are a translator and translate input into {language}"},
    {"role":"user","content":"{query}"}
])

def tranform(result:str):
    return result.upper()

chains= prompts | llm | out | tranform

result=chains.invoke({"language":"hinglish","query":"I love langchain ?"}) 

print(result)