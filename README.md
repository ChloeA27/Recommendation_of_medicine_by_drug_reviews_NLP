# Recommendation_of_medicine_by_drug_reviews_NLP

Workflow structure 

**Data Overview**
  data load
  dataset overview
    dataset variables:
      1. drugName (categorical): name of drug
      2. condition (categorical): name of condition
      3. review (text): patient review
      4. rating (numerical): 10 star patient rating
      5. date (date): date of review entry
      6. usefulCount (numerical): number of users who found review useful
    dataset info: 
      dataset size: 215063
      dataset split: The data is split into a train (75%) a test (25%) partition and stored in two .tsv (tab-separated-values) files, respectively.
  data cleaning 
    drop NA in condition
  
**EDA (show in visualizations)**
  univariate analysis
    numerical: rating
    numerical: userfulCount
    categorial: drugName
    categorial: condition
  bivariate analysis
    drugName & rating
    condition & rating
    condition & drugName
    drugName & condition

**Data Preprocessing**
  Text analysis(review)
    tokenization 
    text normalization
    remove stopwords
    lemmatization    
      NLTK with POS Tagging
 '''
How it Works:
Uses NLTK’s pos_tag to assign POS tags (e.g., verb, noun, adjective) to each word.
Converts these tags to WordNet-compatible tags for lemmatization.
Provides context-aware lemmatization (e.g., "better" → "good" as an adjective).
Pros:
More accurate than plain WordNet lemmatizer because POS tagging adds context.
Still lightweight and fully within the NLTK framework.
Cons:
POS tagging adds computational overhead.
Slower than SpaCy for large datasets.
'''
    sentiment label
      hybrid method: lexicon-based + side effect label + extreme rating label
        lexicon used: VADER 
        side effect dataset: SIDER with nagation handle
        Extreme rating score added
        method: to address up the importance of sentiment of side effect in medicine domain, and side effect grouped by drugs.

**Reference：**

1. side effect database： 
SIDER (Side Effect Resource)
SIDER provides information on marketed medicines and their recorded adverse drug reactions (ADRs). The data is extracted from public documents and package inserts, including side effect frequency and classifications.
License: Creative Commons Attribution-Noncommercial-Share Alike 4.0 License.
http://sideeffects.embl.de/ 
