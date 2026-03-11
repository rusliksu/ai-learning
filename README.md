# AI/ML Learning

![Python](https://img.shields.io/badge/Python-3.12-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![PyTorch](https://img.shields.io/badge/PyTorch-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-blue)
![LangChain](https://img.shields.io/badge/LangChain-green)
![LangGraph](https://img.shields.io/badge/LangGraph-purple)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

A hands-on repository for learning machine learning, neural networks, LLM integrations, and RAG systems. The journey goes from Python and pandas fundamentals to production-ready RAG and multi-agent architectures with LangGraph.

**Author:** Java Backend Developer (Spring Boot, PostgreSQL, Kafka, gRPC) expanding into the AI/ML stack.

## Tech Stack

- **Language:** Python 3.12
- **ML/DL:** scikit-learn, TensorFlow/Keras, PyTorch
- **LLM:** LangChain, LangGraph, OpenAI API, Anthropic API, DeepSeek API
- **RAG:** ChromaDB, Sentence Transformers, BM25, hybrid search
- **Data:** pandas, NumPy, Matplotlib, Seaborn
- **Infra:** Docker, Docker Compose, Jupyter Notebook

## Project Structure

```
notebooks/
├── 01_basics/               # pandas, Seaborn, procurement audit analytics
├── 02_machine_learning/     # scikit-learn, classification (RandomForest, Iris)
├── 03_neural_networks/      # CNN (MNIST), RNN/LSTM (IMDB), GAN, VAE, Autoencoder
├── 04_llm_api/              # Claude API, DeepSeek API — calls and integration
├── 05_rag/                  # RAG: theory + implementation (ChromaDB, BM25, hybrid search)
├── 06_langchain/            # LangChain: chains, prompt templates, LCEL, memory, tools
├── 07_agents/               # AI agents: ReAct, tool calling, LangChain Agents
├── 08_langgraph/            # LangGraph: state graphs, checkpoints, multi-agent, supervisor
├── 09_rag_project/          # RAG chatbot: end-to-end project
├── 10_production_rag/       # Production RAG: chunking strategies, embeddings, vector stores
data/                        # Datasets (CSV)
docker/                      # Docker/Compose examples and guide
docs/                        # Learning roadmap
```

## Modules

| # | Module | Description |
|---|--------|-------------|
| 01 | Basics | Pandas, Seaborn, visualization, procurement audit pipeline |
| 02 | Machine Learning | Classical ML: RandomForest, classification, metrics |
| 03 | Neural Networks | CNN, RNN/LSTM, Transformer, GAN, VAE, Autoencoder |
| 04 | LLM API | Working with APIs: Claude (Anthropic), DeepSeek |
| 05 | RAG | Retrieval Augmented Generation: vector and hybrid search |
| 06 | LangChain | Chains, prompt templates, LCEL, memory, output parsers, tools |
| 07 | Agents | AI agents: ReAct, tool calling, orchestration |
| 08 | LangGraph | State graphs, checkpoints, multi-agent, supervisor, subgraphs |
| 09 | RAG Project | End-to-end RAG chatbot |
| 10 | Production RAG | Chunking strategies, embedding models, vector stores |

## Getting Started

```bash
# Clone the repository
git clone https://github.com/rusliksu/ai-learning.git
cd ai-learning

# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow torch \
  langchain langchain-community chromadb sentence-transformers rank_bm25 \
  openai anthropic jupyter

# Copy the environment file
cp .env.example .env
# Add your API keys to .env

# Launch Jupyter
jupyter notebook
```

## Status

Active learning project. Modules 01--08 are complete, 09--10 are in progress.
