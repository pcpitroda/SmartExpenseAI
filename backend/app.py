import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# Add model and database directories to path
sys.path.append(os.path.dirname(__file__))
from model.classifier import ExpenseClassifier
import database.db as db

app = Flask(__name__)
CORS(app)

# Initialize Classifier and Database
classifier = ExpenseClassifier()
db.init_db()

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "SmartExpense AI API is running"}), 200

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json() or {}
    description = data.get("description", "").strip()
    amount_raw = data.get("amount", 0)

    if not description:
        return jsonify({
            "error": "Expense description is required"
        }), 400

    try:
        amount = float(amount_raw)
        if amount <= 0:
            return jsonify({"error": "Expense amount must be a positive number"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid amount provided. Must be a numeric value."}), 400

    # AI Classification
    result = classifier.predict(description)
    
    return jsonify({
        "description": description,
        "amount": amount,
        "category": result["category"],
        "confidence": result["confidence"],
        "probabilities": result.get("probabilities", {})
    }), 200

@app.route("/api/expenses", methods=["POST"])
def save_expense():
    data = request.get_json() or {}
    description = data.get("description", "").strip()
    amount_raw = data.get("amount", 0)
    category = data.get("category", "").strip()
    confidence = data.get("confidence", 0.85)

    if not description or not category:
        return jsonify({"error": "Description and category are required"}), 400

    try:
        amount = float(amount_raw)
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid numeric amount"}), 400

    saved_expense = db.add_expense(
        description=description,
        amount=amount,
        category=category,
        confidence=float(confidence)
    )

    return jsonify({
        "message": "Expense saved successfully",
        "expense": saved_expense
    }), 201

@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    expenses = db.get_all_expenses()
    return jsonify({"expenses": expenses}), 200

@app.route("/api/summary", methods=["GET"])
def get_summary():
    summary_data = db.get_summary()
    return jsonify(summary_data), 200

@app.route("/api/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    db.delete_expense(expense_id)
    return jsonify({"message": f"Expense {expense_id} deleted successfully"}), 200

if __name__ == "__main__":
    print("Starting SmartExpense AI Flask Backend on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
