# RAG System with LangChain + LangGraph + PGVector

## Features

- Document ingestion
- PDF chunking
- Embedding generation
- PGVector storage
- Context retrieval
- LangGraph workflow
- LLM answer generation

---

# Setup

## 1. Start PGVector

```bash
docker compose up -d
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure environment

Create `.env`

```env
OPENAI_API_KEY=your_key
DB_URI=postgresql+psycopg://postgres:postgres@localhost:5432/ragdb
```

---

# Ingestion Example

```python
ingest_document("documents/sample.pdf")
```

Output:

```plaintext
Ingested 24 chunks.
```

---

# Query Example

Input:

```plaintext
What is the main topic of the document?
```

Output:

```plaintext
The document discusses...
```