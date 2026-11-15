from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


llm = ChatOllama(model="llama3.2:latest")
parser = StrOutputParser()

question_prompt_template = ChatPromptTemplate.from_template("Explain simply in 3 line : {question}")

rate_prompt_template = ChatPromptTemplate.from_template(
    "Question: {question} \nAnswer: {answer}\n\n"
    "Rate the answer for a 15-year old kid.From 1 to 10 .With one line feedback"
)

explain_chain = question_prompt_template | llm | parser

# result = explain_chain.invoke({"question": "What is Gravity?"})

feedback_chain = (
    RunnablePassthrough.assign(answer = explain_chain) | rate_prompt_template | llm | parser
)
print(feedback_chain.invoke({"question": "What is Gravity?"}))