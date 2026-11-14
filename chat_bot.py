import ollama

message = [
    {
        "role" : "system",
        "content" : "You are a friendly assitant"
    }
]
modell = "llama3.2:latest"
while True:
    user_prompt = input("You: ")
    if(user_prompt.lower()=="bye"):
        break
    user_role = {
            "role" : "user",
            "content" : user_prompt
        }
    message.append(user_role)
    res = ollama.chat(model = modell , messages = message)
    res = res.message.content
    print("San's Assistant: ", res , "\n")
    assitant_role = {
        "role": "assistant",
        "content" : res
    }
    message.append(assitant_role)