# KA LLM Pipeline

ქართული ტექსტური კორპუსების დამუშავებისა და Tokenizer-ის მოსამზადებელი Pipeline.

პროექტი შექმნილია შემდეგი მიზნებისთვის:

- ქართული Large Language Model (LLM)
- ქართული Tokenizer-ის შექმნა
- RAG (Retrieval-Augmented Generation)
- Embedding მოდელები
- სემანტიკური ძიება
- Fine-Tuning Dataset-ები
- ქართული NLP კვლევა
- კორპუსის ანალიზი

Pipeline იღებს JSON ფორმატის ტექსტურ მონაცემებს, ასრულებს ლინგვისტურ ანალიზს, ქმნის სხვადასხვა Vocabulary ფაილებს და ავტომატურად წვრთნის SentencePiece Tokenizer-ს.

---

# დატესტილია

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (პაკეტებისა და პროექტის მენეჯერი)
- SentencePiece
- Stanza (Universal Dependencies)
- Georgian Wikipedia Dataset (ქვეჯგუფი)

---

# მონაცემთა წყარო

## გამოყენებული Dataset

ეს პროექტი შემოწმდა და განვითარდა Hugging Face-ზე განთავსებული ქართული ვიკიპედიის Dataset-ის მცირე ნაწილის გამოყენებით.

Dataset:

**MrDimitri / georgian-wikipedia**

სრული Dataset-ის გვერდი:

