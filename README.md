# UOB Task 

## Task 1 - NameMatch

#### 1. Problem Statement 

Provide 3 ideas for matching the company names. 

- S1: Quick hack, fast turnaround/computational time of reasonable accuracy. Need to see the actual implementation in code.
- S2: Good accuracy with reasonable turnaround/computational time. Need to see the actual implementation in code.
- S3: State of arts accuracy, potentially consider deep learning or other technique. You can just show concept, if there is no time for implementation or generate more data at your own method.

#### 2. Solution Explanation

The solution 1 and 2 are implemented in the *'match.py'* with **class BslNameMatcher()** and **AdNameMatcher()** 

- The **BslNameMatcher()** is simple and quick solution that basically doing 3 things 
  - Text Normalization
  - Synonyms alignment : Limited vs LTD ..etc 
  - Decorated-wording removal : holding ...etc 
- The **AdNameMatcher**() is an advanced version that handle 2 general abbreviation patterns, this solution basically solves the given problem. 
- Ex apple & orange -> a&o
- Ex, (singapore) -> (s) 

For more advanced solution 3, SOTA accuracy, I would think a solution that is similar to recommend system. By maintain a company-name table in database + similarity search. The uuid of company name can be treated as the index of the table. The value could be a list of its variants.  Ex: 

```
Apple Inc | [Apple Inc, AAPL (NASDAQ), ....etc]
```

When there is an input-company name, we can then recommend the most likely result.

#### 3. Script Usage Explanation

- by running 

- ```bash
  python match.py
  ```

- It will generated *"advance_output.csv"* and *"basic_output.csv"* as the output for the given problem. 

- There are 2 columns in the csv table. **Key** represents the aligned/processed result and **Value** represents the raw company name given in Table A and Table B.



## Task 2 - NameExtraction 

#### 1. Problem Statement 

- Given news or articles, we are interested to know what companies/organizations are mentioned in the news. A common approach is to apply NER technique to extract organization names. Attached ‘NameExtraction.xlsx’ file contains the dataset of some online news/articles. The task is to identify and extract all the company names from the title and content, and save them into “company names” column. 

#### 2. Solution Explanation

- The solution is implemented in *'extract.py'* 
- The idea is to leverage the existing model to do NER task. The BERT-NER model pertained on dataset CoNLL-2003 is adopted in this solution. The max length of input sentence to the model is 512. There are 4 categories in CoNLL-2003 where is PER, ORG, LOC, MISC. 
- The pretrained model can be download here https://1drv.ms/u/s!Auc3VRul9wo5hgr8jwhFD8iPCYp1?e=UsJJ2V

#### 3. Script Usage Explanation

- by running 

- ```
  python extract.py -p [input excel path] -m [model folder path]
  ```

- It will generated *"extract_output.csv"* as the output for the given problem. 

- The default model folder path is *"ner_bert_large"* 

- The default input excel path is  *"NameExtraction.xlsx"*

- The running time on my local PC without GPU is about 20 mins for given 83 rows. It could be much faster if have GPUs. 

