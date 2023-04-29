from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


# Load Our Dataset
df = pd.read_csv("dhruv_rathee_videos.csv")


# Define a function to vectorize the text data using the TfidfVectorizer
def vectorize_text(text):
    # Define the TfidfVectorizer with the desired parameters
    tfidf = TfidfVectorizer(max_features=1000, stop_words="english")

    # Fit the TfidfVectorizer to the text data and transform it to create the vector representation
    vector = tfidf.fit_transform([text])

    # Return the vector representation as a numpy array
    return vector.toarray()


# Vectorize the "Title" and "Description" columns of your dataset
def vectorize_video_text():
    df["Title"] = df["Title"].apply(lambda x: vectorize_text(x))
    df["Description"] = df["Description"].apply(lambda x: vectorize_text(x))

    # Save Vectorized Dataset
    df.to_csv("vectorized_dhruv_rathee_videos.csv")


if __name__ == "__main__":
    vectorize_video_text()
