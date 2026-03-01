import React, { useEffect } from 'react';
import { Car, CheckCircle2, TrendingDown, Zap } from 'lucide-react';

const AutoLoanPage = () => {
    useEffect(() => {
        document.title = "Apex Auto Financing | ApexBank";
    }, []);

    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 bg-white rounded-3xl p-12 shadow-sm border border-slate-200">
                <div className="flex items-center space-x-4 mb-8">
                    <div className="w-16 h-16 bg-navy-950 rounded-2xl flex items-center justify-center text-gold-500">
                        <Car className="h-8 w-8" />
                    </div>
                    <div>
                        <h1 className="text-3xl font-extrabold text-navy-950 uppercase tracking-tight">Apex Auto Financing</h1>
                        <p className="text-gold-600 font-bold uppercase tracking-widest text-xs">Vehicle Loans</p>
                    </div>
                </div>

                <div className="prose prose-slate max-w-none mb-12">
                    <p className="text-lg text-slate-600 leading-relaxed font-medium">
                        Get behind the wheel of your next vehicle with confidence. ApexBank offers rapid-approval auto loans for new and used cars, with flexible repayment terms designed to fit your budget.
                    </p>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">5.49%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">New Car APR</span>
                        </div>
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">6.25%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">Used Car APR</span>
                        </div>
                    </div>

                    <h2 className="text-2xl font-bold text-navy-950 mb-6">Loan Features</h2>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-4 list-none p-0">
                        <li className="flex items-center space-x-3 text-slate-700">
                            <Zap className="h-5 w-5 text-emerald-500" />
                            <span>Instant decision within 60 seconds</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <TrendingDown className="h-5 w-5 text-emerald-500" />
                            <span>Special rates for EV purchases</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                            <span>Repayment terms up to 84 months</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default AutoLoanPage;
