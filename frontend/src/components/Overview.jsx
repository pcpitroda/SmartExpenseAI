import React from 'react';
import { ArrowRight, Sparkles, Receipt, PieChart } from 'lucide-react';

export default function Overview({ summary, expenses, setActiveTab }) {
  const totalSpending = summary?.total_spending || 0;
  const totalTransactions = summary?.total_transactions || 0;
  const topCategory = summary?.top_category || 'N/A';
  const categoryBreakdown = summary?.category_breakdown || [];

  // Muted color map for editorial look
  const categoryColors = {
    'Food': '#1F4D3A',          // Forest Green
    'Travel': '#C96B4B',        // Terracotta
    'Shopping': '#7A8065',      // Muted Olive
    'Education': '#5C6B73',     // Slate Blue/Gray
    'Entertainment': '#9E5A47', // Muted Rust
    'Bills & Utilities': '#3D5A50', // Dark Sage
    'Others': '#8C857B'         // Warm Muted Gray
  };

  return (
    <div className="space-y-8">
      {/* Editorial Header */}
      <div className="border-b border-[#D8CEBD] pb-6">
        <h2 className="font-serif-heading text-4xl font-normal text-[#242424]">
          Where did my money go?
        </h2>
        <p className="text-[#7A8065] text-base mt-2">
          A simple AI-assisted view of your everyday spending.
        </p>
      </div>

      {/* Editorial Summary Banner */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="paper-card p-6 border-l-4 border-l-[#1F4D3A]">
          <div className="text-xs font-semibold tracking-wider text-[#7A8065] uppercase">
            THIS MONTH
          </div>
          <div className="font-serif-heading text-3xl font-bold text-[#242424] mt-2">
            ₹{totalSpending.toLocaleString('en-IN')}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Total recorded expenditure</div>
        </div>

        <div className="paper-card p-6 border-l-4 border-l-[#C96B4B]">
          <div className="text-xs font-semibold tracking-wider text-[#7A8065] uppercase">
            TRANSACTIONS
          </div>
          <div className="font-serif-heading text-3xl font-bold text-[#242424] mt-2">
            {totalTransactions}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Logged in journal</div>
        </div>

        <div className="paper-card p-6 border-l-4 border-l-[#7A8065]">
          <div className="text-xs font-semibold tracking-wider text-[#7A8065] uppercase">
            TOP CATEGORY
          </div>
          <div className="font-serif-heading text-3xl font-bold text-[#1F4D3A] mt-2">
            {topCategory}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Highest spending bucket</div>
        </div>
      </div>

      {/* Spending Breakdown Section */}
      <div className="paper-card p-6">
        <div className="flex items-center justify-between border-b border-[#D8CEBD] pb-4 mb-6">
          <h3 className="font-serif-heading text-2xl text-[#242424]">
            Spending Breakdown
          </h3>
          <span className="text-xs text-[#7A8065] uppercase font-mono">By Category</span>
        </div>

        {categoryBreakdown.length === 0 ? (
          <div className="text-center py-12 text-[#7A8065]">
            No expenses logged yet. Add your first transaction to view breakdown!
          </div>
        ) : (
          <div className="space-y-5">
            {categoryBreakdown.map((item) => {
              const percentage = totalSpending > 0 ? ((item.total / totalSpending) * 100).toFixed(1) : 0;
              const barColor = categoryColors[item.category] || '#7A8065';

              return (
                <div key={item.category} className="space-y-1.5">
                  <div className="flex items-center justify-between text-sm font-medium">
                    <span className="uppercase tracking-wider font-semibold text-[#242424]">
                      {item.category}
                    </span>
                    <div className="flex items-center gap-3">
                      <span className="text-[#7A8065] text-xs">({percentage}%)</span>
                      <span className="font-bold text-[#1F4D3A]">₹{item.total.toLocaleString('en-IN')}</span>
                    </div>
                  </div>
                  {/* Progress Bar */}
                  <div className="w-full bg-[#E8DDCB] h-3 rounded-none overflow-hidden border border-[#D8CEBD]">
                    <div
                      className="h-full bar-fill"
                      style={{
                        width: `${percentage}%`,
                        backgroundColor: barColor
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* Recent Entries Ledger Preview */}
      <div className="paper-card p-6">
        <div className="flex items-center justify-between border-b border-[#D8CEBD] pb-4 mb-4">
          <h3 className="font-serif-heading text-xl text-[#242424]">Recent Journal Entries</h3>
          <button
            onClick={() => setActiveTab('transactions')}
            className="text-xs font-semibold text-[#1F4D3A] hover:underline flex items-center gap-1"
          >
            <span>View All</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {expenses.length === 0 ? (
          <div className="text-center py-8 text-[#7A8065] text-sm">No recent transactions recorded.</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="ledger-table">
              <thead>
                <tr>
                  <th>DATE</th>
                  <th>DESCRIPTION</th>
                  <th>AMOUNT</th>
                  <th>AI CATEGORY</th>
                </tr>
              </thead>
              <tbody>
                {expenses.slice(0, 5).map((exp) => (
                  <tr key={exp.id}>
                    <td className="text-xs font-mono text-[#7A8065]">{exp.date.split(' ')[0]}</td>
                    <td className="font-medium text-[#242424]">{exp.description}</td>
                    <td className="font-bold text-[#1F4D3A]">₹{exp.amount.toLocaleString('en-IN')}</td>
                    <td>
                      <span className="inline-block px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wider bg-[#E8DDCB] text-[#1F4D3A] border border-[#D8CEBD]">
                        {exp.category}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
