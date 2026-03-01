import React from 'react';
import { Link } from 'react-router-dom';
import { CreditCard, Plane, Banknote, GraduationCap, ChevronRight, CheckCircle2 } from 'lucide-react';

const cards = [
    {
        id: 'travel-platinum',
        name: 'Apex Travel Platinum',
        icon: Plane,
        color: 'bg-blue-600',
        tag: 'Popular',
        benefits: ['5x points on flights', 'Airport Lounge Access', 'No Foreign Fees'],
        fees: '$450 Annual Fee',
        apr: '18.99% - 25.99%',
        cta: 'View Details'
    },
    {
        id: 'daily-cashback',
        name: 'Apex Daily Cashback',
        icon: Banknote,
        color: 'bg-emerald-600',
        tag: 'Best Value',
        benefits: ['3% on Groceries', '1% on all other', 'No Annual Fee'],
        fees: '$0 Annual Fee',
        apr: '15.99% - 22.99%',
        cta: 'View Details'
    },
    {
        id: 'student-learner',
        name: 'Apex Student Learner',
        icon: GraduationCap,
        color: 'bg-indigo-600',
        tag: 'Entry Level',
        benefits: ['Credit Score Monitoring', 'Good Grade Rewards', 'Zero Liability'],
        fees: '$0 Annual Fee',
        apr: '14.99% Fixed',
        cta: 'View Details'
    }
];

const CardsPage = () => {
    return (
        <div className="py-20 bg-slate-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8">Credit Cards</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Find the card that matches your lifestyle. From travel enthusiasts to students, we have you covered.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {cards.map((card) => (
                        <div key={card.id} className="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-200 hover:border-primary-500 transition-all group flex flex-col">
                            <div className={`${card.color} p-8 text-white relative`}>
                                {card.tag && (
                                    <span className="absolute top-4 right-4 bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider">
                                        {card.tag}
                                    </span>
                                )}
                                <card.icon className="h-12 w-12 mb-6 group-hover:scale-110 transition-transform" />
                                <h3 className="text-2xl font-bold">{card.name}</h3>
                            </div>

                            <div className="p-8 flex-grow">
                                <ul className="space-y-4 mb-8">
                                    {card.benefits.map((benefit, idx) => (
                                        <li key={idx} className="flex items-start space-x-3 text-sm text-slate-600">
                                            <CheckCircle2 className="h-5 w-5 text-emerald-500 flex-shrink-0" />
                                            <span>{benefit}</span>
                                        </li>
                                    ))}
                                </ul>
                                <div className="pt-6 border-t border-slate-100 mt-auto">
                                    <div className="flex justify-between text-xs font-bold text-slate-400 uppercase mb-4">
                                        <span>{card.fees}</span>
                                        <span>{card.apr} APR</span>
                                    </div>
                                    <Link
                                        to={`/cards/${card.id}`}
                                        className="w-full flex items-center justify-center space-x-2 bg-navy-950 text-white py-3 rounded-lg font-bold hover:bg-navy-800 transition-colors"
                                    >
                                        <span>{card.cta}</span>
                                        <ChevronRight className="h-4 w-4" />
                                    </Link>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                {/* Comparison Table Section Preview - Target for DAP */}
                <div className="mt-24 p-12 bg-navy-950 rounded-3xl text-white relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-64 h-64 bg-gold-400/10 blur-[100px] rounded-full"></div>
                    <div className="relative z-10 flex flex-col md:flex-row items-center justify-between">
                        <div className="mb-8 md:mb-0">
                            <h2 className="text-3xl font-bold mb-4 italic">Still undecided?</h2>
                            <p className="text-slate-400 max-w-md">Compare all rates, benefits, and insurance coverage side-by-side to find your perfect match.</p>
                        </div>
                        <button className="bg-gold-500 text-navy-950 px-10 py-4 rounded-xl font-bold hover:bg-gold-400 transition-all flex items-center space-x-2">
                            <span>Compare All Cards</span>
                            <ChevronRight className="h-5 w-5" />
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CardsPage;
