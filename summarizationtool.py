# TEXT SUMMARIZATION TOOL USING NLP
import nltk
def summarize_text(text, num_sentences=2):

    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Tokenize words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))

    # Create frequency table
    word_freq = {}

    for word in words:
        if word.isalnum() and word not in stop_words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

    # Score sentences
    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # Select top sentences
    summary_sentences = nlargest(num_sentences,
                                 sentence_scores,
                                 key=sentence_scores.get)

    # Create summary
    summary = ' '.join(summary_sentences)

    return summary


# Main Program
if __name__ == "__main__":

    text = """
    Artificial Intelligence is changing the world rapidly.
    Natural Language Processing helps computers understand human language.
    Text summarization is an important application of NLP.
    It converts lengthy articles into short summaries.
    Python provides many libraries for NLP tasks.
    """

    print("ORIGINAL TEXT:\n")
    print(text)

    summary = summarize_text(text, 2)

    print("\nSUMMARIZED TEXT:\n")
    print(summary)

