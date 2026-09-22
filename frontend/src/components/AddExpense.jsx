import React, { useState } from 'react';
import { Sparkles, CheckCircle2, AlertCircle, Loader2, ArrowRight } from 'lucide-react';

export default function AddExpense({ onExpenseAdded }) {
  const [amount, setAmount] = useState('');
  const [description, setDescription] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [savedSuccess, setSavedSuccess] = useState(false);

  // Category commentary mapping for editorial touch
  const categoryCommentary = {
    'Food': 'Looks like a dining or grocery expense.',
    'Travel': 'Appears to be a commute or transport charge.',
    'Shopping': 'Classified as retail or online merchandise.',
    'Education': 'Identified as learning, course, or tuition fee.',
    'Entertainment': 'Categorized under recreation or leisure activity.',
    'Bills & Utilities': 'Recognized as recurring bill or utility payment.',
    'Others': 'Grouped under general miscellaneous expenditure.'
  };

  const handlePredict = async (e) => {
    e.preventDefault();
    setError(null);
    setPrediction(null);
    setSavedSuccess(false);

    if (!description.trim()) {
      setError('Please enter what you spent money on.');
      return;
    }
    const numAmount = parseFloat(amount);
    if (isNaN(numAmount) || numAmount <= 0) {
      setError('Please enter a valid positive numeric amount.');
      return;
    }

    setLoading(true);

    try {
      const res = await fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description, amount: numAmount })
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Failed to predict category');
      }

      setPrediction(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    if (!prediction) return;
    setSaving(true);
    setError(null);

    try {
      const res = await fetch('/api/expenses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          description: prediction.description,
          amount: prediction.amount,
          category: prediction.category,
          confidence: prediction.confidence
        })
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Failed to save expense');
      }

      setSavedSuccess(true);
      setAmount('');
      setDescription('');
      setPrediction(null);
      if (onExpenseAdded) onExpenseAdded();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      {/* Heading */}
      <div className="border-b border-[#D8CEBD] pb-4">
        <h2 className="font-serif-heading text-4xl text-[#242424]">Record an expense</h2>
        <p className="text-[#7A8065] text-sm mt-1">
          Fill out receipt details and let SmartExpense AI auto-tag your transaction.
        </p>
      </div>

      {/* Success Notification */}
      {savedSuccess && (
        <div className="bg-[#EFE8DC] border border-[#1F4D3A] p-4 flex items-center justify-between text-[#1F4D3A]">
          <div className="flex items-center gap-3">
            <CheckCircle2 className="w-5 h-5 text-[#1F4D3A]" />
            <span className="font-medium text-sm">Expense successfully recorded in ledger!</span>
          </div>
          <button
            onClick={() => setSavedSuccess(false)}
            className="text-xs uppercase font-bold text-[#7A8065] hover:underline"
          >
            Dismiss
          </button>
        </div>
      )}

      {/* Error Notification */}
      {error && (
        <div className="bg-[#FDF2F2] border border-[#C96B4B] p-4 flex items-center gap-3 text-[#C96B4B]">
          <AlertCircle className="w-5 h-5 flex-shrink-0" />
          <span className="text-sm font-medium">{error}</span>
        </div>
      )}

      {/* Entry Form */}
      <form onSubmit={handlePredict} className="paper-card p-6 space-y-6">
        <div>
          <label className="block text-xs font-bold uppercase tracking-wider text-[#7A8065] mb-2">
            AMOUNT (₹)
          </label>
          <div className="relative">
            <span className="absolute left-4 top-3 text-[#7A8065] font-serif text-lg">₹</span>
            <input
              type="number"
              step="any"
              placeholder="250"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              className="w-full pl-9 pr-4 py-3 bg-[#F6F1E8] border border-[#D8CEBD] text-[#242424] font-mono text-lg font-bold focus:outline-none focus:border-[#1F4D3A]"
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-bold uppercase tracking-wider text-[#7A8065] mb-2">
            WHAT DID YOU SPEND ON?
          </label>
          <input
            type="text"
            placeholder="e.g. Pizza at Domino's, Uber to airport, Course fee..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-4 py-3 bg-[#F6F1E8] border border-[#D8CEBD] text-[#242424] text-base focus:outline-none focus:border-[#1F4D3A]"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-[#1F4D3A] text-[#F6F1E8] py-3.5 px-6 font-medium text-sm uppercase tracking-wider border border-[#173B2D] hover:bg-[#183E2F] transition-all flex items-center justify-center gap-2"
        >
          {loading ? (
            <>
              <Loader2 className="w-4 h-4 animate-spin" />
              <span>Analyzing text with AI...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-4 h-4 text-[#C96B4B]" />
              <span>Ask SmartExpense</span>
            </>
          )}
        </button>
      </form>

      {/* AI Prediction Result Receipt Stamp */}
      {prediction && (
        <div className="ai-stamp p-6 space-y-5 animate-fade-in">
          <div className="border-b border-[#D8CEBD] pb-3">
            <span className="text-xs font-bold tracking-widest text-[#7A8065] uppercase">
              AI CLASSIFICATION RESULT
            </span>
          </div>

          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <div className="font-serif-heading text-4xl font-bold text-[#1F4D3A] uppercase tracking-wide">
                {prediction.category}
              </div>
              <p className="text-sm italic text-[#7A8065] mt-1">
                "{categoryCommentary[prediction.category] || 'Classified by model.'}"
              </p>
            </div>

            <div className="text-right sm:border-l sm:border-[#D8CEBD] sm:pl-6">
              <div className="text-xs font-mono uppercase text-[#7A8065]">Confidence</div>
              <div className="font-mono text-2xl font-bold text-[#C96B4B]">
                {Math.round(prediction.confidence * 100)}%
              </div>
            </div>
          </div>

          {/* Details recap */}
          <div className="bg-[#FAF6F0] p-4 border border-[#D8CEBD] text-xs font-mono space-y-1 text-[#242424]">
            <div>ITEM: {prediction.description}</div>
            <div>AMOUNT: ₹{prediction.amount.toLocaleString('en-IN')}</div>
          </div>

          <button
            onClick={handleSave}
            disabled={saving}
            className="w-full bg-[#242424] text-[#F6F1E8] py-3.5 px-6 font-bold text-sm uppercase tracking-wider hover:bg-[#383838] transition-all flex items-center justify-center gap-2"
          >
            {saving ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>Saving to Ledger...</span>
              </>
            ) : (
              <>
                <span>Save Expense</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      )}
    </div>
  );
}
