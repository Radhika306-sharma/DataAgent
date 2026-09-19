# DataAgent

> An intelligent dataset discovery and evaluation engine for finding, collecting, scoring, and cataloguing datasets for multilingual misinformation and fake-news detection.

DataAgent is a modular dataset discovery system being developed as a component of **BharatFact AI**. It is designed to automate the process of discovering relevant datasets from multiple sources and evaluating their usefulness for multilingual misinformation detection.

The primary focus is on datasets containing:

- English content
- Hindi content
- Hinglish content
- Indian-context information
- Fake/real or misinformation-related labels

The system is designed to reduce the manual effort involved in searching for, evaluating, and organizing datasets before model training.

---

## Overview

Finding suitable datasets for multilingual misinformation detection can be difficult because datasets are distributed across different platforms and often have inconsistent metadata, formats, languages, and labeling schemes.

DataAgent addresses this problem through a modular pipeline that:

1. Searches for relevant datasets
2. Collects dataset metadata
3. Extracts important dataset characteristics
4. Evaluates dataset relevance
5. Assigns relevance and priority scores
6. Identifies duplicate datasets
7. Organizes datasets into structured storage
8. Prepares a dataset catalogue for downstream processing and model development

The system is designed to support multiple dataset sources through independent collectors.

---

## Role in BharatFact AI

DataAgent is the **dataset discovery and preparation layer** of the BharatFact AI system.

```text
                    BharatFact AI
                          │
                          ▼
                 ┌──────────────────┐
                 │    DataAgent     │
                 │                  │
                 │ Dataset Discovery│
                 │ & Preparation    │
                 └────────┬─────────┘
                          │
                          ▼
                Multilingual Datasets
                          │
                          ▼
                  Data Preprocessing
                          │
                          ▼
                Model Training/Fine-tuning
                          │
                          ▼
                Misinformation Detection
                          │
                          ▼
                    Evaluation
                          │
                          ▼
                  BharatFact AI App
```

DataAgent focuses specifically on the **data discovery and dataset preparation stage**, while model training and misinformation detection are handled by the downstream BharatFact AI components.

---

# Architecture

DataAgent follows a modular pipeline architecture.

```text
                    ┌─────────────────────┐
                    │     Data Sources    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Collectors      │
                    │                     │
                    │   Hugging Face      │
                    │   (Implemented)     │
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
                    ┌─────────────────────┐
                    │  Dataset Catalogue  │
                    └─────────────────────┘
```

Each stage is designed as an independent module so that additional data sources and processing components can be added without changing the complete pipeline.

---

# Current Implementation

The current version of DataAgent includes:

- Hugging Face dataset collection
- Dataset metadata extraction
- Dataset relevance scoring
- Dataset prioritization
- Dataset deduplication
- Configurable search keywords
- Configurable pipeline settings
- Structured dataset storage

### Currently Implemented Collector

| Source | Status |
|---|---|
| Hugging Face | Implemented |
| Kaggle | Planned |
| GitHub | Planned |
| AI4Bharat | Planned |

Additional collectors will be implemented incrementally.

---

# Dataset Discovery Pipeline

The main workflow is:

```text
Search Keywords
      │
      ▼
Dataset Collection
      │
      ▼
Metadata Extraction
      │
      ▼
Relevance Scoring
      │
      ▼
Priority Assignment
      │
      ▼
Duplicate Detection
      │
      ▼
Dataset Organisation
      │
      ▼
Dataset Catalogue
```

---

## 1. Dataset Collection

Collectors search supported dataset platforms using predefined keywords.

Example search areas include:

```text
fake news
misinformation
fake news detection
Hindi fake news
Hinglish misinformation
Indian misinformation
Indian fake news
news classification
fact checking
```

Search keywords are maintained separately in:

```text
config/search_keywords.py
```

This allows the search strategy to be modified without changing the collector implementation.

---

## 2. Metadata Extraction

After datasets are discovered, DataAgent extracts relevant metadata.

Examples include:

- Dataset name
- Dataset description
- Dataset URL
- Dataset source
- Dataset size
- Available splits
- Languages
- Labels
- Dataset format
- Relevant keywords
- Dataset tags

