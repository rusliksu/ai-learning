# AI Learning Project - Инструкции для Claude

## Контекст проекта
- **Владелец:** Руслан, Java Backend разработчик (Middle, Сбер)
- **Цель:** Освоить AI/ML инструменты, Python, возможная монетизация навыков
- **Бэкграунд:** Java, Spring Boot, PostgreSQL, базовый опыт с LLM (ChatGPT, Claude, RAG)
- **Инструменты:** Claude Pro, DeepSeek API, n8n.cloud

## Правила для Claude
- Всегда отвечать на русском языке
- Объяснять концепции простым языком, учитывая Java-бэкграунд
- При создании ноутбуков добавлять `%matplotlib inline` в первую ячейку
- Проводить параллели между Java и Python где уместно
- Фокус на практических примерах, а не теории

## Структура проекта

```
AI learning/
├── CLAUDE.md              # Этот файл - инструкции для Claude
├── notebooks/
│   ├── 01_basics/         # Pandas, визуализация
│   ├── 02_machine_learning/  # scikit-learn, классическое ML
│   ├── 03_neural_networks/   # TensorFlow, CNN, RNN, GAN, VAE
│   └── 04_llm_api/           # Claude API, OpenAI API
├── data/                  # Датасеты и CSV файлы
└── docs/                  # Документация и роадмап
    └── AI_Learning_Roadmap.md
```

## Текущий прогресс

### Освоено:
- [x] Python окружение (3.12.7)
- [x] Pandas - работа с DataFrame
- [x] Matplotlib/Seaborn - визуализация
- [x] scikit-learn - классификация (RandomForest, Iris)
- [x] TensorFlow/Keras - базовые нейросети
- [x] CNN - свёрточные сети (MNIST)
- [x] RNN/LSTM - рекуррентные сети (IMDB)
- [x] Transformer - механизм внимания
- [x] GAN - генеративные сети
- [x] Autoencoder - сжатие и шумоподавление
- [x] VAE - вариационный автоэнкодер

### Следующие темы:
- [ ] LangChain / LlamaIndex - работа с LLM
- [ ] RAG - retrieval augmented generation
- [ ] API интеграции (OpenAI, Anthropic, DeepSeek)
- [ ] Reinforcement Learning
- [ ] Fine-tuning моделей
- [ ] Деплой моделей (Streamlit, FastAPI)

## Полезные команды

```bash
# Запуск Jupyter в папке проекта
jupyter notebook "C:\Users\Ruslan\Desktop\AI learning"

# Установка пакетов
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow jupyter
```

## Заметки
(Твои заметки)

---
*Обновлено: 12.01.2026*
