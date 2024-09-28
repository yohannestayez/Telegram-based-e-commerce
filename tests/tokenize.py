# Initialize SentencePiece tokenizer
tokenizer_spm = spm.SentencePieceProcessor(model_file='AmharicSPM.model')

# Tokenize the input text with SentencePiece
sentencepiece_tokens = tokenizer_spm.encode("ቁ.2 ለቡ መዳህኒዓለም and here is some English text.", out_type=str)

# Print the tokenized words
print("SentencePiece Tokenization Results:")
print(sentencepiece_tokens)