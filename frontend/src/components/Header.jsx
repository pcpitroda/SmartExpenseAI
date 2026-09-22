import React from 'react';
import { BookOpen, PlusCircle, Table, BarChart3, Info } from 'lucide-react';

export default function Header({ activeTab, setActiveTab }) {
  const navItems = [
    { id: 'overview', label: 'Overview', icon: BookOpen },
    { id: 'add', label: 'Add Expense', icon: PlusCircle },
    { id: 'transactions', label: 'Transactions', icon: Table },
    { id: 'insights', label: 'Insights', icon: BarChart3 },
    { id: 'about', label: 'About AI', icon: Info },
  ];

  return (
    <header className="border-b border-[#242424] bg-[#F6F1E8] sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-6 py-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
        {/* Brand */}
        <div>
          <h1 className="font-serif-heading text-2xl font-bold tracking-tight text-[#1F4D3A]">
            SMARTEXPENSE
          </h1>
          <p className="text-xs text-[#7A8065] font-medium tracking-wide uppercase">
            AI-powered expense journal
          </p>
        </div>

        {/* Horizontal Navigation */}
        <nav className="flex items-center gap-1 overflow-x-auto pb-1 md:pb-0">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium transition-all rounded-sm border ${
                  isActive
                    ? 'bg-[#1F4D3A] text-[#F6F1E8] border-[#1F4D3A]'
                    : 'text-[#242424] hover:bg-[#E8DDCB] border-transparent'
                }`}
              >
                <Icon className="w-4 h-4 opacity-80" />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>
      </div>
    </header>
  );
}
