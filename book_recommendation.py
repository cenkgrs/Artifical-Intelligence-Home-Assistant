import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from difflib import get_close_matches

books = pd.read_csv('csv/books.csv', encoding = "ISO-8859-1")
ratings = pd.read_csv('csv/ratings.csv', encoding = "ISO-8859-1")
book_tags = pd.read_csv('csv/book_tags.csv', encoding = "ISO-8859-1")
tags = pd.read_csv('csv/tags.csv')
tags_join_DF = pd.merge(book_tags, tags, left_on='tag_id', right_on='tag_id', how='inner')
to_read = pd.read_csv('csv/to_read.csv')

# TF -> Term Frequency - > Verinin dökümanda geçme sayısı
# IDF -> Inverse Document Frequency -> Verinin geçtiği döküman sayısı

# Data transforming into vectors
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')

# Her yazar için tf/idf matrixi oluşturuluyor
tfidf_matrix = tf.fit_transform(books['authors'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Build a 1-dimensional array with book titles
titles = books['title']
indices = pd.Series(books.index, index=books['title'])


# Function that get book recommendations based on the cosine similarity score of book authors
def authors_recommendations(title):
    idx = indices[title]
    # Get cosine_sim of this book to other books
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the sim scores so we can get the highest 20
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the highest 20 sim score
    sim_scores = sim_scores[1:21]
    # Get book indices of this sim scores
    book_indices = [i[0] for i in sim_scores]

    # Return title of that book indices
    return titles.iloc[book_indices]


# This function will return similar inputs
def get_book_matches(word):
    # Uses get_close_matches from difflib and find matches from titles list
    books = get_close_matches(word, titles)

    if books:
        return books

    return False


def get_book_recommendations(title):
    book_results = []
    didMatch = get_book_matches(title)

    # If there is a book that matches input
    if didMatch:
        results = authors_recommendations(title)
        for book in results:
            book_results.append(book)

        return book_results
    else:
        return False


