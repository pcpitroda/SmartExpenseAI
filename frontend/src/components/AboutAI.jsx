import React from 'react';
import { Cpu, FileText, Settings, Layers, CheckCircle } from 'lucide-react';

export default function AboutAI() {
  const steps = [
    { label: 'Expense Description', icon: FileText, desc: 'User inputs plain text, e.g. "Pizza at restaurant"' },
    { label: 'Text Processing', icon: Settings, desc: 'Lowercasing, punctuation stripping, token normalization' },
    { label: 'TF-IDF Vectorizer', icon: Layers, desc: 'Extracts unigram & bigram word frequency weights' },
    { label: 'Lightweight ML Model', icon: Cpu, desc: 'Logistic Regression predicts category probabilities' },
    { label: 'Expense Category', icon: CheckCircle, desc: 'Assigned label, confidence %, and ledger storage' }
  ];

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      {/* Header */}
      <div className="border-b border-[#D8CEBD] pb-4">
        <h2 className="font-serif-heading text-4xl text-[#242424]">Behind the classification</h2>
        <p className="text-[#7A8065] text-sm mt-1">
          Understanding the machine learning methodology powering SmartExpense AI.
        </p>
      </div>

      {/* Main explanation text card */}
      <div className="paper-card p-6 space-y-4">
        <h3 className="font-serif-heading text-2xl text-[#1F4D3A]">
          How SmartExpense AI Works
        </h3>
        <p className="text-[#242424] text-base leading-relaxed">
          SmartExpense AI uses <strong>TF-IDF (Term Frequency-Inverse Document Frequency)</strong> text features combined with a lightweight <strong>Logistic Regression model</strong> to analyze raw transaction descriptions and infer their appropriate category.
        </p>
        <p className="text-[#7A8065] text-sm leading-relaxed">
          Unlike heavy neural networks that require massive GPUs, this Tiny AI prototype relies on a compact model trained on structured financial transaction keywords. It executes in milliseconds with minimal CPU memory overhead.
        </p>
      </div>

      {/* Minimal Monochrome Flow Diagram */}
      <div className="paper-card p-8 space-y-6">
        <div className="text-xs font-bold uppercase tracking-widest text-[#7A8065] text-center border-b border-[#D8CEBD] pb-3">
          TINY AI PIPELINE ARCHITECTURE
        </div>

        <div className="flex flex-col md:flex-row items-center justify-between gap-4 py-4">
          {steps.map((step, idx) => {
            const Icon = step.icon;
            return (
              <React.Fragment key={step.label}>
                <div className="flex-1 bg-[#F6F1E8] border border-[#242424] p-4 text-center space-y-2 w-full md:w-auto">
                  <div className="w-8 h-8 mx-auto bg-[#242424] text-[#F6F1E8] rounded-none flex items-center justify-center font-bold text-xs">
                    0{idx + 1}
                  </div>
                  <div className="font-serif-heading font-bold text-[#242424] text-sm">
                    {step.label}
                  </div>
                  <div className="text-xs text-[#7A8065] leading-tight">
                    {step.desc}
                  </div>
                </div>

                {idx < steps.length - 1 && (
                  <div className="hidden md:block text-[#1F4D3A] font-bold text-lg">
                    →
                  </div>
                )}
              </React.Fragment>
            );
          })}
        </div>
      </div>

      {/* Model Spec Box */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="paper-card p-5 space-y-2">
          <div className="text-xs font-bold text-[#7A8065] uppercase">FEATURE EXTRACTION</div>
          <div className="font-serif-heading text-lg font-bold text-[#242424]">TF-IDF N-Grams</div>
          <p className="text-xs text-[#7A8065]">
            Converts text phrases into numerical term frequency vectors incorporating 1-gram and 2-gram word pairs.
          </p>
        </div>

        <div className="paper-card p-5 space-y-2">
          <div className="text-xs font-bold text-[#7A8065] uppercase">CLASSIFICATION ALGORITHM</div>
          <div className="font-serif-heading text-lg font-bold text-[#1F4D3A]">Logistic Regression</div>
          <p className="text-xs text-[#7A8065]">
            Multi-class classification trained with L-BFGS solver, providing calibrated confidence probabilities for every prediction.
          </p>
        </div>
      </div>
    </div>
  );
}
