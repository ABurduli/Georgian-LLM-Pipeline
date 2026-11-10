# KA LLM Pipeline

🇬🇪 For Georgian Documentation see: [readme_ka.md](readme_ka.md)

A complete Georgian NLP and tokenizer preparation pipeline designed for:

- Georgian Large Language Models (LLMs)
- SentencePiece tokenizer training
- Retrieval-Augmented Generation (RAG)
- Embedding models
- Semantic search
- Fine-tuning datasets
- Corpus analysis
- Georgian NLP research

The pipeline processes a JSON corpus, performs linguistic analysis, generates vocabularies, creates a tokenizer training corpus, and trains a SentencePiece tokenizer.

---

# Tested With

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package and project manager)
- SentencePiece
- Stanza (Universal Dependencies)
- Georgian Wikipedia Dataset (subset)

## Dataset Source

Dataset:

**MrDimitri / georgian-wikipedia**

Source:

[Georgian Wikipedia Dataset on Hugging Face](https://huggingface.co/datasets/MrDimitri/georgian-wikipedia)

The complete dataset contains the full Georgian Wikipedia corpus and can be used for large-scale tokenizer training, language model pretraining, embedding generation, semantic search, and other Georgian NLP tasks.

### Development Dataset

Development and testing were performed using only a small subset of the Georgian Wikipedia dataset.

Approximate size used during testing:

```text
~28,000 articles
```

The pipeline itself is designed to process the complete dataset as well as significantly larger Georgian corpora.

The dataset is not included in this repository.

Please refer to the original dataset license and usage terms.

---

# Features

The pipeline automatically performs:

✅ JSON dataset loading

✅ Document deduplication

✅ Title + Summary + Text merging

✅ Georgian word extraction

✅ Heuristic stemming

✅ Stanza lemmatization (when available)

✅ POS tagging

✅ Morphological analysis

✅ Vocabulary generation

✅ Frequency analysis

✅ Lemma vocabulary generation

✅ Entity extraction

✅ SentencePiece tokenizer training

✅ Corpus statistics generation

✅ Quality reports

✅ Modern LLM special token generation

---

# Project Structure

```text
Georgian-LLM-Pipeline/

├── pyproject.toml
├── uv.lock
│
├── input/
│   └── data.json
│
├── src/
│   └── georgian_llm_pipeline/
│       ├── __init__.py
│       ├── build.py
│       ├── config.py
│       ├── init_stanza.py
│       │
│       ├── processors/
│       │   ├── text_processing.py
│       │   ├── linguistic.py
│       │   └── tokenizer.py
│       │
│       └── exporters/
│           ├── analysis.py
│           ├── corpus.py
│           └── statistics.py
│
└── outputs/
    ├── analysis/
    ├── tokenizer/
    └── logs/
```

---

# Expected JSON Format

```json
[
  {
    "title": "თბილისი",
    "summary": "საქართველოს დედაქალაქი",
    "text": "თბილისი არის საქართველოს დედაქალაქი..."
  }
]
```

---

# Installation

## Prerequisites

This project is managed with [uv](https://docs.astral.sh/uv/). Install it if you don't have it:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Clone Repository

```bash
git clone <repository-url>
cd Georgian-LLM-Pipeline
```

## Install Dependencies

uv automatically creates a virtual environment and installs all dependencies from `pyproject.toml` / `uv.lock`:

```bash
uv sync
```

## Download Georgian Stanza Model

```bash
uv run python src/georgian_llm_pipeline/init_stanza.py
```

or

```bash
uv run python -c "import stanza; stanza.download('ka')"
```

If Stanza cannot be loaded, the pipeline automatically switches to heuristic stemming mode.

---

# Usage

## Step 1. Prepare Dataset

Create:

```text
input/
└── data.json
```

Example:

```json
[
  {
    "title": "თბილისი",
    "summary": "საქართველოს დედაქალაქი",
    "text": "თბილისი არის საქართველოს დედაქალაქი..."
  }
]
```

---

## Step 2. Run Pipeline

```bash
uv run georgian-llm-pipeline
```

This runs the `georgian-llm-pipeline` console script defined in `pyproject.toml`.

---

## Example Console Output

```text
Loading dataset...

Loaded 28,065 documents

Removing duplicates...

Remaining documents: 27,541

Collecting words...

Total words: 7,421,983

Unique words: 387,614

Initializing Stanza...

Building linguistic dictionary...

Generating analysis files...

Generating corpus...

Training tokenizer...

Writing statistics...

BUILD COMPLETED
```

---

# Testing Configuration

For development and testing purposes, the tokenizer vocabulary size was intentionally reduced:

```python
VOCAB_SIZE = 1450
```

This value was used only for testing, validation, and rapid tokenizer generation.

It is **not recommended** for production tokenizer training or Georgian LLM development.

---

# Recommended Production Configuration

For real-world Georgian corpora:

```python
VOCAB_SIZE = 50000
```

Recommended for:

- Georgian LLM training
- Using the full Georgian Wikipedia dataset
- Embedding models
- RAG systems
- Semantic search
- Large-scale Georgian corpora

---

# Recommended Vocabulary Sizes

| Corpus Size | Vocabulary Size |
|------------|----------------|
| 10K–100K documents | 32K |
| 100K–1M documents | 50K |
| 1M+ documents | 64K |
| 10M+ documents | 80K |

For the Georgian Wikipedia dataset:

```python
VOCAB_SIZE = 50000
```

is recommended.

---

# Generated Files

After execution:

```text
outputs/

analysis/
├── words.csv
├── lemma_vocab.txt
├── vocab_freq.txt
└── entities.txt

tokenizer/
├── corpus.txt
├── vocab.txt
├── tokenizer.model
└── tokenizer.vocab

logs/
├── statistics.json
└── quality_report.json
```

---

# Analysis Files

## words.csv

Detailed linguistic analysis:

```csv
word,stem,lemma,upos,features
თბილისში,თბილის,თბილისი,PROPN,Case=Ine
კაცებმა,კაც,კაცი,NOUN,Case=Erg|Number=Plur
წავიდა,წავ,წასვლა,VERB,Tense=Past
```

---

## lemma_vocab.txt

Unique lemmas:

```text
თბილისი
საქართველო
კაცი
ადამიანი
წიგნი
```

Useful for:

- Search
- Embeddings
- Knowledge Graphs
- Entity Normalization

---

## vocab_freq.txt

Word frequency counts:

```text
საქართველო 15234
თბილისი 13445
ადამიანი 9234
```

---

## entities.txt

Proper nouns extracted from POS tagging:

```text
თბილისი
ბათუმი
ქუთაისი
საქართველო

Microsoft
OpenAI
```

---

# Tokenizer Files

## corpus.txt

Tokenizer training corpus generated from:

```text
title
summary
text
```

Example:

```text
თბილისი საქართველოს დედაქალაქია
ქართული ენა უძველესი ენაა
საქართველო მდებარეობს კავკასიაში
```

---

## vocab.txt

Vocabulary file:

```text
<pad>
<unk>
<bos>
<eos>
<mask>
<cls>
<sep>
<system>
<user>
<assistant>

საქართველო
თბილისი
ადამიანი
```

---

## tokenizer.model

SentencePiece tokenizer model.

---

## tokenizer.vocab

SentencePiece vocabulary.

---

# Statistics Files

## statistics.json

```json
{
  "documents": 28065,
  "total_words": 7421983,
  "unique_words": 387614,
  "vocab_size": 50000
}
```

---

## quality_report.json

```json
{
  "documents_loaded": 28065,
  "documents_after_dedup": 27541,
  "duplicates_removed": 524,
  "total_words": 7421983,
  "unique_words": 387614,
  "avg_document_length": 269.35
}
```

---

# Tokenizer Configuration

Default:

```python
VOCAB_SIZE = 50000

MODEL_TYPE = "unigram"

CHARACTER_COVERAGE = 1.0
```

---

# Special Tokens

Automatically added:

```text
<pad>
<unk>
<bos>
<eos>
<mask>
<cls>
<sep>
<system>
<user>
<assistant>
```

Suitable for:

- Llama
- Mistral
- Gemma
- Qwen
- GPT-style architectures

---

# Using the Generated Tokenizer

```python
import sentencepiece as spm

sp = spm.SentencePieceProcessor()

sp.load(
    "outputs/tokenizer/tokenizer.model"
)

tokens = sp.encode(
    "თბილისი საქართველოს დედაქალაქია",
    out_type=str
)

print(tokens)
```

Example output:

```python
[
  "▁თბილისი",
  "▁საქართველოს",
  "▁დედაქალაქია"
]
```

## Tokenization Efficiency for Non-English Languages


This project demonstrates how a custom SentencePiece tokenizer can be combined with the standard LLaMA tokenizer to improve tokenization efficiency for non-English languages such as Georgian.

```bash
uv run test.py
```

### Results

Test text:

> "თბილისი საქართველოს დედაქალაქია. Tbilisi is the capital of Georgia."

| Tokenizer | Token Count |
|------------|-------------|
| Standard LLaMA | 43 |
| Custom SentencePiece | 21 |
| Combined Tokenizer | 26 |

The custom tokenizer reduced the number of tokens to approximately **60%** of the standard LLaMA tokenizer, while the combined tokenizer achieved a similar reduction with only **26 tokens**.

### Why It Matters

Large Language Models process text as tokens. When a tokenizer is optimized for a specific language, it can represent words and phrases using fewer tokens. This provides several advantages:

- Lower inference and API costs
- Reduced memory consumption
- Faster processing
- More efficient use of the model context window
- Better support for low-resource and non-English languages

For Georgian and other non-English languages, a language-specific tokenizer can significantly reduce token fragmentation compared to English-centric tokenizers. As a result, the same text requires fewer tokens, making AI applications more efficient and cost-effective.

---

# Processing Pipeline

```text
JSON Dataset
      │
      ▼
Document Deduplication
      │
      ▼
Text Extraction
      │
      ▼
Word Collection
      │
      ▼
Stanza Analysis
      │
      ├── Lemmas
      ├── POS Tags
      └── Morphology
      │
      ▼
Vocabulary Generation
      │
      ▼
Corpus Creation
      │
      ▼
SentencePiece Training
      │
      ▼
tokenizer.model
      │
      ▼
LLM Pretraining / Fine-Tuning
```

---

# Intended Use Cases

- Georgian LLM training
- Georgian tokenizer development
- Corpus analysis
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Question answering systems
- Embedding model training
- Knowledge graph creation
- Georgian NLP research

---

# Future Improvements

Potential future additions:

- Georgian NER
- Wikipedia dump processing
- PDF ingestion
- EPUB ingestion
- Web crawling
- FastText embeddings
- FAISS index generation
- RAG dataset generation
- Instruction dataset generation
- GGUF-ready exports
- Llama fine-tuning exports
- Qwen fine-tuning exports

---

# License

Use at your own discretion.

Please respect the original dataset licenses (including Wikipedia-derived datasets) and verify redistribution rights before training or publishing derived models.