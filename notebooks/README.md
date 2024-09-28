


# Telegram Data NER Labeling and Tokenization Project

This project involves extracting named entities such as locations, prices, and products from messages obtained from a Telegram channel and tokenizing the dataset for further analysis. The workflow utilizes a combination of pre-trained Named Entity Recognition (NER) models, custom rule-based labeling techniques, and tokenization for Amharic and multi-lingual text data.

## Project Structure

- **Dataset**: The dataset consists of Telegram messages saved in a CSV file named `telegram_data.csv`
- **Model**: We use the pre-trained Masakhane NER model `afroxlmr-large-ner-masakhaner-1.0_2.0` for identifying location, organization, and miscellaneous entities.
- **Pipeline**: A custom pipeline is built that integrates both NER model predictions and custom rule-based labeling for price and location extraction.

## Files

- **telegram_data.csv**: The input dataset containing Telegram messages.
- **labeled_data_conll.txt**: The output file containing labeled data in CoNLL format.
- **temp_text.txt**: The output file containing tokenized data for further analysis.
- **tokenization.ipynb**: Jupyter notebook demonstrating the preprocessing and tokenization of a multi-lingual dataset.
- **PreprocessingDataLabelStarter.ipynb**: Jupyter notebook for the preprocessing steps and initial data labeling setup for the dataset.

## How to Use

### 1. Install the Required Dependencies:

1. **Python 3.x**: Ensure you have a compatible version of Python installed.

2. **pandas**: For data manipulation and analysis.

3. **transformers**: For working with pre-trained models and pipelines from Hugging Face.
 
4. **emoji**: For handling emojis in the text data.

5. **amseg**: For tokenizing Amharic text.
  

### Installation Command
You can install all these dependencies at once by running the following command:
```
pip install pandas transformers emoji amseg
```

Make sure to run this command in your terminal or command prompt where your Python environment is set up.



### 2. Run the Tokenization Notebook:
   - The `tokenization.ipynb` is used to preprocess the raw dataset, clean the text, and tokenize Amharic and multi-lingual messages.
   - Tokens are saved to `temp_text.txt` for further processing.
   - Execute the notebook step by step to preprocess and generate tokenized data.

### 3. Run the Data Preprocessing and Labeling Notebook:
   - The `PreprocessingDataLabelStarter.ipynb` notebook will guide you through the preprocessing steps and set up initial labels for the dataset.
   - Follow the instructions in the notebook to process the data and prepare it for labeling.

### 4. Run the NER Labeling Script:
   - After preprocessing, run the `main.py` script (if applicable) to apply the NER model and custom labeling rules to the dataset.
   - The final labeled data will be saved in `labeled_data_conll.txt`.

## NER and Labeling Process

### 1. **NER Model**:
   - The script uses the `Masakhane` pre-trained model to extract location (LOC), organization (ORG), and miscellaneous (MISC) entities from messages.

### 2. **Custom Labeling**:
   - In addition to the NER model, a custom rule-based approach is used to identify prices (ETB, Birr, $, etc.) and additional location names (e.g., Addis Ababa, Mekelle, Bole, etc.).
   - Specific tokens such as `አድራሻ` (address), `Price`, `Discount`, etc., are labeled manually.

### 3. **Combining Labels**:
   - The final labels for each token are a combination of the NER model results and the custom labeling rules. The NER model's labels take precedence over custom labels, but custom labels are applied to fill in missing annotations.

### 4. **Output Format**:
   - The output is saved in a CoNLL-style format where each token in a message is labeled with the respective entity type.


## Tokenization Process

The **tokenization.ipynb** notebook demonstrates the following steps:

### 1. **Data Preprocessing**:
   - The raw text data is cleaned and prepared for tokenization. The dataset contains Amharic and English text.

### 2. **Tokenization**:
   - The Amharic text is segmented into smaller units (tokens) using the `amseg` library.
   - Tokens are displayed for verification and stored in `temp_text.txt` for further analysis.

### 3. **Token Output**:
   - Tokenized data is stored in a temporary file `temp_text.txt`, which can be used for further processing or training machine learning models.

## Customizable Elements

- **Location List**: You can modify the list of predefined locations in the `custom_label_prices_locations` function to fit your specific needs.
- **Price Patterns**: Update the `price_patterns` list to add or change the patterns for identifying prices.

## License

This project is open-source and available for modification or extension.
