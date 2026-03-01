import React, { useEffect } from 'react';
import { User, CheckCircle2, ShieldCheck, Zap } from 'lucide-react';

const PersonalLoanPage = () => {
    useEffect(() => {
        document.title = "Personal Loans | ApexBank";
    }, []);

    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 bg-white rounded-3xl p-12 shadow-sm border border-slate-200">
                <div className="flex items-center space-x-4 mb-8">
                    <div className="w-16 h-16 bg-navy-950 rounded-2xl flex items-center justify-center text-gold-500">
                        <User className="h-8 w-8" />
                    </div>
                    <div>
                        <h1 className="text-3xl font-extrabold text-navy-950 uppercase tracking-tight">Apex Personal Loan</h1>
                        <p className="text-gold-600 font-bold uppercase tracking-widest text-xs">Flexible Consumer Financing</p>
                    </div>
                </div>

                <div className="prose prose-slate max-w-none mb-12">
                    <p className="text-lg text-slate-600 leading-relaxed font-medium">
                        Consolidate high-interest debt, fund a major life event, or cover unexpected expenses with a fixed-rate personal loan from ApexBank. Enjoy rapid funding and transparent terms without the need for collateral.
                    </p>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">8.99%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">Standard Fixed APR</span>
                        </div>
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">7.49%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">Premier Fixed APR</span>
                        </div>
                    </div>

                    <h2 className="text-2xl font-bold text-navy-950 mb-6">Why Choose Apex Personal Loans?</h2>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-4 list-none p-0">
                        <li className="flex items-center space-x-3 text-slate-700">
                            <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                            <span>No collateral or home equity needed</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <Zap className="h-5 w-5 text-emerald-500" />
                            <span>Funds in as little as 24 hours</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <ShieldCheck className="h-5 w-5 text-emerald-500" />
                            <span>No application or origination fees</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                            <span>Fixed monthly payments for easy budgeting</span>
                        </li>
                    </ul>
                </div>

                <div className="mt-12 p-8 bg-navy-950 rounded-2xl text-center">
                    <h3 className="text-xl font-bold text-white mb-4">Ready to start?</h3>
                    <p className="text-slate-400 mb-8 max-w-md mx-auto">Check your rate in less than 2 minutes without affecting your credit score.</p>
                    <button className="bg-gold-500 text-navy-950 px-8 py-4 rounded-xl font-bold hover:bg-gold-400 transition-colors">
                        CHECK MY RATE
                    </button>
                </div>
            </div>
        </div>
    );
};

export default PersonalLoanPage;
