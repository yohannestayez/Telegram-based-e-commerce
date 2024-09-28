from amseg.amharicSegmenter import AmharicSegmenter


# Initialize the Amharic segmenter
sent_punct = []
word_punct = []
segmenter = AmharicSegmenter(sent_punct, word_punct)

# Function to check if the word contains Amharic characters
def contains_amharic(word):
    # Check if any character in the word is within the Amharic Unicode block (U+1200 to U+137F)
    return any(0x1200 <= ord(char) <= 0x137F for char in word)

# Function to segment Amharic text (with type checking)
def segment_amharic_text(segmenter, tokens):
    segmented_tokens = []
    for word in tokens:
        if isinstance(word, str):  # Ensure the token is a string
            if contains_amharic(word):
                tokenized_word = segmenter.amharic_tokenizer(word)
            else:
                tokenized_word = word  # Leave non-Amharic words as is
            segmented_tokens.append(tokenized_word)
    return segmented_tokens

# Example tokens (replace with your actual tokens)
tokens = ["ሰላም", "Hello", "አማርኛ", "123"]

# Segment Amharic tokens
segmented_tokens = segment_amharic_text(segmenter, tokens)

# Display the first 20 segmented results
print("Segmented Amharic Tokens:", segmented_tokens[:20])
