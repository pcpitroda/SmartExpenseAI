import React, { useState } from 'react';
import { Search, Filter, Trash2, Receipt } from 'lucide-react';

export default function Transactions({ expenses, onDeleteExpense }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');

  const categories = ['All', 'Food', 'Travel', 'Shopping', 'Education', 'Entertainment', 'Bills & Utilities', 'Others'];

  const filteredExpenses = expenses.filter((exp) => {
    const matchesSearch = exp.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'All' || exp.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="border-b border-[#D8CEBD] pb-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="font-serif-heading text-4xl text-[#242424]">Expense Ledger</h2>
          <p className="text-[#7A8065] text-sm mt-1">
            Complete transaction record with AI category tagging.
          </p>
        </div>

        {/* Filter Controls */}
        <div className="flex flex-col sm:flex-row items-center gap-3">
          {/* Search */}
          <div className="relative w-full sm:w-64">
            <Search className="w-4 h-4 absolute left-3 top-3 text-[#7A8065]" />
            <input
              type="text"
              placeholder="Search expenses..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-4 py-2 text-sm bg-[#FAF6F0] border border-[#D8CEBD] text-[#242424] focus:outline-none focus:border-[#1F4D3A]"
            />
          </div>

          {/* Category Filter */}
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="w-full sm:w-44 px-3 py-2 text-sm bg-[#FAF6F0] border border-[#D8CEBD] text-[#242424] focus:outline-none focus:border-[#1F4D3A]"
          >
            {categories.map((cat) => (
              <option key={cat} value={cat}>
                {cat === 'All' ? 'All Categories' : cat}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Ledger Table Container */}
      <div className="paper-card overflow-hidden">
        {filteredExpenses.length === 0 ? (
          <div className="text-center py-16 text-[#7A8065]">
            <Receipt className="w-8 h-8 mx-auto opacity-50 mb-2" />
            <p className="text-sm font-medium">No matching transactions found in ledger.</p>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="ledger-table">
              <thead>
                <tr>
                  <th>DATE</th>
                  <th>DESCRIPTION</th>
                  <th>AMOUNT</th>
                  <th>AI CATEGORY</th>
                  <th>CONFIDENCE</th>
                  <th className="text-right">ACTION</th>
                </tr>
              </thead>
              <tbody>
                {filteredExpenses.map((exp) => (
                  <tr key={exp.id}>
                    <td className="text-xs font-mono text-[#7A8065]">
                      {exp.date ? exp.date.split(' ')[0] : 'N/A'}
                    </td>
                    <td className="font-medium text-[#242424]">{exp.description}</td>
                    <td className="font-bold text-[#1F4D3A]">
                      ₹{exp.amount.toLocaleString('en-IN')}
                    </td>
                    <td>
                      <span className="inline-block px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wider bg-[#E8DDCB] text-[#1F4D3A] border border-[#D8CEBD]">
                        {exp.category}
                      </span>
                    </td>
                    <td className="font-mono text-xs text-[#7A8065]">
                      {exp.confidence ? `${Math.round(exp.confidence * 100)}%` : '85%'}
                    </td>
                    <td className="text-right">
                      <button
                        onClick={() => onDeleteExpense(exp.id)}
                        className="text-[#C96B4B] hover:text-[#a54f32] p-1 transition-colors"
                        title="Delete entry"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      <div className="text-xs text-[#7A8065] text-right font-mono">
        Showing {filteredExpenses.length} of {expenses.length} total recorded entries
      </div>
    </div>
  );
}
