import csv
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
import pickle

stemmer = PorterStemmer()

reviews = [row for row in csv.reader(open('../texts/commands_list.txt'))]
print(reviews)


def process_text(text):
    print(text)
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())
    print(text)
    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)
    print(f"tokenized text : {tokenized_text}")
    # Remove the stopwords and stem each word to its root
    clean_text = [
        stemmer.stem(word) for word in tokenized_text
        if word not in stopwords.words('english')
    ]
    print(f"clean text : {clean_text}")
    # Remember, this final output is a list of words
    return clean_text


def prepare_text():
    # Remove the first row, since it only has the labels
    # reviews = reviews[1:]

    texts = [row[0] for row in reviews]
    topics = [row[1] for row in reviews]

    # Process the texts to so they are ready for training
    # But transform the list of words back to string format to feed it to sklearn
    texts = [" ".join(process_text(text)) for text in texts]

    print(texts)
    vectors = vectorize_text(texts)
    print(vectors)
    # Split the training and test data
    vectors_train, vectors_test, topics_train, topics_test = train_test_split(vectors, topics)

    return vectors_train, vectors_test, topics_train, topics_test


def vectorize_text(texts):
    matrix = CountVectorizer(max_features=1000)
    vectors = matrix.fit_transform(texts).toarray()

    return vectors


def train(vectors_train, vectors_test, topics_train, topics_test):
    classifier = GaussianNB()
    classifier.fit(vectors_train, topics_train)

    # Predict with the testing set
    print(vectors_test)
    topics_pred = classifier.predict(vectors_test)

    # ...and measure the accuracy of the results
    print(classification_report(topics_test, topics_pred))


vectors_train, vectors_test, topics_train, topics_test = prepare_text()

train(vectors_train, vectors_test, topics_train, topics_test)


text = 'thank you Oracle for everything'
text = process_text(text)
text = ' '.join(text)
print([text])

vectors = vectorize_text([text])
print(vectors)



