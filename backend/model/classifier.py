import os
import re
import joblib
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "smartexpense_model.joblib")

class ExpenseClassifier:
    def __init__(self):
        self.pipeline = None
        self.categories = [
            "Food", "Travel", "Shopping", "Education",
            "Entertainment", "Bills & Utilities", "Others"
        ]
        self.load_or_train()

    def load_or_train(self):
        if os.path.exists(MODEL_PATH):
            try:
                self.pipeline = joblib.load(MODEL_PATH)
                print("ExpenseClassifier: Loaded trained model from disk.")
            except Exception as e:
                print(f"ExpenseClassifier: Error loading model ({e}), retraining...")
                self._train_fallback()
        else:
            print("ExpenseClassifier: No saved model found. Training fresh model...")
            self._train_fallback()

    def _train_fallback(self):
        # Import train script directly if model not found
        import sys
        sys.path.append(os.path.join(os.path.dirname(__file__), "..", "training"))
        from train_model import build_and_train_model
        self.pipeline = build_and_train_model()

    def clean_text(self, text):
        if not text:
            return ""
        # Remove numbers, special symbols, multiple spaces
        text = text.lower().strip()
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text

    def predict(self, description):
        """
        Takes raw description string and predicts category and confidence score.
        Returns dict: { "category": str, "confidence": float, "probabilities": dict }
        """
        if not description or not description.strip():
            return {
                "category": "Others",
                "confidence": 0.50,
                "explanation": "Default assigned due to empty input description."
            }

        cleaned = self.clean_text(description)
        if not cleaned:
            return {
                "category": "Others",
                "confidence": 0.50,
                "explanation": "Default assigned due to non-alphanumeric input."
            }

        # Predict using sklearn pipeline
        probabilities = self.pipeline.predict_proba([cleaned])[0]
        classes = self.pipeline.classes_
        
        # Best prediction
        best_idx = np.argmax(probabilities)
        best_category = classes[best_idx]
        confidence = float(probabilities[best_idx])

        # If confidence is too low or out of domain, smooth confidence score for realistic representation
        confidence = round(max(0.55, min(0.98, confidence)), 2)

        return {
            "category": best_category,
            "confidence": confidence,
            "probabilities": {cls: round(float(prob), 3) for cls, prob in zip(classes, probabilities)}
        }
