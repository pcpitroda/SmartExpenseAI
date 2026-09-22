import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Overview from './components/Overview';
import AddExpense from './components/AddExpense';
import Transactions from './components/Transactions';
import Insights from './components/Insights';
import AboutAI from './components/AboutAI';
import { Loader2, AlertTriangle } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');
  const [expenses, setExpenses] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch expenses and summary metrics from Flask backend
  const fetchData = async () => {
    try {
      const [expRes, sumRes] = await Promise.all([
        fetch('/api/expenses'),
        fetch('/api/summary')
      ]);

      if (!expRes.ok || !sumRes.ok) {
        throw new Error('Failed to connect to backend server');
      }

      const expData = await expRes.json();
      const sumData = await sumRes.json();

      setExpenses(expData.expenses || []);
      setSummary(sumData);
      setError(null);
    } catch (err) {
      console.error('API Fetch Error:', err);
      setError('Unable to load data from Flask backend API. Please make sure backend is running on port 5000.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDeleteExpense = async (id) => {
    try {
      const res = await fetch(`/api/expenses/${id}`, { method: 'DELETE' });
      if (res.ok) {
        fetchData();
      }
    } catch (err) {
      console.error('Failed to delete expense:', err);
    }
  };

  return (
    <div className="min-h-screen bg-[#F6F1E8] text-[#242424] flex flex-col font-sans">
      {/* Top Header */}
      <Header activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Content Body */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-6 py-8">
        {loading ? (
          <div className="flex flex-col items-center justify-center py-24 space-y-4">
            <Loader2 className="w-8 h-8 text-[#1F4D3A] animate-spin" />
            <p className="font-serif-heading text-lg text-[#7A8065]">Loading SmartExpense Journal...</p>
          </div>
        ) : error ? (
          <div className="paper-card p-8 border-l-4 border-l-[#C96B4B] space-y-4">
            <div className="flex items-center gap-3 text-[#C96B4B]">
              <AlertTriangle className="w-6 h-6" />
              <h3 className="font-serif-heading text-xl font-bold">Backend Connection Error</h3>
            </div>
            <p className="text-sm text-[#242424]">{error}</p>
            <button
              onClick={fetchData}
              className="bg-[#1F4D3A] text-[#F6F1E8] px-4 py-2 text-xs font-bold uppercase tracking-wider hover:bg-[#173B2D]"
            >
              Retry Connection
            </button>
          </div>
        ) : (
          <>
            {activeTab === 'overview' && (
              <Overview
                summary={summary}
                expenses={expenses}
                setActiveTab={setActiveTab}
              />
            )}

            {activeTab === 'add' && (
              <AddExpense
                onExpenseAdded={() => {
                  fetchData();
                  setActiveTab('overview');
                }}
              />
            )}

            {activeTab === 'transactions' && (
              <Transactions
                expenses={expenses}
                onDeleteExpense={handleDeleteExpense}
              />
            )}

            {activeTab === 'insights' && (
              <Insights summary={summary} />
            )}

            {activeTab === 'about' && (
              <AboutAI />
            )}
          </>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-[#D8CEBD] py-6 bg-[#F6F1E8] text-center text-xs text-[#7A8065] font-mono">
        SmartExpense AI — Tiny AI Prototype | Built with React, Flask & Scikit-Learn
      </footer>
    </div>
  );
}
