try:

    import stanza

    STANZA_AVAILABLE = True

except Exception:

    STANZA_AVAILABLE = False


def initialize_stanza():

    if not STANZA_AVAILABLE:

        print(
            "[WARN] stanza not installed"
        )

        return None

    try:

        stanza.download(
            "ka",
            verbose=False
        )

        nlp = stanza.Pipeline(
            lang="ka",
            processors="tokenize,pos,lemma",
            verbose=False
        )

        print(
            "[OK] Stanza ready"
        )

        return nlp

    except Exception as e:

        print(
            f"[WARN] Stanza disabled: {e}"
        )

        return None


def build_linguistic_dictionary(
        unique_words,
        nlp,
        stem_fn
):

    result = {}

    total = len(unique_words)

    if nlp is None:

        for index, word in enumerate(
                unique_words, 1):

            result[word] = {
                "lemma": stem_fn(word),
                "upos": "",
                "features": ""
            }

            if index % 1000 == 0 \
                    or index == total:

                print(
                    f"\rProcessing words: "
                    f"{index:,}/{total:,} "
                    f"({index / total:.0%})",
                    end="",
                    flush=True
                )

        print()

        return result

    try:

        words = sorted(unique_words)

        batch_size = 2000

        for start in range(
                0, total, batch_size):

            batch = words[
                start:start + batch_size
            ]

            text = "\n".join(batch)

            doc = nlp(text)

            for sentence in doc.sentences:

                for token in sentence.words:

                    result[token.text] = {

                        "lemma":
                            token.lemma
                            or token.text,

                        "upos":
                            token.upos
                            or "",

                        "features":
                            token.feats
                            or ""
                    }

            done = min(
                start + batch_size, total
            )

            print(
                f"\rProcessing words: "
                f"{done:,}/{total:,} "
                f"({done / total:.0%})",
                end="",
                flush=True
            )

        print()

    except Exception as e:

        print(
            f"\n[WARN] stanza processing failed: {e}"
        )

    return result