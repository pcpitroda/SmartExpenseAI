import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "smartexpense.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        confidence REAL NOT NULL DEFAULT 0.85,
        date TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()

    # Seed sample expenses if table is brand new
    cursor.execute("SELECT COUNT(*) FROM expenses;")
    count = cursor.fetchone()[0]
    if count == 0:
        seed_sample_expenses(conn)

    conn.close()
    print("Database initialized successfully.")

def seed_sample_expenses(conn):
    sample_data = [
        ("Pizza at Domino's", 350.0, "Food", 0.94, "2026-09-22 13:15:00"),
        ("Uber ride to college", 280.0, "Travel", 0.91, "2026-09-21 09:30:00"),
        ("New sneakers from Nike", 3499.0, "Shopping", 0.96, "2026-09-20 18:45:00"),
        ("Udemy Python ML Course", 499.0, "Education", 0.93, "2026-09-18 11:20:00"),
        ("PVR Movie Tickets", 650.0, "Entertainment", 0.89, "2026-09-16 20:00:00"),
        ("Wi-Fi Fiber Monthly Bill", 899.0, "Bills & Utilities", 0.95, "2026-09-14 10:10:00"),
        ("Groceries from Supermarket", 1240.0, "Food", 0.92, "2026-09-12 17:30:00"),
        ("Zomato Biryani Lunch", 420.0, "Food", 0.95, "2026-09-10 14:00:00"),
        ("Petrol for Bike", 500.0, "Travel", 0.88, "2026-09-08 08:45:00"),
        ("Mobile Postpaid Recharge", 399.0, "Bills & Utilities", 0.91, "2026-09-05 16:20:00")
    ]
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO expenses (description, amount, category, confidence, date)
        VALUES (?, ?, ?, ?, ?);
    """, sample_data)
    conn.commit()

def add_expense(description, amount, category, confidence=0.85, date_str=None):
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (description, amount, category, confidence, date)
        VALUES (?, ?, ?, ?, ?);
    """, (description, amount, category, confidence, date_str))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return {
        "id": new_id,
        "description": description,
        "amount": amount,
        "category": category,
        "confidence": confidence,
        "date": date_str
    }

def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, amount, category, confidence, date FROM expenses ORDER BY id DESC;")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) as total_spending, COUNT(*) as total_transactions, AVG(amount) as avg_transaction FROM expenses;")
    row = cursor.fetchone()
    total_spending = row["total_spending"] or 0.0
    total_transactions = row["total_transactions"] or 0
    avg_transaction = row["avg_transaction"] or 0.0
    
    cursor.execute("""
        SELECT category, SUM(amount) as total, COUNT(*) as count 
        FROM expenses 
        GROUP BY category 
        ORDER BY total DESC;
    """)
    cat_rows = cursor.fetchall()
    
    category_breakdown = []
    top_category = "None"
    max_cat_amount = 0
    
    for r in cat_rows:
        cat_total = r["total"] or 0.0
        category_breakdown.append({
            "category": r["category"],
            "total": cat_total,
            "count": r["count"]
        })
        if cat_total > max_cat_amount:
            max_cat_amount = cat_total
            top_category = r["category"]

    conn.close()

    return {
        "total_spending": round(total_spending, 2),
        "total_transactions": total_transactions,
        "avg_transaction": round(avg_transaction, 2),
        "top_category": top_category,
        "category_breakdown": category_breakdown
    }

def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?;", (expense_id,))
    conn.commit()
    conn.close()
    return True
