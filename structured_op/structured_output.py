from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

llm = ChatOllama(model = "llama3.2:latest")

text = "Im Sanjay , im 20 years old and u can connect me at sanx0064@gmail.com"

# response = llm.invoke(f"Extract name , age and email from the text: {text}")
# print(response.content)
# print(type(response.content))

class Userinfo(BaseModel):
    name : str = Field(description = "Name of the user")
    age : int = Field(description = "Age of the user")
    email : str = Field(description = "Email of the user")

structured_llm = llm.with_structured_output(Userinfo)
response = structured_llm.invoke(f"Extract name , age and email from the text: {text}")
# print(response)
# print(type(response))

dis_output = response.model_dump()

print(dis_output)