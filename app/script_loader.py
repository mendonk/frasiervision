import os
from langchain.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
from langchain.vectorstores.astradb import AstraDB
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
OPEN_AI_API_KEY = os.environ.get("OPENAI_API_KEY")
ASTRA_DB_COLLECTION = "test"

embedding = OpenAIEmbeddings()
vstore = AstraDB(
    embedding=embedding,
    collection_name="test",
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
)

folder_path = './pdfs'
loader = PyPDFDirectoryLoader("./pdfs")
docs = loader.load_and_split()

inserted_ids = vstore.add_documents(docs)
