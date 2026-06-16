from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_postgres import PGVector
from langchain_community.embeddings import HuggingFaceEmbeddings

from embeddings import get_embeddings
from config import DB_URI

load_dotenv()

# Embeddings
embeddings = get_embeddings()

# Vector store
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="documents",
    connection=DB_URI,
    use_jsonb=True
)

retriever = vector_store.as_retriever()

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

def retrieve_context(state: dict) -> dict:
    """Retrieve context documents for the given question."""
    question = state["question"]
    docs = retriever.invoke(question)
    context = []
    for doc in docs:
        if hasattr(doc, "page_content"):
            context.append(doc.page_content)
        else:
            context.append(str(doc))
    return {"context": context}

def generate_answer(state: dict) -> dict:
    """Generate an answer based on the question and context."""
    question = state["question"]
    context = state["context"]
    # Format context as a single string
    context_str = "\n\n".join(context)
    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context_str}

    Question:
    {question}
    """
    response = llm.invoke(prompt)
    return {"answer": response.content}