import ollama

message = [
    {   "role" : "system",
        "content" : "Your a funny little boy , answer in on line"

    },
    {
        "role" : "user",
        "content" : "What is LLM ?"
    }
]

modell = "llama3.2:latest"
res = ollama.chat(model = modell, messages = message)
print(res.message.content)