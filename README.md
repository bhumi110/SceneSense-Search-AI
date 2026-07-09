# 🎬 SceneSense AI
### AI-Powered Semantic Movie Retrieval using Transformer Embeddings & FAISS

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-MiniLM-orange)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)

</p>

---

## Overview

Finding a movie based only on a vague memory is difficult.

Traditional streaming platforms primarily rely on **movie titles, actors, genres, or keyword matching**, making it impossible to search for movies using descriptions like:

- *"A father sacrifices himself for his family."*
- *"A lonely astronaut stranded in space."*
- *"Friends reunite after many years."*
- *"A detective solves a mysterious murder."*

**SceneSense AI** solves this problem using **Semantic Search**.

Instead of matching keywords, the system understands the **meaning** of the user's query using **Sentence Transformers** and retrieves the most semantically relevant movies using **FAISS Vector Search**.

---

## Features

- Natural Language Movie Search
- Semantic Understanding using Transformer Embeddings
- Fast Vector Similarity Search using FAISS
- Match Percentage Scoring
- Movie Metadata Display
- Human-written Plot Summaries
- Intelligent "No Results Found" Handling
- Interactive Streamlit Interface

---

## Example Search

### User Query

```
A father sacrifices himself for his family.
```

### Output

| Movie | Match |
|--------|-------|
| Interstellar | 91% |
| Logan | 87% |
| The Pursuit of Happyness | 82% |

---

## System Architecture

```
                    User Query
                         │
                         ▼
         Sentence Transformer (MiniLM)
                         │
                  Query Embedding
                         │
                         ▼
              FAISS Vector Database
                         │
          Top-K Similar Movie Vectors
                         │
                         ▼
             Retrieve Movie Metadata
                         │
                         ▼
                 Streamlit Interface
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| NLP | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Search | FAISS |
| Similarity Metric | Cosine Similarity |
| UI | Streamlit |
| Machine Learning | Scikit-Learn |

---

## Project Structure

```
SceneSense/

│
├── app/
│     ├── app.py
│     └── search.py
│
├── data/
│     ├── raw/
│     └── processed/
│            processed_movies.csv
│
├── models/
│     ├── movie_embeddings.npy
│     ├── movie_index.faiss
│     └── sentence_model/
│
├── notebooks/
│     ├── 01_dataset.ipynb
│     ├── 02_embeddings.ipynb
│     ├── 03_search.ipynb
│     └── 04_faiss.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## Dataset

The project uses a **Movie Scripts Corpus**.

Version 1 focuses on **movie metadata** rather than complete scripts.

Important fields:

- Movie Title
- Release Year
- Genres
- Plot
- Plot Outline
- Synopsis

---

## Data Preprocessing

Before generating embeddings, the dataset was cleaned using **Pandas**.

### Steps Performed

- Removed duplicate movies
- Removed missing plots
- Removed incomplete entries
- Selected important columns
- Saved processed dataset

Output:

```
processed_movies.csv
```

---

## Semantic Embedding Generation

Every movie plot is converted into a dense numerical vector using the pre-trained transformer model:

```
all-MiniLM-L6-v2
```

Pipeline

```
Movie Plot
      │
      ▼
Sentence Transformer
      │
      ▼
384-Dimensional Embedding
```

Generated embeddings are stored locally.

```
movie_embeddings.npy
```

---

## Why Sentence Transformers?

Traditional approaches like **TF-IDF** only compare words.

Sentence Transformers capture the **semantic meaning** of complete sentences.

For example,

```
"A father sacrifices himself"

≈

"A parent gives their life to protect family"
```

Although the wording is different, the embeddings are highly similar.

This allows SceneSense AI to retrieve movies based on **meaning rather than exact keywords**.

---

## Semantic Search

Initially, semantic retrieval was implemented using cosine similarity.

Pipeline:

```
User Query
      │
      ▼
Embedding
      │
      ▼
Cosine Similarity
      │
      ▼
Top 5 Movies
```

Although accurate, searching every movie embedding sequentially becomes slower as the dataset grows.

---

## Vector Search using FAISS

To improve scalability and search speed, cosine similarity was replaced by **FAISS**.

Pipeline

```
Movie Embeddings
        │
        ▼
Normalize
        │
        ▼
IndexFlatIP
        │
        ▼
FAISS Index
```

Saved as

```
movie_index.faiss
```

Benefits

- Extremely fast nearest-neighbor search
- Optimized for high-dimensional vectors
- Scales efficiently to thousands of movies
- Production-ready vector retrieval

---

## Search Pipeline

```
User Query
      │
      ▼
Sentence Transformer
      │
      ▼
Query Embedding
      │
      ▼
Normalize
      │
      ▼
FAISS Search
      │
      ▼
Top Matching Movies
      │
      ▼
Retrieve Metadata
      │
      ▼
Streamlit Interface
```

---

## Match Score

Raw cosine similarity values are converted into a more user-friendly percentage.

Example

```
Similarity: 0.91

↓

Match: 91%
```

Displayed as

```
🎯 Match: 91%
```

---

## No Match Handling

If none of the retrieved movies exceed a predefined similarity threshold, the application displays:

```
No similar movies found.

Try describing the movie differently.
```

This avoids returning irrelevant recommendations.

---

## Movie Summary

Instead of generating summaries using a text summarization model, the project utilizes the existing **Plot Outline** available in the dataset.

Reasons:

- Faster inference
- Human-written summaries
- No additional model required
- Lower computational cost

---

## Streamlit Interface

The application provides a clean and minimal interface.

Each search result displays:

- Movie Title
- Release Year
- Genres
- Match Percentage
- Plot Outline

---

## Generated Files

### Processed Dataset

```
processed_movies.csv
```

### Movie Embeddings

```
movie_embeddings.npy
```

### FAISS Index

```
movie_index.faiss
```

### Sentence Transformer Model

```
sentence_model/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/bhumi110/SceneSense-Search-AI.git

cd SceneSense-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app/app.py
```

---

## Libraries Used

| Library | Purpose |
|----------|---------|
| Pandas | Data preprocessing |
| NumPy | Numerical operations |
| Sentence Transformers | Semantic embeddings |
| FAISS | Vector similarity search |
| Scikit-Learn | Initial cosine similarity testing |
| Streamlit | User Interface |

---

## Why FAISS Instead of Cosine Similarity?

| Cosine Similarity | FAISS |
|-------------------|--------|
| Sequential search | Indexed search |
| Slower for large datasets | Optimized nearest-neighbor retrieval |
| Not scalable | Highly scalable |
| Higher search latency | Millisecond-level search |

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Transformer-based Sentence Embeddings
- Semantic Search
- Information Retrieval
- Vector Databases
- Similarity Search
- Data Preprocessing
- Streamlit Application Development

---

## References

- Sentence Transformers: https://www.sbert.net/
- Hugging Face Transformers: https://huggingface.co/
- FAISS: https://github.com/facebookresearch/faiss
- Streamlit: https://streamlit.io/
- Scikit-Learn: https://scikit-learn.org/

---

### ⭐ If you found this project interesting, consider giving it a star!
