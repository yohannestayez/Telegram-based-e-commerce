def load_conll_dataset(file_path):
    sentences = []
    sentence = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == "":
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                word, tag = line.split()
                sentence.append((word, tag))
        
        if sentence:  # Add the last sentence if file doesn't end with a blank line
            sentences.append(sentence)

    return sentences



