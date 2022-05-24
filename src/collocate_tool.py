import pandas as pd
#Installing and initialising spaCy
import spacy 
nlp = spacy.load("en_core_web_sm")

#Defining filepath and finding file
import os
filepath = os.path.join("..", "..", "CDS-LANG", "100_english_novels", "corpus", "Burnett_Princess_1905.txt")
with open(filepath, "r") as file:
    text = file.read()
    
#Making everything lowercase, so that the number of keywords does not depend on upper- or lowercase letters
#Also removing all punctuation, so that spacy will not count any punctuation as tokens, using regex
import re
text = text.lower()
text = re.sub("\W+"," ", text)

#Creating doc object which holds the text
doc = nlp(text)

# A quick regex tokenizer for splitting files below
def tokenize(input_string):
    tokenizer = re.compile(r"\W+")
    return tokenizer.split(input_string)



def collocate_tool():
    filename = os.path.join("..", "..", "CDS-LANG", "100_english_novels", "corpus", "Forster_Howards_1910.txt")
    with open(filename, "r") as f:
        text = f.read()
    
    
    keyword = "love"
    context_words = []
    window_size = 5

    # ... tokenize the text and remove punctuation
    tokenized_text = []

    for word in tokenize(text):
        # Lowercase
        lowercase = word.lower()
        # cleanup punctuation etc
        cleaned = re.sub(r'[^\w\s]', '', lowercase)
        tokenized_text.append(cleaned)
            
            
    # create temporary list
    tmp = []
    # For the target word... 
    for idx,word in enumerate(tokenized_text):
        # If it's the keyword...
        if word == keyword:
            # Left context catch start of list
            left_context = max(0, idx-window_size)
            right_context = idx+window_size
            # ... extract all words ± 5 and add to tmp list.
            full_context = tokenized_text[left_context:idx] + tokenized_text[idx+1:right_context]
            # append to list
            tmp.append(full_context)
            
    # Flatten list
    flattened_list = []
    # For each sublist in list of lists
    for sublist in tmp:
        # For each item in sublist
        for item in sublist:
            # append
            flattened_list.append(item)
    
    # Create a list of collocate counts
    collocate_counts = []

    # for every collocate 
    for word in set(flattened_list):
        # Count how often each word appears as a collocate
        count = flattened_list.count(word)
        # Append tuple of word and count to list
        collocate_counts.append((word, count))
        
        
    def MI(A, B, AB, span, corpus_size):
        score = math.log((AB * corpus_size) / (A * B * span)) / math.log(2)
        return score


    import math
    keyword_freq = tokenized_text.count(keyword)
    corpus_size = len(tokenized_text)
    outfile = "collocates.csv"


    out_list = []
    for tup in collocate_counts:
        coll_text = tup[0]
        coll_count = tup[1]
        total_occurrences = tokenized_text.count(coll_text)
        score = MI(keyword_freq, coll_count, total_occurrences, 10, corpus_size)
        out_list.append((coll_text, coll_count, total_occurrences, score))

    words = []
    count = []
    occurances = []
    score = []

    for element in out_list:
        words.append(element[0])
        count.append(element[1])
        occurances.append(element[2])
        score.append(element[3])
    
    
    all_elements = list(zip(words, count, occurances, score))
    dframe = pd.DataFrame(all_elements, columns = ["words", "collocate_count", "total_count", "MI"])
    print(dframe)
    dframe.to_csv("../output/collocate_tool.csv", encoding = "utf-8")
    
    print("Script suceeded, results can be seen in output-folder")
    
    
collocate_tool()