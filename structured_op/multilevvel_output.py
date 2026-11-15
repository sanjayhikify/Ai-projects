from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import List

llm = ChatOllama(model = "llama3.2:latest")

class Book(BaseModel):
    name : str = Field(description = "Name of the book")
    author : str = Field(description = "Author of the book")
    publication_year : int = Field(description = "Publication year of the book")

# structured_llm = llm.with_structured_output(Book)

# response = structured_llm.invoke("Suggest one well known sci-fi book")
# print(response)

class BookCollection(BaseModel):
    book : List[Book] = Field(description = "List of books in the collection")

structured_llm = llm.with_structured_output(BookCollection)
response = structured_llm.invoke("Suggest 3 well known sci-fi books")   
print(response)