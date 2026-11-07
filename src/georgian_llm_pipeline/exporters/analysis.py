import csv

from georgian_llm_pipeline.config import (
    WORDS_CSV,
    VOCAB_FREQ_FILE,
    LEMMA_VOCAB_FILE,
    ENTITIES_FILE
)


def create_words_csv(
        unique_words,
        linguistic_data,
        stem_fn
):

    with open(
        WORDS_CSV,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "word",
            "stem",
            "lemma",
            "upos",
            "features"
        ])

        for word in sorted(unique_words):

            info = linguistic_data.get(
                word,
                {}
            )

            writer.writerow([
                word,
                stem_fn(word),
                info.get("lemma", word),
                info.get("upos", ""),
                info.get("features", "")
            ])

    print(f"[OK] {WORDS_CSV}")


def create_vocab_frequency(
        all_words
):

    from collections import Counter

    counter = Counter(all_words)

    with open(
        VOCAB_FREQ_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for word, freq in sorted(
            counter.items(),
            key=lambda x: (
                -x[1],
                x[0]
            )
        ):

            if len(word) < 2:
                continue

            f.write(
                f"{word} {freq}\n"
            )

    print(f"[OK] {VOCAB_FREQ_FILE}")


def create_lemma_vocab(
        linguistic_data
):

    lemmas = set()

    for value in linguistic_data.values():

        lemma = value.get(
            "lemma"
        )

        if lemma and len(lemma) > 1:

            lemmas.add(
                lemma.lower()
            )

    with open(
        LEMMA_VOCAB_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for lemma in sorted(lemmas):

            f.write(
                lemma + "\n"
            )

    print(
        f"[OK] {LEMMA_VOCAB_FILE}"
    )


def create_entities_file(
        linguistic_data
):

    entities = set()

    for word, info in linguistic_data.items():

        upos = info.get(
            "upos",
            ""
        )

        if upos in (
            "PROPN",
        ):

            entities.add(word)

    with open(
        ENTITIES_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for entity in sorted(entities):

            f.write(
                entity + "\n"
            )

    print(
        f"[OK] {ENTITIES_FILE}"
    )