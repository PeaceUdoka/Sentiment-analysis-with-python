# Sentiment-analysis-with-python
This repository contains all deliverables on the Sentiment analysis project for the FliT Data Analytics/Data Science Apprenticeship Program.

## Overview
This project involves building a model that can classify each review as positive, negative, or neutral based on the text content. The dataset contains reviews on Amazon products and is publicly available. 

## Steps
1. **Data Import:**
   - The dataset was loaded into a Jupyter notebook and necessary libraries were imported. You may be required to install wordcloud if not already on your environment.
   
2. **Data Exploration:**
   - Visualised the data using word clouds and seaborn plots. Generated a new feature to count the number of words in each review. It was discovered that majority of the reviews were positive and that negative reviews had more words.
    
3. **Building the Model:**
   - The problem was identified as a classification problem and the LogisticRegression classifier was used to build the model. On evaluation of the model, it was found to perform well with an accuracy score of 89.465%.
  
## Further Work
More work can be done to improve the model performance through stemming and applying other model classifiers.
