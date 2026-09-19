# DataAgent

> An intelligent dataset discovery and evaluation engine for finding, collecting, scoring, and cataloguing datasets from multiple sources.

DataAgent is a modular dataset discovery system being developed as part of the **BharatFact AI** project.

The goal is to automate the process of discovering relevant datasets for multilingual misinformation and fake-news detection, particularly datasets involving **English, Hindi, Hinglish, and Indian-context content**.

---

## Overview

Finding suitable datasets for an NLP/AI project is often a time-consuming process.

DataAgent automates this workflow by:

1. Searching multiple dataset sources
2. Collecting dataset metadata
3. Removing duplicate datasets
4. Evaluating dataset relevance
5. Assigning a priority score
6. Preparing datasets for further processing
7. Generating structured reports

The architecture is designed to support multiple data sources and can be extended as new collectors and processing modules are added.

---
```text
## Architecture


DataAgent follows a modular pipeline architecture:

                    ┌─────────────────────┐
                    │     Data Sources     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Collectors      │
                    │                     │
                    │   Hugging Face      │
                    │   (Currently)       │
                    │                     │
                    │   Kaggle            │
                    │   GitHub            │
                    │   AI4Bharat         │
                    │   (Planned)         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Metadata Extraction │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Dataset Scoring   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Priority Engine   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Deduplication     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Processed Dataset   │
                    └──────────┬──────────┘
                               │
                               ▼
                       Dataset Catalogue
```
---

## Current Implementation

The current version includes:

- Hugging Face dataset collection
- Dataset metadata extraction
- Dataset relevance scoring
- Dataset prioritization
- Dataset deduplication
- Configurable search keywords
- Configurable pipeline settings
- Structured dataset storage

Additional collectors and reporting modules are planned for future development.

---

## Project Structure

```text
DataAgent/
│
├── analyzer/
│   ├── metadata_extractor.py
│   ├── priority_engine.py
│   └── dataset_scorer.py
│
├── collector/
│   └── huggingface_collector.py
│
├── config/
│   ├── search_keywords.py
│   └── settings.py
│
├── processor/
│   └── deduplicator.py
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── logs/
├── cache/
│
├── collect.py
├── requirements.txt
├── README.md
└── .gitignore