
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
The data used in this assignment is the in class flowers-folder from UCloud (shared-drive/CDS-VIS/flowers). 

Link to flowers dataset: [flowers dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/index.html).


## Methods
To solve this assignment i have worked with ```opencv``` in order to both calculate the histograms as well as for the general image processing (using the ```calcHist```, ```imread```, ```normalize``` and ```compareHist```). Futhermore i used the ```jimshow``` and ```jimshow_channel``` from the ```utils```-folder, along with the ```matplotlib``` for plotting and visualisation.

## Usage (reproducing results)
These are the steps you will need to follow in order to get the script running and working:
- load the given data into ```input```
- make sure to install and import all necessities from ```requirements.txt``` 
- change your current working directory to the folder above src in order to get access to the input, output and utils folder as well 
- the following should be written in the command line:

      - cd src (changing the directory to the src folder in order to run the script)
      
      - python image_search.py (calling the function within the script)
      
- when processed, there will be a messagge saying that the script has succeeded and that the outputs can be seen in the output folder 



## Discussion of results
The result of this script is an image which contains one target flower image and the calculated three similar images, as well as the calculated distance scores of the images. Furthermore, a csv file is made with the results (similar images). 

For further development, it could have been interesting to look at how to make the script run with a user defined input. Since this code have already been through a transision from jupiter notebook to .py script, it would not have been much change to do. For the user to parse an argument via the command line when running the code, the script would have been more reproduceble/reuseble, because of the fact that the user wpuld be able to define the target image themselves. 

