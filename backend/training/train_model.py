import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from dataset import TRAINING_DATA

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "smartexpense_model.joblib")

def build_and_train_model():
    """
    Trains a TF-IDF + Logistic Regression classification model on the expense dataset.
    Saves the pipeline to joblib.
    """
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    texts = [item[0] for item in TRAINING_DATA]
    labels = [item[1] for item in TRAINING_DATA]
    
    # Create Pipeline with TF-IDF Vectorizer and Logistic Regression
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=1,
            lowercase=True,
            sublinear_tf=True
        )),
        ('clf', LogisticRegression(
            C=1.5,
            max_iter=1000,
            solver='lbfgs',
            random_state=42
        ))
    ])
    
    pipeline.fit(texts, labels)
    
    # Calculate training accuracy
    accuracy = pipeline.score(texts, labels)
    print(f"Model successfully trained on {len(texts)} samples.")
    print(f"Training Accuracy: {accuracy * 100:.2f}%")
    
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    return pipeline

if __name__ == "__main__":
    build_and_train_model()
