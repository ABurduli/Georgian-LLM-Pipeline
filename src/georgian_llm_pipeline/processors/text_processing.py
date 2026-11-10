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
    suffixes2 = [
        "ა",
        "ად",
        "ადი",
        "ავა",
        "აია",
        "აკი",
        "ას",
        "გვარი",
        "დ",
        "ებ",
        "ება",
        "ები",
        "ებრივი",
        "ებური",
        "ედი",
        "ეთი",
        "ელი",
        "ეული",
        "ვე",
        "თ",
        "თა",
        "ი",
        "ია",
        "იანი",
        "იერი",
        "ით",
        "ითი",
        "ილება",
        "ილი",
        "ირება",
        "ის",
        "ისას",
        "ისებრი",
        "ისებრნი",
        "ისტი",
        "ლოგია",
        "მაგვარი",
        "მდის",
        "მე",
        "ნაირი",
        "ნაცვალი",
        "ნი",
        "ო",
        "ობა",
        "ოდე",
        "ოდენა",
        "ოვანი",
        "ოსი",
        "ს",
        "უა",
        "ულება",
        "ული",
        "ური",
        "უჭი",
        "ფერი",
        "ფილი",
        "ფილია",
        "ფობი",
        "ფობია",
        "ღაც",
        "შვილი",
        "ში",
        "ძე",
        "ხანა",
        "ხელ",
        "ხელა",
        "ჯერ"
    ]


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