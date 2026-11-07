import sentencepiece as spm

print("Loading SentencePiece model...")
sp = spm.SentencePieceProcessor()
sp.load("outputs/tokenizer/tokenizer.model")

print(sp.get_piece_size())
print(
    sp.encode(
        "თბილისი საქართველოს დედაქალაქია",
        out_type=str
    )
)


print("Loading LLaMA tokenizer...")
from transformers import LlamaTokenizer

tokenizer = LlamaTokenizer(
    vocab_file="outputs/tokenizer/tokenizer.model"
)
print(tokenizer.vocab_size)