import React, { useEffect } from 'react';
import { Home, User, Car, ArrowRight, CheckCircle2 } from 'lucide-react';
import { Link } from 'react-router-dom';

const loanTypes = [
    {
        title: 'Home Loans',
        icon: Home,
        desc: 'Competitive rates and flexible terms for your dream home.',
        items: ['30-Year Fixed', '15-Year Fixed', 'ARM Options', 'VA & FHA'],
        cta: 'View Mortgage Options',
        link: '/loans/home'
    },
    {
        title: 'Personal Loans',
        icon: User,
        desc: 'Consolidate debt or fund major life events with ease.',
        items: ['Fixed Monthly Payments', 'No Collateral Required', 'Rapid Funding', 'Low Interest'],
        cta: 'View Personal Loans',
        link: '/loans/personal'
    },
    {
        title: 'Auto Loans',
        icon: Car,
        desc: 'Get behind the wheel faster with our rapid approval process.',
        items: ['New & Used Vehicles', 'Refinancing Options', 'Flexible Terms', 'Competitive APR'],
        cta: 'View Auto Deals',
        link: '/loans/auto'
    }
];

const LoansPage = () => {
    useEffect(() => {
        document.title = "Lending Solutions | ApexBank";
    }, []);

    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Financing Solutions</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Transparent lending for your biggest milestones. Simple applications, fast approvals, and human support.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {loanTypes.map((loan) => (
                        <div key={loan.title} className="bg-white rounded-3xl p-8 shadow-sm border border-slate-200 flex flex-col hover:shadow-2xl transition-all">
                            <div className="w-16 h-16 bg-navy-950 rounded-2xl flex items-center justify-center text-gold-500 mb-8">
                                <loan.icon className="h-8 w-8" />
                            </div>
                            <h3 className="text-2xl font-bold text-navy-950 mb-4">{loan.title}</h3>
                            <p className="text-slate-500 mb-8 text-sm leading-relaxed">{loan.desc}</p>

                            <ul className="space-y-4 mb-10 flex-grow">
                                {loan.items.map((item) => (
                                    <li key={item} className="flex items-center space-x-3 text-sm font-medium text-slate-700">
                                        <CheckCircle2 className="h-4 w-4 text-emerald-500" />
                                        <span>{item}</span>
                                    </li>
                                ))}
                            </ul>

                            <Link
                                to={loan.link}
                                className="w-full bg-slate-100 text-navy-950 py-4 rounded-xl font-bold flex items-center justify-center space-x-2 border border-slate-200 hover:bg-gold-500 transition-colors"
                            >
                                <span>{loan.cta}</span>
                                <ArrowRight className="h-4 w-4" />
                            </Link>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default LoansPage;
