import re
from pathlib import Path

import nltk
import pandas as pd

from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer


nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("vader_lexicon", quiet=True)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "clean_survey_data.csv"


def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    words = []

    for word in tokens:

        if word not in stop_words:

            words.append(word)

    return " ".join(words)


def process_text():

    df = pd.read_csv(DATA_PATH)

    df["clean_comment"] = df["open_comment"].apply(clean_text)

    analyzer = SentimentIntensityAnalyzer()

    sentiment_scores = []

    for sentence in df["clean_comment"]:

        score = analyzer.polarity_scores(sentence)["compound"]

        sentiment_scores.append(score)

    df["sentiment_score"] = sentiment_scores

    vectorizer = TfidfVectorizer(max_features=50)

    tfidf = vectorizer.fit_transform(df["clean_comment"])

    tfidf_df = pd.DataFrame(

        tfidf.toarray(),

        columns=vectorizer.get_feature_names_out()

    )

    df = pd.concat(

        [

            df.reset_index(drop=True),

            tfidf_df.reset_index(drop=True)

        ],

        axis=1

    )

    df.to_csv(DATA_PATH, index=False)

    print()

    print("NLP Processing Completed")

    print()

    print("Rows :", df.shape[0])

    print("Columns :", df.shape[1])

    print()

    print("Added")

    print("- clean_comment")

    print("- sentiment_score")

    print("- TF-IDF features")


if __name__ == "__main__":

    process_text()