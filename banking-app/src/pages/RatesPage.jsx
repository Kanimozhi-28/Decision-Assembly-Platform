import React from 'react';
import { Percent, TrendingUp, Calendar, AlertCircle } from 'lucide-react';

const RatesPage = () => {
    const depositRates = [
        { product: 'Smart Saver Savings', rate: '4.25%', min: '$100', note: 'Variable' },
        { product: '12-Month CD', rate: '5.10%', min: '$5,000', note: 'Fixed' },
        { product: '24-Month CD', rate: '4.85%', min: '$2,500', note: 'Fixed' },
        { product: 'Money Market+', rate: '3.75%', min: '$10,000', note: 'Variable' },
    ];

    const loanRates = [
        { product: '30-Year Fixed Mortgage', rate: '6.45%', apr: '6.52%', term: '360 Mo.' },
        { product: '15-Year Fixed Mortgage', rate: '5.85%', apr: '5.98%', term: '180 Mo.' },
        { product: 'Personal Loan', rate: '8.99%', apr: '9.24%', term: '60 Mo.' },
        { product: 'Auto Loan (New)', rate: '5.49%', apr: '5.62%', term: '48 Mo.' },
    ];

    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Current Rates</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Transparent and competitive rates updated daily. Locked-in value for your future.
                    </p>
                </div>

                <div className="space-y-12">
                    {/* Deposit Rates */}
                    <section className="bg-white rounded-3xl shadow-sm border border-slate-200 overflow-hidden">
                        <div className="bg-navy-950 px-8 py-6 text-white flex justify-between items-center">
                            <div className="flex items-center space-x-3">
                                <TrendingUp className="h-6 w-6 text-gold-500" />
                                <h2 className="text-xl font-bold italic">Deposit & Savings Rates</h2>
                            </div>
                            <span className="text-xs font-mono text-slate-400">Updated: Feb 16, 2026</span>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full text-left">
                                <thead className="bg-slate-50 border-b border-slate-200">
                                    <tr>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-center">APY</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Product</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Minimum</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Details</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-slate-100">
                                    {depositRates.map((row, idx) => (
                                        <tr key={idx} className="hover:bg-slate-50 transition-colors">
                                            <td className="px-8 py-6 text-center">
                                                <span className="text-3xl font-black text-primary-600">{row.rate}</span>
                                            </td>
                                            <td className="px-8 py-6 font-bold text-navy-950">{row.product}</td>
                                            <td className="px-8 py-6 text-slate-600 text-sm">{row.min}</td>
                                            <td className="px-8 py-6">
                                                <span className="px-3 py-1 rounded-full bg-slate-100 text-[10px] font-bold text-slate-500 uppercase">{row.note}</span>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </section>

                    {/* Loan Rates */}
                    <section className="bg-white rounded-3xl shadow-sm border border-slate-200 overflow-hidden">
                        <div className="bg-navy-950 px-8 py-6 text-white flex justify-between items-center">
                            <div className="flex items-center space-x-3">
                                <Percent className="h-6 w-6 text-gold-500" />
                                <h2 className="text-xl font-bold italic">Lending Rates</h2>
                            </div>
                            <span className="text-xs font-mono text-slate-400">Updated: Feb 16, 2026</span>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full text-left">
                                <thead className="bg-slate-50 border-b border-slate-200">
                                    <tr>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Product</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-center">Rate</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-center">APR</th>
                                        <th className="px-8 py-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-center">Term</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-slate-100">
                                    {loanRates.map((row, idx) => (
                                        <tr key={idx} className="hover:bg-slate-50 transition-colors">
                                            <td className="px-8 py-6 font-bold text-navy-950">{row.product}</td>
                                            <td className="px-8 py-6 text-center font-black text-primary-600 text-xl">{row.rate}</td>
                                            <td className="px-8 py-6 text-center font-bold text-slate-600">{row.apr}</td>
                                            <td className="px-8 py-6 text-center text-slate-400 text-sm font-mono">{row.term}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </section>

                    <div className="bg-amber-50 border-l-4 border-amber-500 p-6 rounded-r-2xl flex items-start space-x-4">
                        <AlertCircle className="h-6 w-6 text-amber-500 flex-shrink-0" />
                        <p className="text-sm text-amber-800 leading-relaxed">
                            <strong>Disclaimer:</strong> All rates are subject to modification without notice. Annual Percentage Yield (APY) and Annual Percentage Rate (APR) calculated based on standard credit profiles. Please contact an advisor for a personalized quote.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RatesPage;