Metadata extraction is handled by:

```text
analyzer/metadata_extractor.py
```

---

## 3. Dataset Scoring

Each discovered dataset is evaluated according to its relevance to the project.

Potential relevance factors include:

- Indian context
- Hindi content
- English content
- Hinglish content
- Fake/real labels
- Misinformation labels
- News-related content
- Dataset size
- Availability of useful metadata

The scoring logic is implemented in:

```text
analyzer/dataset_scorer.py
```

The objective is to prioritize datasets that are more useful for multilingual misinformation detection.

---

## 4. Priority Assignment

After scoring, datasets can be prioritized based on their relevance.

The priority engine is implemented in:

```text
analyzer/priority_engine.py
```

This allows downstream processing to focus on the most relevant datasets first.

---

## 5. Deduplication

Datasets collected from different sources may refer to the same or highly similar datasets.

The deduplication module helps identify duplicate entries and prevents unnecessary repetition in the dataset catalogue.

Implementation:

```text
processor/deduplicator.py
```

---

# Project Structure

```text
DataAgent/
│
├── analyzer/
│   ├── dataset_scorer.py
│   ├── metadata_extractor.py
│   └── priority_engine.py
│
├── collector/
│   └── huggingface_collector.py
│
├── config/
│   ├── search_keywords.py
│   └── settings.py
│
├── datasets/
│   ├── raw/
│   │   └── .gitkeep
│   │
│   ├── processed/
│   │   └── .gitkeep
│   │
│   └── final/
│       └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
├── processor/
│   └── deduplicator.py
│
├── cache/
│
├── collect.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Directory Responsibilities

### `collector/`

Contains modules responsible for collecting dataset information from external sources.

Current implementation:

```text
huggingface_collector.py
```

Future collectors can be added independently.

---

### `analyzer/`

Contains modules responsible for understanding and evaluating discovered datasets.

```text
dataset_scorer.py
metadata_extractor.py
priority_engine.py
```

---

### `processor/`

Contains modules that process and organize discovered datasets.

Current implementation:

```text
deduplicator.py
```

---

### `config/`

Contains configurable project settings.

```text
search_keywords.py
settings.py
```

Keeping configuration separate makes the pipeline easier to modify and maintain.

---

### `datasets/`

Stores datasets at different stages of the pipeline.

```text
raw/
```

Stores newly collected or unprocessed dataset information.

```text
processed/
```

Stores datasets after preprocessing and analysis.

```text
final/
```

Stores datasets that are ready for downstream use.

---

### `logs/`

Stores execution logs generated during pipeline execution.

---

### `cache/`

Used for temporary or cached information generated during dataset discovery.

---

# Configuration

Important configuration values are centralized in:

```text
config/settings.py
```

Search terms are maintained in:

```text
config/search_keywords.py
```

This allows the dataset discovery strategy to be modified without modifying the core pipeline logic.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Radhika306-sharma/DataAgent.git
```

Move into the project directory:

```bash
cd DataAgent
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment on macOS/Linux:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

The main entry point for dataset collection is:

```text
collect.py
```

Run the collector using:

```bash
python collect.py
```

The pipeline will use the configured search keywords and collector modules to discover relevant datasets.

---

# Example Workflow

A typical DataAgent execution follows:

```text
1. Load configuration
        ↓
2. Load search keywords
        ↓
3. Search supported dataset source
        ↓
4. Collect dataset metadata
        ↓
5. Extract relevant attributes
        ↓
6. Calculate relevance score
        ↓
7. Assign priority
        ↓
8. Detect duplicates
        ↓
