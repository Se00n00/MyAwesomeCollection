# Agentic RAG using LangGraph

[![LangGraph](https://img.shields.io/badge/LangGraph-1.0.2-blue?logo=python\&logoColor=white)]()
[![LangChain](https://img.shields.io/badge/LangChain-1.0.4-ff6f00?logo=chainlink\&logoColor=white)]()
[![LangChain OpenAI](https://img.shields.io/badge/LangChain%20OpenAI-1.0.2-412991?logo=openai\&logoColor=white)]()
[![Pydantic](https://img.shields.io/badge/Pydantic-2.11.10-006dad?logo=fastapi\&logoColor=white)]()
[![ChromaDB](https://img.shields.io/badge/ChromaDB-1.3.4-009688?logo=databricks\&logoColor=white)]()
[![HuggingFace Tokenizers](https://img.shields.io/badge/HF%20Tokenizers-0.22.1-ffcc00?logo=huggingface\&logoColor=white)]()
[![PyPDF](https://img.shields.io/badge/PyPDF-6.1.3-8b0000?logo=adobeacrobatreader\&logoColor=white)]()
[![Gradio](https://img.shields.io/badge/Gradio-5.49.1-0096ff?logo=gradio\&logoColor=white)]()
[![OpenAI](https://img.shields.io/badge/OpenAI-Supported-412991?logo=openai\&logoColor=white)]()
[![Gemini](https://img.shields.io/badge/Gemini-Supported-1a73e8?logo=google\&logoColor=white)]()
[![Claude](https://img.shields.io/badge/Claude-Supported-111?logo=anthropic\&logoColor=white)]()
[![Groq](https://img.shields.io/badge/Groq-Supported-f53151?logo=groq\&logoColor=white)]()
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Supported-ffcc00?logo=huggingface\&logoColor=white)]()

---

An agent-driven Retrieval-Augmented Generation (RAG) pipeline with planning, reflection, structured workflows, evaluation, and a Gradio UI.
<p align="center"> <img src="https://github.com/Se00n00/MyAwesomeCollection/blob/notebooks/rag/AgenticRag.png" width="600" /> </p>

---

## Overview

This project implements an **Agentic RAG system** using **LangGraph**, where every step of the workflow behaves as an intelligent agentic node. Instead of a single-pass RAG, the system **plans**, **retrieves**, **answers**, and **reflects** on its own outputs—allowing more structured reasoning, higher factual correctness, and improved explainability.

The notebook (`Agentic_RAG.ipynb`) demonstrates:

* **Planning**: Interpret the query and decide whether retrieval is needed
* **Retrieval**: Use a local vector DB (Chroma) to fetch relevant context
* **Answering**: Generate responses using any LLM (OpenAI, Gemini, Claude, Groq, HF models)
* **Reflection**: Evaluate completeness & relevance before returning the final answer
* **Step-by-step logging** for all nodes
* **Gradio UI** for simple interactive querying
* **RAG Evaluation** using LLM-as-a-judge (LangSmith)

---

## Directory Contents

| File                            | Description                                                                         | Link |
| ------------------------------- | ----------------------------------------------------------------------------------- |------|
| **Agentic_RAG.ipynb**           | Main notebook containing the full Agentic RAG implementation.                       |[<img src="https://colab.research.google.com/assets/colab-badge.svg" height="20">](https://colab.research.google.com/drive/1hhOvyiK-M8-tLy4L4EKdCNaIRZ_iL__B?usp=sharing)
| **rag_evaluation-fee40206.csv** | LangSmith evaluation results for correctness, groundedness, relevance, and latency. |[<img src="https://img.shields.io/badge/GitHub-View-blue" height="20">](https://github.com/Se00n00/MyAwesomeCollection/blob/notebooks/rag/rag_evaluation-fee40206.csv)

---

## 🧠 How the Agentic Workflow Works

A traditional RAG pipeline simply retrieves documents and generates an answer.
This **Agentic RAG** extends this by introducing **intent-driven decision-making and self-reflection**:

### **1️⃣ Plan Node**

* Interprets the query
* Decides whether retrieval is necessary
* Routes the workflow accordingly

### **2️⃣ Retrieve Node**

* Uses **ChromaDB** as a local vector store
* Embeddings generated via HuggingFace models
* Works with any small dataset, PDFs, or text files

### **3️⃣ Answer Node**

* Combines query + retrieved docs
* Generates the response using your chosen LLM provider

### **4️⃣ Reflect Node**

* Performs a self-evaluation step
* Judges completeness, factual grounding, and relevance
* Can trigger revisions or confidence scoring

### **Result:**

A more **accurate**, **traceable**, and **self-correcting** RAG pipeline.

---

## 📊 RAG Evaluation Results (LLM-as-a-Judge)

The `rag_evaluation-fee40206.csv` file summarizes evaluation metrics computed using **LangSmith**.

### **📈 Summary Table**

| Metric                    | Score         |
| ------------------------- | ------------- |
| **Correctness (AVG)**     | **0.875**     |
| **Groundedness (AVG)**    | **0.875**     |
| **Relevance (AVG)**       | **0.8824**    |
| **Retrieval Score (AVG)** | **1.00**      |
| **Latency (P50)**         | **9.422 sec** |

🔎 *Retrieval score of 1.00 indicates perfect retrieval quality for the provided dataset.*

---
