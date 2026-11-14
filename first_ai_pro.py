import ollama

modell = "llama3.2:latest"
promptt = "Explain me gen ai in one line"
r= ollama.generate(model = modell , prompt = promptt)
print(r.response)