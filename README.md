
# Language Analytics - Spring 2022
# Portfolio Assignment 1

This repository contains the code and descriptions from the first assigned project of the Spring 2022 module Language Analytics as part of the bachelor's tilvalg in Cultural Data Science at Aarhus University - whereas the overall Language Analytics portfolio (zip-file) consist of 5 projects, 4 class assignments + 1 self-assigned.

## Repo structure
### This repository has the following directory structure:

| **Folder** | **Description** |
| ----------- | ----------- |
| ```input``` | Contains the input data (will be empty) |
| ```output``` | Contains the results (outputs like plots or reports)  |
| ```src``` | Contains code for assignment 1 |
| ```utils``` | Contains utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), and which have been used in the assignments |

Also containing a ```MITLICENSE``` for guidelines of how to reproduce and use the data in this repository, as well as a ```.txt``` reqirements-file, where the required installments will be listed.

## Assignment description
The official description of the assignment from github/brightspace: [assignment description](https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment1.md).

For this assignment, you will write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered. Your script should do the following:

- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.


### The goal of the assignment 
The goal of this assignment was to demonstrate that we have a good understanding of how to use simple text processing techniques to extract valuable information from text data. Essentially we are attemping to replicate the kind of functionality available in the online web interfaces that we saw last week but on a dataset of our choosing.

### Data source
The data used in this assignment is the in class folder from UCloud (shared-drive/CDS-VIS/100_english_novels/corpus). 

Link to the 100_english_novels dataset: [english novels](https://github.com/computationalstylistics/100_english_novels).


## Methods
To solve this assignment i have worked with ```spacy``` for basic ```nlp (natural language processing)``` and ```spacy.load("en_core_web_sm")``` which is a small English pipeline trained on written web. Furthermore, i used ```re```in order to perform ```regex```on the text, as well as ```pandas```and ```os``` for defining filepaths.

## Usage (reproducing results)
These are the steps you will need to follow in order to get the script running and working:
- load the given data into ```input```
- make sure to install and import all necessities from ```requirements.txt``` 
- change your current working directory to the folder above src in order to get access to the input, output and utils folder as well 
- the following should be written in the command line:

      - cd src (changing the directory to the src folder in order to run the script)
      
      - python collocate_tool.py (calling the function within the script)
      
- when processed, there will be a messagge saying that the script has succeeded and that the outputs can be seen in the output folder 



## Discussion of results
The reuslts of this assignment shows a table (.csv) of valuable information from the chosen text, shuch as the words, it's collocate count, word count and the mutual information scores for all words close to the target keyword = "love". For futher development it would could be useful to have made the script capable of runnign trough a whole corpus of texts and then creating a table with the above informations for each text in that corpus. 

