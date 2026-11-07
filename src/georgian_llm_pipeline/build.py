# build.py

import json
from pathlib import Path
from collections import Counter

from georgian_llm_pipeline.config import *

from georgian_llm_pipeline.processors.text_processing import (
    extract_words,
    get_stem
)

from georgian_llm_pipeline.processors.linguistic import (
    initialize_stanza,
    build_linguistic_dictionary
)

from georgian_llm_pipeline.processors.tokenizer import (
    train_tokenizer
)

from georgian_llm_pipeline.exporters.analysis import (
    create_words_csv,
    create_vocab_frequency,
    create_lemma_vocab,
    create_entities_file
)

from georgian_llm_pipeline.exporters.corpus import (
    create_corpus,
    create_vocab_file,
    deduplicate_documents
)

from georgian_llm_pipeline.exporters.statistics import (
    save_statistics
)


def load_dataset():

    with open(
        INPUT_JSON,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def prepare_directories():

    ANALYSIS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    TOKENIZER_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    LOGS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def collect_words(data):

    all_words = []
    unique_words = set()

    for row in data:

        text = (
            row.get("title", "")
            + " "
            + row.get("summary", "")
            + " "
            + row.get("text", "")
        )

        words = extract_words(text)

        all_words.extend(words)

        unique_words.update(words)

    return (
        all_words,
        unique_words
    )


def main():

    print("\nLoading dataset...")

    prepare_directories()

    data = load_dataset()

    print(
        f"Loaded {len(data):,} documents"
    )

    print(
        "\nRemoving duplicates..."
    )

    data = deduplicate_documents(
        data
    )

    print(
        f"Remaining documents: {len(data):,}"
    )

    print(
        "\nCollecting words..."
    )

    all_words, unique_words = (
        collect_words(data)
    )

    print(
        f"Total words: {len(all_words):,}"
    )

    print(
        f"Unique words: {len(unique_words):,}"
    )

    print(
        "\nInitializing Stanza..."
    )

    nlp = initialize_stanza()

    print(
        "\nBuilding linguistic dictionary..."
    )

    linguistic_data = (
        build_linguistic_dictionary(
            unique_words,
            nlp,
            get_stem
        )
    )

    print(
        "\nGenerating analysis files..."
    )

    create_words_csv(
        unique_words,
        linguistic_data,
        get_stem
    )

    create_vocab_frequency(
        all_words
    )

    create_lemma_vocab(
        linguistic_data
    )

    create_entities_file(
        linguistic_data
    )

    print(
        "\nGenerating corpus..."
    )

    create_corpus(data)

    create_vocab_file(
        all_words
    )

    print(
        "\nTraining tokenizer..."
    )

    train_tokenizer(
        input_file=CORPUS_FILE,
        model_prefix=TOKENIZER_PREFIX,
        vocab_size=VOCAB_SIZE,
        model_type=MODEL_TYPE,
        character_coverage=CHARACTER_COVERAGE,
        user_defined_symbols=USER_DEFINED_SYMBOLS
    )

    print(
        "\nWriting statistics..."
    )

    save_statistics(
        documents=len(data),
        total_words=len(all_words),
        unique_words=len(unique_words),
        vocab_size=VOCAB_SIZE
    )

    print(
        "\n================================="
    )

    print(
        "BUILD COMPLETED"
    )

    print(
        "=================================\n"
    )

    print(
        f"Analysis:  {ANALYSIS_DIR}"
    )

    print(
        f"Tokenizer: {TOKENIZER_DIR}"
    )

    print(
        f"Logs:      {LOGS_DIR}"
    )


#if __name__ == "__main__":
#    main()