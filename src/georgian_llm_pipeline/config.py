from pathlib import Path

# =====================================================
# INPUT
# =====================================================

INPUT_JSON = "input/data.json"

# =====================================================
# OUTPUTS
# =====================================================

OUTPUT_ROOT = Path("outputs")

ANALYSIS_DIR = OUTPUT_ROOT / "analysis"
TOKENIZER_DIR = OUTPUT_ROOT / "tokenizer"
LOGS_DIR = OUTPUT_ROOT / "logs"

# =====================================================
# ANALYSIS FILES
# =====================================================

WORDS_CSV = ANALYSIS_DIR / "words.csv"

VOCAB_FREQ_FILE = ANALYSIS_DIR / "vocab_freq.txt"

LEMMA_VOCAB_FILE = ANALYSIS_DIR / "lemma_vocab.txt"

ENTITIES_FILE = ANALYSIS_DIR / "entities.txt"

# =====================================================
# TOKENIZER FILES
# =====================================================

CORPUS_FILE = TOKENIZER_DIR / "corpus.txt"

VOCAB_FILE = TOKENIZER_DIR / "vocab.txt"

TOKENIZER_PREFIX = str(
    TOKENIZER_DIR / "tokenizer"
)

# =====================================================
# LOG FILES
# =====================================================

STATISTICS_FILE = LOGS_DIR / "statistics.json"

QUALITY_REPORT_FILE = LOGS_DIR / "quality_report.json"

# =====================================================
# TOKENIZER SETTINGS
# =====================================================

VOCAB_SIZE = 1450 #50000

MODEL_TYPE = "unigram"

CHARACTER_COVERAGE = 1.0

SPECIAL_TOKENS = [
    "<pad>",
    "<unk>",
    "<bos>",
    "<eos>",
    "<mask>",
    "<cls>",
    "<sep>",
    "<system>",
    "<user>",
    "<assistant>"
]

USER_DEFINED_SYMBOLS = [
    "<system>",
    "<user>",
    "<assistant>"
]