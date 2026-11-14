from langchain_ollama import ChatOllama
model_name = "llama3.2:latest"
temperatures = [0,1.2,3]

for temp in temperatures:
    llm = ChatOllama(model=model_name , temperature=temp)
    response = llm.invoke("What is AI? Reply in one line.")
    print(f"{response.content} - temp: {temp}")