# AI/ML Learning

Репозиторий для изучения машинного обучения, нейронных сетей, LLM-интеграций и RAG-систем. Путь от основ Python и pandas до production-ready RAG и мульти-агентных архитектур на LangGraph.

**Автор:** Java Backend Developer (Spring Boot, PostgreSQL, Kafka, gRPC), осваивающий AI/ML стек.

## Стек

- **Язык:** Python 3.12
- **ML/DL:** scikit-learn, TensorFlow/Keras, PyTorch
- **LLM:** LangChain, LangGraph, OpenAI API, Anthropic API, DeepSeek API
- **RAG:** ChromaDB, Sentence Transformers, BM25, гибридный поиск
- **Данные:** pandas, NumPy, Matplotlib, Seaborn
- **Инфра:** Docker, Docker Compose, Jupyter Notebook

## Структура

```
notebooks/
├── 01_basics/               # pandas, Seaborn, аналитика закупок
├── 02_machine_learning/     # scikit-learn, классификация (RandomForest, Iris)
├── 03_neural_networks/      # CNN (MNIST), RNN/LSTM (IMDB), GAN, VAE, Autoencoder
├── 04_llm_api/              # Claude API, DeepSeek API — вызовы и интеграция
├── 05_rag/                  # RAG: теория + реализация (ChromaDB, BM25, гибридный поиск)
├── 06_langchain/            # LangChain: chains, prompt templates, LCEL, memory, tools
├── 07_agents/               # AI-агенты: ReAct, tool calling, LangChain Agents
├── 08_langgraph/            # LangGraph: графы, checkpoints, multi-agent, supervisor
├── 09_rag_project/          # RAG-чатбот: end-to-end проект
├── 10_production_rag/       # Production RAG: chunking-стратегии, embeddings, vector stores
data/                        # Датасеты (CSV)
docker/                      # Docker/Compose примеры, гайд
docs/                        # Роадмап обучения
```

## Модули

| # | Модуль | Описание |
|---|--------|----------|
| 01 | Basics | Pandas, Seaborn, визуализация, пайплайн аудита закупок |
| 02 | Machine Learning | Классическое ML: RandomForest, классификация, метрики |
| 03 | Neural Networks | CNN, RNN/LSTM, Transformer, GAN, VAE, Autoencoder |
| 04 | LLM API | Работа с API: Claude (Anthropic), DeepSeek |
| 05 | RAG | Retrieval Augmented Generation: векторный и гибридный поиск |
| 06 | LangChain | Chains, prompt templates, LCEL, memory, output parsers, tools |
| 07 | Agents | AI-агенты: ReAct, tool calling, оркестрация |
| 08 | LangGraph | Графы состояний, checkpoints, multi-agent, supervisor, subgraphs |
| 09 | RAG Project | End-to-end RAG-чатбот |
| 10 | Production RAG | Chunking-стратегии, embedding-модели, vector stores |

## Запуск

```bash
# Клонировать
git clone https://github.com/rusliksu/ai-learning.git
cd ai-learning

# Установить зависимости
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow torch \
  langchain langchain-community chromadb sentence-transformers rank_bm25 \
  openai anthropic jupyter

# Скопировать .env
cp .env.example .env
# Указать API-ключи в .env

# Запустить Jupyter
jupyter notebook
```

## Статус

Активный учебный проект. Модули 01--08 завершены, 09--10 в процессе.
