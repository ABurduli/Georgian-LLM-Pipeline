from hashlib import md5

from georgian_llm_pipeline.config import (
    CORPUS_FILE,
    VOCAB_FILE,
    SPECIAL_TOKENS
)

from georgian_llm_pipeline.processors.text_processing import (
    extract_words,
    normalize_text
)


def deduplicate_documents(
        data
):

    seen = set()

    result = []

    for row in data:

        text = normalize_text(row)

        signature = md5(
            text.encode(
                "utf-8"
            )
        ).hexdigest()

        if signature in seen:
            continue

        seen.add(signature)

        result.append(row)

    duplicates_removed = (
        len(data)
        - len(result)
    )

    print(
        f"[INFO] Removed {duplicates_removed} duplicates"
    )

    return result


def create_corpus(
        data
):

    with open(
        CORPUS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for row in data:

            text = normalize_text(
                row
            )

            words = extract_words(
                text
            )

            if not words:
                continue

            f.write(
                " ".join(words)
            )

            f.write("\n")

    print(
        f"[OK] {CORPUS_FILE}"
    )


def create_vocab_file(
        all_words
):

    from collections import Counter

    counter = Counter(
        all_words
    )

    with open(
        VOCAB_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for token in SPECIAL_TOKENS:

            f.write(
                token + "\n"
            )

        for word, _ in sorted(
            counter.items(),
            key=lambda x: (
                -x[1],
                x[0]
            )
        ):

            if len(word) < 2:
                continue

            f.write(
                word + "\n"
            )

    print(
        f"[OK] {VOCAB_FILE}"
    )