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
GOOGLE_API_KEY=your_key
DB_URI=postgresql+psycopg://postgres:postgres@localhost:5432/ragdb
```

---

# Ingestion Example

<img width="1466" height="212" alt="image" src="https://github.com/user-attachments/assets/fe6432cc-dafc-4760-8ce1-b82cbca73ba4" />


---

# Query Example

<img width="1466" height="756" alt="image" src="https://github.com/user-attachments/assets/bff71aa1-5fb2-4264-b02b-29b2a3ab6824" />

```plaintext
The document discusses...
```
