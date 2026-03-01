import React, { useEffect } from 'react';
import { Home, CheckCircle2, ShieldCheck, Clock } from 'lucide-react';

const HomeLoanPage = () => {
    useEffect(() => {
        document.title = "Apex Home Mortgage | ApexBank";
    }, []);

    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 bg-white rounded-3xl p-12 shadow-sm border border-slate-200">
                <div className="flex items-center space-x-4 mb-8">
                    <div className="w-16 h-16 bg-navy-950 rounded-2xl flex items-center justify-center text-gold-500">
                        <Home className="h-8 w-8" />
                    </div>
                    <div>
                        <h1 className="text-3xl font-extrabold text-navy-950 uppercase tracking-tight">Apex Home Mortgage</h1>
                        <p className="text-gold-600 font-bold uppercase tracking-widest text-xs">Real Estate Financing</p>
                    </div>
                </div>

                <div className="prose prose-slate max-w-none mb-12">
                    <p className="text-lg text-slate-600 leading-relaxed font-medium">
                        Secure your dream home with ApexBank's industry-leading mortgage solutions. From first-time homebuyers to seasoned investors, our flexible terms and competitive rates make home ownership reachable.
                    </p>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">6.45%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">30-Year Fixed APR</span>
                        </div>
                        <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 text-center">
                            <span className="block text-4xl font-black text-navy-950 mb-2">5.85%</span>
                            <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">15-Year Fixed APR</span>
                        </div>
                    </div>

                    <h2 className="text-2xl font-bold text-navy-950 mb-6">Why Apex Home Loans?</h2>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-4 list-none p-0">
                        <li className="flex items-center space-x-3 text-slate-700">
                            <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                            <span>No early payoff penalties</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <ShieldCheck className="h-5 w-5 text-emerald-500" />
                            <span>Locked-in rates for 90 days</span>
                        </li>
                        <li className="flex items-center space-x-3 text-slate-700">
                            <Clock className="h-5 w-5 text-emerald-500" />
                            <span>15-day average closing time</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default HomeLoanPage;
