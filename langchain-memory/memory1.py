from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(model="gpt-4o")

history=[]
while True:
    query=input("user: ")
    if query.lower() in ["exit","bye","stop"]:
        print("Good Bye")
        break
    
    history.append({"role":"user","content":query})
    print("user: ",query)
    
    res=llm.invoke(history)
    history.append({"role":"ai","content":res.text})
    print("AI: ",res.text)
