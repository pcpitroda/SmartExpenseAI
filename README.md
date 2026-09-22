# SmartExpense AI 💰🤖

SmartExpense AI is a full-stack expense management application that uses Machine Learning to automatically classify expenses into meaningful categories.

The project combines a modern React frontend with a Flask backend and a Scikit-learn based text classification model.

## 🚀 Features

* Add and manage expenses
* AI-powered expense categorization
* Automatic category prediction from expense descriptions
* Prediction confidence score
* Expense transaction history
* Expense summary dashboard
* Category-wise spending analysis
* Average transaction calculation
* Top spending category detection
* Delete transactions
* REST API powered by Flask
* SQLite database for local expense storage

## 🧠 AI / Machine Learning

SmartExpense AI uses a text classification pipeline built with:

* TF-IDF Vectorization
* Logistic Regression
* Scikit-learn
* Joblib

The model classifies expense descriptions into 7 categories:

1. Food
2. Travel
3. Shopping
4. Education
5. Entertainment
6. Bills & Utilities
7. Others

### Example

Input:

```text
Pizza at Domino's
```

Possible prediction:

```text
Category: Food
Confidence: 94%
```

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS
* JavaScript
* Lucide React

### Backend

* Python
* Flask
* Flask-CORS
* SQLite

### Machine Learning

* Scikit-learn
* TF-IDF
* Logistic Regression
* Joblib
* NumPy
* Pandas

## 📁 Project Structure

```text
SmartExpenseAI/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── backend/
│   ├── database/
│   │   └── db.py
│   ├── model/
│   │   ├── classifier.py
│   │   └── smartexpense_model.joblib
│   ├── training/
│   │   ├── dataset.py
│   │   └── train_model.py
│   ├── app.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartExpenseAI.git
cd SmartExpenseAI
```

## 🔧 Backend Setup

Open a terminal inside the project:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

Backend will run on:

```text
http://127.0.0.1:5000
```

Health check:

```text
http://127.0.0.1:5000/api/health
```

## 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend will run on:

```text
http://localhost:5173
```

The Vite development server proxies `/api` requests to the Flask backend running on port `5000`.

## 🔌 API Endpoints

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| GET    | `/api/health`        | Check backend status     |
| POST   | `/api/predict`       | Predict expense category |
| POST   | `/api/expenses`      | Save an expense          |
| GET    | `/api/expenses`      | Get all expenses         |
| GET    | `/api/summary`       | Get expense summary      |
| DELETE | `/api/expenses/<id>` | Delete an expense        |

### Prediction Request

```json
{
  "description": "Pizza at Domino's",
  "amount": 350
}
```

### Prediction Response

```json
{
  "description": "Pizza at Domino's",
  "amount": 350,
  "category": "Food",
  "confidence": 0.94
}
```

## 🧪 Training the Model

The model can be retrained using the included training script:

```bash
cd backend/training
python train_model.py
```

The trained model is saved as:

```text
backend/model/smartexpense_model.joblib
```

## 🔐 GitHub Safety

Do not commit sensitive or generated files such as:

* `.env`
* `node_modules/`
* `__pycache__/`
* `*.pyc`
* local virtual environments
* local database files

These files should be excluded using `.gitignore`.

## 🎯 Project Purpose

SmartExpense AI demonstrates how Machine Learning can be integrated into a practical full-stack application to automate expense categorization and provide useful spending insights.

## 👨‍💻 Author

**Priyanshi Pitroda**

Built using React, Flask, SQLite and Scikit-learn.
