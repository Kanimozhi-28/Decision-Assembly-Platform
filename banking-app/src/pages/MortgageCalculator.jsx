import React, { useState, useEffect } from 'react';
import { Calculator, DollarSign, Calendar, Percent, ArrowRight } from 'lucide-react';

const MortgageCalculator = () => {
    const [homePrice, setHomePrice] = useState(450000);
    const [downPayment, setDownPayment] = useState(90000);
    const [loamTerm, setLoanTerm] = useState(30);
    const [interestRate, setInterestRate] = useState(6.5);
    const [monthlyPayment, setMonthlyPayment] = useState(0);

    useEffect(() => {
        const principal = homePrice - downPayment;
        const calculatedInterest = interestRate / 100 / 12;
        const numberOfPayments = loamTerm * 12;

        const x = Math.pow(1 + calculatedInterest, numberOfPayments);
        const monthly = (principal * x * calculatedInterest) / (x - 1);

        if (isFinite(monthly)) {
            setMonthlyPayment(monthly.toFixed(2));
        }
    }, [homePrice, downPayment, loamTerm, interestRate]);

    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Mortgage Calculator</h1>
                    <p className="text-slate-600 max-w-2xl mx-auto text-lg">
                        Plan your future home with precision. Adjust the parameters below to see your estimated monthly commitments.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-200">
                    <div className="p-12 bg-slate-50 border-r border-slate-200">
                        <h2 className="text-2xl font-bold mb-10 flex items-center space-x-3 text-navy-950">
                            <Calculator className="h-6 w-6 text-gold-600" />
                            <span>Loan Parameters</span>
                        </h2>

                        <div className="space-y-8">
                            <div>
                                <div className="flex justify-between mb-4">
                                    <label className="text-sm font-bold text-slate-500 uppercase tracking-wider">Home Price</label>
                                    <span className="font-mono font-bold text-primary-600">${homePrice.toLocaleString()}</span>
                                </div>
                                <input
                                    type="range" min="100000" max="2000000" step="10000"
                                    value={homePrice} onChange={(e) => setHomePrice(Number(e.target.value))}
                                    className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600"
                                />
                            </div>

                            <div>
                                <div className="flex justify-between mb-4">
                                    <label className="text-sm font-bold text-slate-500 uppercase tracking-wider">Down Payment</label>
                                    <span className="font-mono font-bold text-primary-600">${downPayment.toLocaleString()}</span>
                                </div>
                                <input
                                    type="range" min="0" max={homePrice} step="5000"
                                    value={downPayment} onChange={(e) => setDownPayment(Number(e.target.value))}
                                    className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary-600"
                                />
                            </div>

                            <div className="grid grid-cols-2 gap-8">
                                <div>
                                    <label className="block text-sm font-bold text-slate-500 uppercase tracking-wider mb-4">Interest Rate (%)</label>
                                    <div className="relative">
                                        <Percent className="absolute left-3 top-3.5 h-4 w-4 text-slate-400" />
                                        <input
                                            type="number" step="0.1"
                                            value={interestRate} onChange={(e) => setInterestRate(Number(e.target.value))}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 outline-none font-bold"
                                        />
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-sm font-bold text-slate-500 uppercase tracking-wider mb-4">Loan Term (Years)</label>
                                    <div className="relative">
                                        <Calendar className="absolute left-3 top-3.5 h-4 w-4 text-slate-400" />
                                        <select
                                            value={loamTerm} onChange={(e) => setLoanTerm(Number(e.target.value))}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 outline-none font-bold appearance-none bg-white"
                                        >
                                            <option value={15}>15 Years</option>
                                            <option value={20}>20 Years</option>
                                            <option value={30}>30 Years</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="p-12 flex flex-col justify-center items-center text-center bg-navy-950 text-white relative">
                        <div className="absolute top-0 right-0 w-32 h-32 bg-primary-500/10 blur-3xl"></div>
                        <div className="absolute bottom-0 left-0 w-32 h-32 bg-gold-400/10 blur-3xl"></div>

                        <h3 className="text-slate-400 text-sm font-bold uppercase tracking-[0.3em] mb-4">Estimated Monthly Payment</h3>
                        <div className="flex items-start justify-center mb-8">
                            <span className="text-3xl font-bold text-gold-500 mr-1 mt-2">$</span>
                            <span className="text-7xl font-black text-white tracking-tighter">{monthlyPayment.split('.')[0]}</span>
                            <span className="text-2xl font-bold text-slate-400 mt-2">.{monthlyPayment.split('.')[1]}</span>
                        </div>

                        <div className="w-full h-px bg-white/10 my-10"></div>

                        <p className="text-slate-400 text-sm italic mb-10 max-w-sm">
                            *This estimate includes principal and interest only. Actual payments will vary based on taxes, insurance, and individual credit profile.
                        </p>

                        <button className="w-full bg-gold-500 text-navy-950 py-5 rounded-2xl font-black text-lg hover:bg-gold-400 transition-all shadow-xl flex items-center justify-center space-x-3 group">
                            <span>GET PRE-APPROVED NOW</span>
                            <ArrowRight className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
                        </button>
                    </div>
                </div>

                {/* Informational Section - Target for Just Exploring */}
                <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div className="p-8 bg-white rounded-2xl border border-slate-100 shadow-sm">
                        <h4 className="font-bold text-navy-950 mb-4 flex items-center space-x-2">
                            <ShieldCheck className="h-5 w-5 text-emerald-500" />
                            <span>Locked Rates</span>
                        </h4>
                        <p className="text-slate-500 text-sm">Lock your rate for up to 90 days while you shop for your dream home.</p>
                    </div>
                    <div className="p-8 bg-white rounded-2xl border border-slate-100 shadow-sm">
                        <h4 className="font-bold text-navy-950 mb-4 flex items-center space-x-2">
                            <Globe className="h-5 w-5 text-primary-500" />
                            <span>Digital Closing</span>
                        </h4>
                        <p className="text-slate-500 text-sm">Minimize paperwork with our secure digital closing portal available anywhere.</p>
                    </div>
                    <div className="p-8 bg-white rounded-2xl border border-slate-100 shadow-sm">
                        <h4 className="font-bold text-navy-950 mb-4 flex items-center space-x-2">
                            <DollarSign className="h-5 w-5 text-gold-600" />
                            <span>Zero Down Options</span>
                        </h4>
                        <p className="text-slate-500 text-sm">Qualified first-time buyers may be eligible for specialty low-down-payment programs.</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

// Internal icon helper to fix Landmark/Globe import issues
function ShieldCheck(props) {
    return (
        <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10" /><path d="m9 12 2 2 4-4" /></svg>
    );
}

function Globe(props) {
    return (
        <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10" /><line x1="2" y1="12" x2="22" y2="12" /><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" /></svg>
    );
}

export default MortgageCalculator;
