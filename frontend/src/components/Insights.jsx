import React from 'react';
import { BarChart2, TrendingUp, DollarSign, Layers } from 'lucide-react';

export default function Insights({ summary }) {
  const totalSpending = summary?.total_spending || 0;
  const totalTransactions = summary?.total_transactions || 0;
  const avgTransaction = summary?.avg_transaction || 0;
  const topCategory = summary?.top_category || 'N/A';
  const categoryBreakdown = summary?.category_breakdown || [];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="border-b border-[#D8CEBD] pb-4">
        <h2 className="font-serif-heading text-4xl text-[#242424]">Your spending, decoded.</h2>
        <p className="text-[#7A8065] text-sm mt-1">
          Financial patterns and AI-segmented budget metrics.
        </p>
      </div>

      {/* Metric Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="paper-card p-5">
          <div className="text-xs font-semibold text-[#7A8065] uppercase">Average Transaction</div>
          <div className="font-serif-heading text-2xl font-bold text-[#1F4D3A] mt-2">
            ₹{avgTransaction.toLocaleString('en-IN')}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Per transaction avg</div>
        </div>

        <div className="paper-card p-5">
          <div className="text-xs font-semibold text-[#7A8065] uppercase">Total Expenditure</div>
          <div className="font-serif-heading text-2xl font-bold text-[#242424] mt-2">
            ₹{totalSpending.toLocaleString('en-IN')}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Overall journal spend</div>
        </div>

        <div className="paper-card p-5">
          <div className="text-xs font-semibold text-[#7A8065] uppercase">Most Frequent Category</div>
          <div className="font-serif-heading text-2xl font-bold text-[#C96B4B] mt-2">
            {topCategory}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Highest frequency</div>
        </div>

        <div className="paper-card p-5">
          <div className="text-xs font-semibold text-[#7A8065] uppercase">Logged Entries</div>
          <div className="font-serif-heading text-2xl font-bold text-[#7A8065] mt-2">
            {totalTransactions}
          </div>
          <div className="text-xs text-[#7A8065] mt-1">Total items</div>
        </div>
      </div>

      {/* Editorial Category Distribution Chart */}
      <div className="paper-card p-6 space-y-6">
        <div className="border-b border-[#D8CEBD] pb-4 flex items-center justify-between">
          <h3 className="font-serif-heading text-2xl text-[#242424]">Category Distribution</h3>
          <span className="text-xs font-mono uppercase text-[#7A8065]">Visual Ledger View</span>
        </div>

        {categoryBreakdown.length === 0 ? (
          <div className="text-center py-12 text-[#7A8065]">No category data available yet.</div>
        ) : (
          <div className="space-y-6">
            {categoryBreakdown.map((cat, idx) => {
              const share = totalSpending > 0 ? ((cat.total / totalSpending) * 100).toFixed(1) : 0;
              const barColors = ['#1F4D3A', '#C96B4B', '#7A8065', '#5C6B73', '#9E5A47', '#3D5A50', '#8C857B'];
              const color = barColors[idx % barColors.length];

              return (
                <div key={cat.category} className="space-y-2">
                  <div className="flex items-center justify-between text-sm">
                    <div className="flex items-center gap-2">
                      <span
                        className="w-3 h-3 inline-block border border-[#242424]"
                        style={{ backgroundColor: color }}
                      />
                      <span className="font-serif-heading font-bold text-[#242424] text-base">
                        {cat.category}
                      </span>
                      <span className="text-xs font-mono text-[#7A8065]">({cat.count} items)</span>
                    </div>
                    <div className="font-mono text-sm">
                      <span className="font-bold text-[#1F4D3A] mr-2">₹{cat.total.toLocaleString('en-IN')}</span>
                      <span className="text-[#7A8065]">({share}%)</span>
                    </div>
                  </div>

                  <div className="w-full bg-[#E8DDCB] h-4 border border-[#D8CEBD] overflow-hidden">
                    <div
                      className="h-full bar-fill"
                      style={{
                        width: `${share}%`,
                        backgroundColor: color
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