[MrDimitri/georgian-wikipedia](https://huggingface.co/datasets/MrDimitri/georgian-wikipedia)

Dataset შეიცავს ქართულ ვიკიპედიაზე დაფუძნებულ სტატიებს და შეიძლება გამოყენებულ იქნას:

- ქართული LLM-ის ტრენინგისთვის
- Tokenizer-ის შესაქმნელად
- Embedding მოდელებისთვის
- RAG სისტემებისთვის
- Semantic Search სისტემებისთვის
- ქართული NLP კვლევებისთვის

---

## გამოყენებული სატესტო მონაცემები

პროექტის განვითარების და ტესტირების პროცესში გამოყენებული იყო Dataset-ის მხოლოდ მცირე ნაწილი.

გამოყენებული მოცულობა:

```text
~28,000 სტატია
```

სრული Dataset-ის მხოლოდ ეს ნაწილი იყო კონვერტირებული JSON ფორმატში და გამოყენებული Pipeline-ის გამართვისა და ვალიდაციისთვის.

Pipeline არ არის შეზღუდული ამ მოცულობით და შექმნილია იმისთვის, რომ იმუშაოს:

- სრულ Georgian Wikipedia Dataset-ზე
- უფრო დიდ ქართულ კორპუსებზე
- სხვადასხვა წყაროდან შეგროვებულ ტექსტებზე

---

## მოსალოდნელი მონაცემების ფორმატი

Pipeline ელოდება მონაცემებს შემდეგ JSON ფორმატში:

```json
[
  {
    "title": "...",
    "summary": "...",
    "text": "..."
  }
]
```

---

## მნიშვნელოვანი შენიშვნა

ამ რეპოზიტორიაში Dataset არ შედის.

მოდელების გაწვრთნის, მონაცემების გავრცელებისა და გამოყენებისას დარწმუნდით, რომ იცავთ:

- ორიგინალური Dataset-ის ლიცენზიას
- Wikipedia-ს ლიცენზირების პირობებს
- Hugging Face Dataset-ის გამოყენების წესებს

დამატებითი ინფორმაცია:

[MrDimitri/georgian-wikipedia](https://huggingface.co/datasets/MrDimitri/georgian-wikipedia)

---

# შესაძლებლობები

Pipeline ავტომატურად ასრულებს:

✅ JSON Dataset-ის წაკითხვას

✅ დუბლიკატების მოცილებას

✅ title + summary + text გაერთიანებას

✅ ქართული სიტყვების ამოღებას

✅ Stem გენერაციას

✅ Lemma გენერაციას (Stanza)

✅ POS Tagging

✅ მორფოლოგიური ინფორმაციის მიღებას

✅ Vocabulary გენერაციას

✅ Frequency Analysis

✅ Lemma Vocabulary გენერაციას

✅ Entity Extraction

✅ SentencePiece Tokenizer-ის გაწვრთნას

✅ Corpus Statistics გენერაციას

✅ Quality Report გენერაციას

✅ თანამედროვე LLM Token-ების დამატებას

---

# პროექტის სტრუქტურა

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

# ინსტალაცია

## წინაპირობები

პროექტი მართულია [uv](https://docs.astral.sh/uv/)-ით. დააყენეთ, თუ არ გაქვთ:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## პროექტის კლონირება

```bash
git clone <repository-url>
cd Georgian-LLM-Pipeline
```

---

## საჭირო ბიბლიოთეკების დაყენება

uv ავტომატურად ქმნის ვირტუალურ გარემოს და აყენებს ყველა დამოკიდებულებას `pyproject.toml` / `uv.lock` ფაილებიდან:

```bash
uv sync
```

---

## ქართული Stanza მოდელის ჩამოტვირთვა

ერთხელ გაუშვით:

```bash
uv run python src/georgian_llm_pipeline/init_stanza.py
```

ან:

```bash
uv run python -c "import stanza; stanza.download('ka')"
```

თუ Stanza არ არის ხელმისაწვდომი ან ქართული მოდელი არ ჩაიტვირთა, Pipeline ავტომატურად გადავა Fallback რეჟიმში და გამოიყენებს მხოლოდ Stemmer-ს.

---

# გამოყენება

## 1. Dataset-ის მომზადება

შექმენით:

```text
input/
└── data.json
```

მაგალითი:

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

## 2. Pipeline-ის გაშვება

```bash
uv run georgian-llm-pipeline
```

ეს უშვებს `georgian-llm-pipeline` ბრძანებას, რომელიც განსაზღვრულია `pyproject.toml`-ში.

---

## გაშვების მაგალითი

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

# სატესტო კონფიგურაცია

პროექტის განვითარების და ტესტირების პროცესში გამოყენებული იყო:

```python
VOCAB_SIZE = 1450
```

ეს მნიშვნელობა გამოყენებული იყო მხოლოდ:

- Pipeline-ის ვალიდაციისთვის
- Tokenizer-ის სწრაფი გენერაციისთვის
- Debugging-ისთვის
- ტესტირების პროცესის დასაჩქარებლად

რეალურ ქართული NLP ან LLM პროექტებისთვის ეს მნიშვნელობა საკმარისი არ არის.

---

# რეკომენდებული კონფიგურაცია

რეალური ქართული კორპუსებისთვის რეკომენდებულია:

```python
VOCAB_SIZE = 50000
```

განსაკუთრებით მაშინ, როდესაც:

- გამოიყენება სრული Georgian Wikipedia Dataset
- ხდება ქართული LLM-ის Pretraining
- ხდება RAG სისტემის აგება
- იქმნება Embedding მოდელები
- მუშავდება დიდი ტექსტური კორპუსები

---

# რეკომენდებული Vocabulary ზომები

| კორპუსის ზომა | Vocabulary |
|-------------|------------|
| 10K – 100K დოკუმენტი | 32K |
| 100K – 1M დოკუმენტი | 50K |
| 1M+ დოკუმენტი | 64K |
| 10M+ დოკუმენტი | 80K |

Georgian Wikipedia Dataset-ისთვის რეკომენდებულია:

```python
VOCAB_SIZE = 50000
```

---

# გენერირებული ფაილები

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

# Analysis ფაილები

## words.csv

```csv
word,stem,lemma,upos,features
თბილისში,თბილის,თბილისი,PROPN,Case=Ine
კაცებმა,კაც,კაცი,NOUN,Case=Erg|Number=Plur
წავიდა,წავ,წასვლა,VERB,Tense=Past
```

---

## lemma_vocab.txt

```text
თბილისი
საქართველო
კაცი
ადამიანი
წიგნი
ქართველი
```

---

## vocab_freq.txt

```text
საქართველო 15234
თბილისი 13445
ადამიანი 9234
```

---

## entities.txt

```text
თბილისი
ბათუმი
ქუთაისი
საქართველო

Microsoft
OpenAI
```

---

# Tokenizer ფაილები

## corpus.txt

იქმნება:

```text
title
summary
text
```

ველების გაერთიანებით.

მაგალითი:

```text
თბილისი საქართველოს დედაქალაქია
ქართული ენა უძველესი ენაა
საქართველო მდებარეობს კავკასიაში
```

---

## vocab.txt

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

SentencePiece Tokenizer Model.

---

## tokenizer.vocab

SentencePiece Vocabulary.

---

# Statistics ფაილები

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

# Tokenizer-ის პარამეტრები

`config.py`

```python
VOCAB_SIZE = 50000

MODEL_TYPE = "unigram"

CHARACTER_COVERAGE = 1.0
```

---

# სპეციალური Token-ები

ავტომატურად ემატება:

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

თავსებადია:

- Llama
- Mistral
- Gemma
- Qwen
- GPT სტილის მოდელები

---

# Tokenizer-ის გამოყენება

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

შესაძლო შედეგი:

```python
[
  "▁თბილისი",
  "▁საქართველოს",
  "▁დედაქალაქია"
]
```

---

# სამუშაო სქემა

```text
JSON Dataset
      │
      ▼
დუბლიკატების მოცილება
      │
      ▼
ტექსტის ამოღება
      │
      ▼
სიტყვების შეგროვება
      │
      ▼
Stanza ანალიზი
      │
      ├── Lemma
      ├── POS
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
LLM Training / Fine-Tuning
```

---

# გამოყენების სფეროები

- ქართული LLM-ის ტრენინგი
- ქართული Tokenizer-ის შექმნა
- Corpus Analysis
- RAG სისტემები
- Semantic Search
- Question Answering
- Embedding მოდელები
- Knowledge Graph
- ქართული NLP კვლევა

---

# მომავალი განვითარება

შესაძლებელია დაემატოს:

- Named Entity Recognition (NER)
- Wikipedia Dump Parser
- PDF Import
- EPUB Import
- Web Crawling
- FastText Embeddings
- FAISS Index
- RAG Dataset Generator
- Instruction Dataset Generator
- GGUF Export
- Llama Fine-Tuning Export
- Qwen Fine-Tuning Export

---

# ლიცენზია

გამოიყენეთ თქვენი პასუხისმგებლობით.

მოდელების გაწვრთნისა და გავრცელებისას დაიცავით:

- Wikipedia-ს ლიცენზიის პირობები
- Hugging Face Dataset-ის ლიცენზია
- ორიგინალური მონაცემთა წყაროს პირობები
- თქვენი ქვეყნის შესაბამისი საავტორო უფლებების რეგულაციები