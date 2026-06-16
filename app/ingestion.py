from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector

from embeddings import get_embeddings
from config import DB_URI

COLLECTION_NAME = "documents"

def ingest_document(file_path):

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = splitter.split_documents(docs)

    vector_store = PGVector(
        embeddings=get_embeddings(),
        collection_name=COLLECTION_NAME,
        connection=DB_URI,
        use_jsonb=True
    )

    vector_store.add_documents(split_docs)

    print(f"Ingested {len(split_docs)} chunks.")