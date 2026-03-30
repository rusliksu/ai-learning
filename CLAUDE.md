# CLAUDE.md — AI Learning Project

> Общие правила: `~/.claude/rules/shared.md` (загружаются автоматически)

## Контекст проекта
- **Цель:** Освоить AI/ML инструменты, Python, возможная монетизация навыков
- **Бэкграунд:** Java, Spring Boot, PostgreSQL, базовый опыт с LLM (ChatGPT, Claude, RAG)
- **Инструменты:** Claude Pro, DeepSeek API, n8n.cloud

## Правила проекта
- Объяснять концепции простым языком, учитывая Java-бэкграунд
- При создании ноутбуков добавлять `%matplotlib inline` в первую ячейку
- Проводить параллели между Java и Python где уместно
- Фокус на практических примерах, а не теории

## Структура проекта

```
AI learning/
├── CLAUDE.md
├── notebooks/
│   ├── 01_basics/            # Pandas, визуализация
│   ├── 02_machine_learning/  # scikit-learn, классическое ML
│   ├── 03_neural_networks/   # TensorFlow, CNN, RNN, GAN, VAE
│   └── 04_llm_api/           # Claude API, OpenAI API
├── data/                     # Датасеты и CSV файлы
└── docs/                     # Документация и роадмап
```

## Текущий прогресс

### Освоено:
- [x] Python окружение (3.12.7)
- [x] Pandas, Matplotlib/Seaborn, scikit-learn
- [x] TensorFlow/Keras, CNN, RNN/LSTM, Transformer
- [x] GAN, Autoencoder, VAE
- [x] RAG (базовый + Advanced: Multi-Query, HyDE, Reranking, CRAG/LangGraph)

### Следующие темы:
- [ ] LangChain / LlamaIndex
- [ ] API интеграции (OpenAI, Anthropic, DeepSeek)
- [ ] Reinforcement Learning
- [ ] Fine-tuning моделей
- [ ] Деплой моделей (Streamlit, FastAPI)

## Полезные команды

```bash
jupyter notebook "C:\Users\Ruslan\Desktop\AI learning"
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow jupyter
```

---
*Обновлено: 12.01.2026*
