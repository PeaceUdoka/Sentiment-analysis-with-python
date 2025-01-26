# Sentiment-analysis-with-python
This repository contains all deliverables on the Sentiment analysis project for the FliT Data Analytics/Data Science Apprenticeship Program.

## Overview
This project involves building a model that can classify each review as positive or negative based on the text content. The dataset contains reviews on an Amazon product and is publicly for download on this repo. 

## Steps
1. **Data Import:**
   - The dataset was loaded into a Jupyter notebook and necessary libraries were imported. You may be required to install wordcloud and nltk if not already on your environment.
   
2. **Data Exploration:**
   - Removed html tags, urls, punctuations from the review body. Visualised the data using word clouds and seaborn plots. Generated a new feature to count the number of words in each review. It was discovered that majority of the reviews were positive and that negative reviews had more words.
    
3. **Building the Model:**
   - The problem was identified as a classification problem and several classifiers were used to train the model. The logistic regression binary classififier gave the highest accuracy with the lowest false positives and false negatives.
  

