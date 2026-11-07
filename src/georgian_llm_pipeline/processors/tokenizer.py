import sentencepiece as spm


def train_tokenizer(
        input_file,
        model_prefix,
        vocab_size,
        model_type,
        character_coverage,
        user_defined_symbols
):

    spm.SentencePieceTrainer.train(

        input=str(input_file),

        model_prefix=model_prefix,

        vocab_size=vocab_size,

        model_type=model_type,

        character_coverage=character_coverage,

        train_extremely_large_corpus=True,

        pad_id=0,
        unk_id=1,
        bos_id=2,
        eos_id=3,

        pad_piece="<pad>",
        unk_piece="<unk>",
        bos_piece="<bos>",
        eos_piece="<eos>",

        user_defined_symbols=",".join(
            user_defined_symbols
        )
    )