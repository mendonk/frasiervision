import os
from langchain.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
from langchain.vectorstores.astradb import AstraDB
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")
ASTRA_DB_COLLECTION = os.environ.get("ASTRA_DB_COLLECTION")

embedding = OpenAIEmbeddings()
vstore = AstraDB(
    embedding=embedding,
    collection_name="test",
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
)
retriever = vstore.as_retriever(search_kwargs={'k': 3})

prompt_template = """
You are a screenwriter with deep knowledge of the characters described in the context. Write scenes for the characters based on the question.
Context: {context}
Question: {question}
Your answer:
"""
prompt = ChatPromptTemplate.from_template(prompt_template)
model = ChatOpenAI(openai_api_key=OPEN_AI_API_KEY)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

response = chain.invoke("What would happen if Frasier left KACL to work at OpenAI?")
print(response)