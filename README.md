# TEXT_SUMMARIZATION_TOOL

*COMPANY*: CODTECH IT SOLUTIONS

I*NAME*: Shreya Vilas Bondre

 *INTERN ID*: CTIS7717

*DOMAIN*: Artificial Intelligence

 *DURATION*: 8 WEEEKS

 *MENTOR*: NEELA SANTOSH

 This project is developed using Python in Google Colab. The main purpose of this program is to summarize long text into a short and meaningful summary using Natural Language Processing (NLP) techniques.

The program uses the NLTK (Natural Language Toolkit) library, which provides various functions for text processing. First, the input paragraph is divided into sentences using sentence tokenization. Then, the text is converted into words using word tokenization. Common English stopwords such as “is”, “the”, “and”, etc., are removed because they do not contribute much meaning to the summary.

After removing stopwords, the program creates a frequency table to count how many times important words appear in the text. Based on these word frequencies, each sentence is given a score. Sentences containing more important words receive higher scores.

Finally, the program selects the top-ranked sentences using the nlargest() function from the heapq module and combines them to generate a summarized version of the original text.

This project helps in reducing lengthy articles into short summaries quickly and efficiently. It is useful in applications such as news summarization, document analysis, research papers, and content management systems.

Technologies Used
Python Programming
Natural Language Processing (NLP)
NLTK Library
Google Colab

 *OUTPUT*
 <img width="758" height="268" alt="Image" src="https://github.com/user-attachments/assets/710477d9-0a4f-44da-8a37-38cc36dc1d0a" />