9. Store structured dataset information
```

---

# Multilingual Dataset Focus

DataAgent is primarily designed for datasets relevant to multilingual misinformation detection.

The target language categories include:

### English

Standard English-language misinformation and fake-news datasets.

### Hindi

Datasets containing Hindi text written in Devanagari script.

### Hinglish

Datasets containing Hindi-English code-mixed text, including Romanized Hindi.

### Indian Context

Datasets related to Indian:

- News
- Social media
- Politics
- Public events
- Fact-checking
- Misinformation
- Online claims

The multilingual focus is important for BharatFact AI because misinformation in India frequently occurs across multiple languages and code-mixed communication.

---

# Dataset Evaluation Criteria

DataAgent can evaluate datasets using criteria such as:

| Criterion | Description |
|---|---|
| Indian Context | Relevance to India |
| Language | English, Hindi, Hinglish, or multilingual |
| Fake/Real Labels | Availability of misinformation-related labels |
| Misinformation Relevance | Relevance to misinformation/fake-news detection |
| Dataset Size | Number of available samples |
| Data Quality | Completeness and usefulness of metadata |
| Source | Reliability and accessibility of the dataset source |
| Diversity | Variety of topics and sources |

These criteria can be extended as the project evolves.

---

# Design Principles

DataAgent follows several design principles.

### Modularity

Each dataset source is handled by an independent collector.

### Extensibility

New dataset sources can be added without redesigning the entire pipeline.

### Configurability

Search keywords and project settings are maintained separately from the processing logic.

### Reusability

DataAgent is designed as an independent component that can be reused by BharatFact AI and potentially other NLP/ML projects.

### Automation

The goal is to minimize manual dataset discovery and evaluation.

### Multilingual Support

The architecture is designed around multilingual and Indian-language dataset discovery.

---

# Future Development

Planned improvements include:

### Additional Dataset Collectors

- Kaggle
- GitHub
- AI4Bharat
- Papers With Code
- Zenodo

### Improved Dataset Analysis

- Automatic language detection
- Hindi/Hinglish identification
- Label analysis
- Class distribution analysis
- Dataset quality analysis
- Dataset size estimation
- Duplicate dataset detection across sources

### Advanced Scoring

Future versions may incorporate more sophisticated scoring based on:

```text
Language Relevance
        +
Indian Context
        +
Label Availability
        +
Dataset Size
        +
Misinformation Relevance
        +
Data Quality
        =
Overall Dataset Relevance
```

### Dataset Preparation

Future processing modules may include:

- Text cleaning
- Language normalization
- Label normalization
- Class balancing
- Train/validation/test splitting
- Cross-dataset merging
- Dataset format standardization

### Reporting

Structured reports may be added in future versions to provide:

- Dataset summaries
- Dataset comparison
- Scoring information
- Dataset statistics
- Collection history

---

# Planned BharatFact AI Integration

The long-term integration is:

```text
                ┌─────────────────────┐
                │     Data Sources    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      DataAgent      │
                │                     │
                │ Collection          │
                │ Metadata            │
                │ Scoring             │
                │ Deduplication       │
                │ Preparation         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Multilingual Data   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Model Training      │
                │                     │
                │ IndicBERT / MuRIL   │
                │ Gemma / Other LLMs  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Misinformation      │
                │ Detection Model     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    BharatFact AI    │
                └─────────────────────┘
```

DataAgent therefore acts as the **data intelligence layer** that prepares the foundation for the downstream multilingual misinformation detection system.

---

# Development Status

| Component | Status |
|---|---|
| Project structure | Implemented |
| Configuration system | Implemented |
| Search keywords | Implemented |
| Hugging Face collector | Implemented |
| Metadata extraction | Implemented |
| Dataset scoring | Implemented |
| Priority engine | Implemented |
| Deduplication | Implemented |
| Dataset storage | Implemented |
| Kaggle collector | Planned |
| GitHub collector | Planned |
| AI4Bharat collector | Planned |
| Advanced language detection | Planned |
| Dataset normalization | Planned |
| Automated reporting | Planned |
| BharatFact AI integration | Planned |

---

# Repository

GitHub:

**https://github.com/Radhika306-sharma/DataAgent**

---

# Project Context

DataAgent is being developed as part of:

**BharatFact AI**

A multilingual misinformation detection project focused on Indian digital content and languages.

The overall objective is to build a reliable pipeline for discovering, preparing, and utilizing multilingual datasets for misinformation detection.

---

# License

This project is currently under development.

License information will be added in a future release.