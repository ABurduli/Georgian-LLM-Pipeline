import json

from georgian_llm_pipeline.config import (
    STATISTICS_FILE,
    QUALITY_REPORT_FILE
)


def save_statistics(
        documents,
        total_words,
        unique_words,
        vocab_size
):

    stats = {

        "documents":
            documents,

        "total_words":
            total_words,

        "unique_words":
            unique_words,

        "vocab_size":
            vocab_size
    }

    with open(
        STATISTICS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            stats,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] {STATISTICS_FILE}"
    )


def save_quality_report(
        original_documents,
        final_documents,
        total_words,
        unique_words
):

    duplicates_removed = (
        original_documents
        - final_documents
    )

    avg_document_length = 0

    if final_documents > 0:

        avg_document_length = (
            total_words
            / final_documents
        )

    report = {

        "documents_loaded":
            original_documents,

        "documents_after_dedup":
            final_documents,

        "duplicates_removed":
            duplicates_removed,

        "total_words":
            total_words,

        "unique_words":
            unique_words,

        "avg_document_length":
            round(
                avg_document_length,
                2
            )
    }

    with open(
        QUALITY_REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] {QUALITY_REPORT_FILE}"
    )