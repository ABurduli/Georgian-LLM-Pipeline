import re

GEORGIAN_PATTERN = re.compile(
    r"[ა-ჰ]+"
)


def extract_words(text):

    if not text:
        return []

    return GEORGIAN_PATTERN.findall(
        text.lower()
    )


def get_stem(word):

    suffixes = [

        "ებისთვის",
        "ებისგან",
        "ებთან",
        "ებიდან",

        "ების",
        "ებმა",
        "ებში",

        "იდან",
        "ამდე",

        "ობით",
        "ურად",
        "ულად",

        "თან",
        "დან",

        "ებს",

        "ით",
        "ში",
        "ზე",

        "მა",
        "ის",
        "ას",
        "ად",
        "თა",

        "ს",
        "ი",
        "ა"
    ]

    for suffix in sorted(
        suffixes,
        key=len,
        reverse=True
    ):

        if (
            word.endswith(suffix)
            and len(word)
            > len(suffix) + 2
        ):

            return word[:-len(suffix)]

    return word


def normalize_text(record):

    title = record.get(
        "title",
        ""
    )

    summary = record.get(
        "summary",
        ""
    )

    text = record.get(
        "text",
        ""
    )

    return (
        title
        + "\n"
        + summary
        + "\n"
        + text
    )