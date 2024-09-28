# Tokenization Notebook

## Overview
This notebook demonstrates the tokenization of a multi-lingual dataset using Python, along with libraries such as amseg.amharicSegmenter. The notebook tokenizes the dataset and prepares it for further processing by writing the tokens to a temporary file.

## Main Components

### 1. Data Preprocessing
The raw text data is cleaned and preprocessed. It contains a mix of languages (English and Amharic), but mostly amharic and the data is prepared for tokenization.

### 2. Tokenization
Tokens are generated using AmharicSegmenter method, which segments the text into smaller units (tokens). The tokens are displayed for verification and analysis.

### 3. okenizer
The tokens are stored in a file `temp_text.txt`, which will be used for further analysis.

## How to Use

1. **Data Preparation**: Ensure you have the appropriate text data loaded for tokenization.
2. **Run the Notebook**: Execute the cells step by step to preprocess the data, tokenize it, and generate tokens.
3. **Token Output**: The tokenized data is stored in `temp_text.txt`, which can be used for further processing or model training.

## Dependencies
- Python 3.x
- pandas
- amseg