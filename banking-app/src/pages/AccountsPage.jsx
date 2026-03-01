import React from 'react';
import { PiggyBank, Briefcase, Landmark, CheckCircle2, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

const accounts = [
    {
        category: 'Checking',
        icon: Landmark,
        description: 'Everyday banking made simple and secure.',
        products: [
            { id: 'apex-classic', name: 'Apex Classic', feature: 'No monthly fee with direct deposit', min: '$0' },
            { id: 'apex-silver', name: 'Apex Silver', feature: 'Earn 0.15% APY on balances', min: '$1,500' },
            { id: 'apex-platinum', name: 'Apex Platinum', feature: 'Unlimited ATM fee rebated globally', min: '$25,000' }
        ]
    },
    {
        category: 'Savings',
        icon: PiggyBank,
        description: 'High-yield solutions to grow your wealth.',
        products: [
            { id: 'smart-saver', name: 'Smart Saver', feature: '4.25% APY with auto-save', min: '$100' },
            { id: 'wealth-builder-cd', name: 'Wealth Builder CD', feature: '5.10% APY for 12 months', min: '$5,000' },
            { id: 'money-market-plus', name: 'Money Market+', feature: 'Tiered rates based on balance', min: '$10,000' }
        ]
    }
];

const AccountsPage = () => {
    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Accounts & Deposits</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Choose the perfect home for your money. Whether you need daily flexibility or long-term growth, we have the account for you.
                    </p>
                </div>

                <div className="space-y-16">
                    {accounts.map((group) => (
                        <div key={group.category}>
                            <div className="flex items-center space-x-4 mb-8">
                                <div className="w-12 h-12 bg-primary-600 rounded-xl flex items-center justify-center text-white shadow-lg">
                                    <group.icon className="h-6 w-6" />
                                </div>
                                <div>
                                    <h2 className="text-3xl font-bold text-navy-950">{group.category}</h2>
                                    <p className="text-slate-500">{group.description}</p>
                                </div>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                                {group.products.map((product) => (
                                    <div key={product.name} className="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm hover:shadow-xl transition-all group border-b-4 hover:border-b-gold-500">
                                        <h3 className="text-xl font-bold text-navy-950 mb-4">{product.name}</h3>
                                        <div className="flex items-center space-x-3 text-sm text-slate-600 mb-6 bg-slate-50 p-3 rounded-lg">
                                            <CheckCircle2 className="h-4 w-4 text-emerald-500" />
                                            <span>{product.feature}</span>
                                        </div>
                                        <div className="flex justify-between items-center mt-6 pt-6 border-t border-slate-100">
                                            <div>
                                                <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest">Min. to Open</p>
                                                <p className="text-lg font-bold text-navy-950">{product.min}</p>
                                            </div>
                                            <Link
                                                to={`/accounts/${product.id}`}
                                                className="h-10 w-10 rounded-full border border-slate-200 flex items-center justify-center group-hover:bg-primary-600 group-hover:text-white group-hover:border-primary-600 transition-all font-bold text-xl"
                                            >
                                                <ArrowRight className="h-5 w-5" />
                                            </Link>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>

                {/* Wealth Management Promo */}
                <div className="mt-24 p-12 bg-gradient-to-br from-navy-900 to-navy-950 rounded-3xl text-white flex flex-col items-center text-center">
                    <Briefcase className="h-12 w-12 text-gold-500 mb-6" />
                    <h2 className="text-3xl font-bold mb-4 italic">Private Wealth Management</h2>
                    <p className="text-slate-400 max-w-2xl mb-8">
                        For individuals with assets exceeding $250k. Experience bespoke financial planning, exclusive investment access, and dedicated private bankers.
                    </p>
                    <button className="bg-white text-navy-950 px-8 py-3 rounded-xl font-bold hover:bg-gold-500 hover:text-navy-950 transition-all">
                        Schedule a Consultation
                    </button>
                </div>
            </div>
        </div>
    );
};

export default AccountsPage;
