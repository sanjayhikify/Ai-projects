from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
modell = "llama3.2:latest"
prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a friendly {subject} teacher.Explain me in simple under 80 words with one real life example."),
    ("user","{question}")
])

prompt = prompt_template.invoke({
    "subject":"Physics",
    "question":"What is gravity?"
})

llm = ChatOllama(model = modell)
res = llm.invoke(prompt)
parser = StrOutputParser()
res = parser.invoke(res)
print(res)
