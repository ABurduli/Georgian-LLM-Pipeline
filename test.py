from shlex import split
from pathlib import Path

import sentencepiece as spm

sample_text = 'თბილისი საქართველოს დედაქალაქია. Tbilisi is the capital of Georgia.'

print("Loading SentencePiece model...")
sp = spm.SentencePieceProcessor()
sp.load("outputs/tokenizer/tokenizer.model")

print(sp.get_piece_size())
print(
    sp.encode(
        sample_text,
        out_type=str
    )
)

print("Loading LLaMA tokenizer...")
from transformers import LlamaTokenizer
# using standart LLaMA tokenizer from HuggingFace, but you can use your own tokenizer trained with SentencePiece
print("Loading standard LLaMA tokenizer...")
std_tokenizer = LlamaTokenizer.from_pretrained('huggyllama/llama-7b', legacy=False) #huggyllama/llama-7b
std_encoded_text = std_tokenizer.encode(sample_text)
print("Encoded text:", std_encoded_text)
# print tokens by id   
print("Tokens by ID:", [std_tokenizer.convert_ids_to_tokens(i) for i in std_encoded_text])

print("Loading custom LLaMA tokenizer...")

SCRIPT_DIR = Path(__file__).resolve().parent
VOCAB_PATH = SCRIPT_DIR / "outputs" / "tokenizer" 

tokenizer = LlamaTokenizer.from_pretrained(VOCAB_PATH,legacy=False)

print("Vocabulary size:", tokenizer.vocab_size)
encoded_text = tokenizer.encode(sample_text)
print("Encoded text:", encoded_text)
# print tokens by id   
print("Tokens by ID:", [tokenizer.convert_ids_to_tokens(i) for i in encoded_text])

print("Combine tokenizers...")
# Convert vocab keys to sets for fast membership testing
std_vocab_set = set(std_tokenizer.get_vocab().keys())
new_tokens = [tok for tok in tokenizer.get_vocab() if tok not in std_vocab_set]

if new_tokens:
    std_tokenizer.add_tokens(new_tokens)
    print(f"Added {len(new_tokens)} new tokens to tokenizer.")
else:
    print("No new tokens to add.")

# resize the model's embedding before training or inference !
mrg_encoded_text = std_tokenizer.encode(sample_text)
print("Encoded text:", mrg_encoded_text)
print("Tokens by ID:", [std_tokenizer.convert_ids_to_tokens(i) for i in mrg_encoded_text])

print("Summary of tokenizers testing:")

print("Standard tokenizer encoded tokens count:", len(std_encoded_text))
tokens_count = len(encoded_text)
std_tokens_count = len(std_encoded_text)
percentage = tokens_count / std_tokens_count * 100
print(f"Custom tokenizer produced {tokens_count} tokens ({percentage:.2f}% of the standard tokenizer's {std_tokens_count} tokens).")

combined_tokens_count = len(mrg_encoded_text)
combined_percentage = combined_tokens_count / std_tokens_count * 100
print(f"Combined tokenizer produced {combined_tokens_count} tokens ({combined_percentage:.2f}% of the standard tokenizer's {std_tokens_count} tokens).")

