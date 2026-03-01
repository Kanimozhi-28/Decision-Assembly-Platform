import React, { useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ShieldCheck, Gift, Globe, CheckCircle2, Award, ArrowLeft, CreditCard as CardIcon } from 'lucide-react';

const cardData = {
    'travel-platinum': {
        name: 'Apex Travel Platinum',
        description: 'The ultimate companion for the global explorer. Earn massive rewards on every mile and enjoy premium luxury at every stop.',
        price: '$450 Annual Fee',
        apr: '18.99% Variable',
        eligibility: 'Excellent credit history required',
        features: ['5X points on flights and hotels', 'Complimentary airport lounge access', ' $200 annual travel credit', 'No foreign transaction fees'],
        longDesc: 'The Apex Travel Platinum card is designed for those who demand more from their travel experience. With comprehensive travel insurance and a suite of global lifestyle benefits, it is more than a card—it is your passport to the world.',
        color: 'from-blue-700 to-blue-900',
        icon: Globe
    },
    'daily-cashback': {
        name: 'Apex Daily Cashback',
        description: 'Transform your every day into rewards. Get cash back on the things you buy most, from groceries to gas.',
        price: '$0 Annual Fee',
        apr: '15.99% Variable',
        eligibility: 'Good to Excellent credit',
        features: ['3% back on Groceries & Dining', '2% back on Gas & EV charging', '1% back on everything else', 'Unlimited cashback that never expires'],
        longDesc: 'Why wait for points? The Apex Daily Cashback card gives you real money for your real life. No categories to track or sign up for—just consistent value on every swipe.',
        color: 'from-emerald-600 to-emerald-800',
        icon: Gift
    },
    'student-learner': {
        name: 'Apex Student Learner',
        description: 'Start your financial journey on the right foot. Build credit responsibly while earning rewards for good grades.',
        price: '$0 Annual Fee',
        apr: '14.99% Fixed',
        eligibility: 'Verified student status',
        features: ['$20 Statement Credit for GPA > 3.0', 'No late fee on first payment', 'Credit limit increase after 6 months', 'Zero Liability Protection'],
        longDesc: 'The Apex Student Learner card is the perfect tool for building a solid financial foundation. We provide the tools and education to help you understand your credit while rewarding your academic success.',
        color: 'from-indigo-600 to-indigo-800',
        icon: Award
    }
};

const CardDetailsPage = () => {
    const { id } = useParams();
    const card = cardData[id];

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [id]);

    if (!card) {
        return (
            <div className="py-20 text-center">
                <h1 className="text-2xl font-bold">Card not found</h1>
                <Link to="/cards" className="text-primary-600 underline">Back to cards</Link>
            </div>
        );
    }

    return (
        <div className="bg-white">
            {/* Header Splash */}
            <div className={`bg-gradient-to-r ${card.color} text-white py-24 px-4`}>
                <div className="max-w-7xl mx-auto flex flex-col items-center text-center">
                    <Link to="/cards" className="flex items-center space-x-2 text-white/70 hover:text-white mb-8 transition-colors self-start">
                        <ArrowLeft className="h-4 w-4" />
                        <span>All Cards</span>
                    </Link>
                    <card.icon className="h-20 w-20 mb-8 opacity-90" />
                    <h1 className="text-4xl md:text-6xl font-black mb-6">{card.name}</h1>
                    <p className="text-xl text-white/80 max-w-2xl">{card.description}</p>
                </div>
            </div>

            {/* Main Content */}
            <div className="max-w-7xl mx-auto px-4 py-20">
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-16">
                    <div className="lg:col-span-2">
                        <h2 className="text-3xl font-bold text-navy-950 mb-8 italic border-b-2 border-gold-500 pb-4 inline-block">Key Benefits</h2>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
                            {card.features.map((feature, idx) => (
                                <div key={idx} className="flex space-x-4 p-6 bg-slate-50 rounded-2xl border border-slate-100 hover:shadow-md transition-shadow">
                                    <div className="w-10 h-10 rounded-full bg-white flex items-center justify-center shadow-sm flex-shrink-0">
                                        <CheckCircle2 className="h-6 w-6 text-emerald-500" />
                                    </div>
                                    <p className="text-slate-700 font-medium leading-tight pt-1">{feature}</p>
                                </div>
                            ))}
                        </div>

                        <h2 className="text-3xl font-bold text-navy-950 mb-8 italic">Product Overview</h2>
                        <p className="text-lg text-slate-600 leading-relaxed mb-8">
                            {card.longDesc}
                        </p>
                        <div className="p-8 bg-navy-950 text-white rounded-3xl">
                            <div className="flex items-center space-x-4 mb-6">
                                <ShieldCheck className="h-8 w-8 text-gold-500" />
                                <h3 className="text-xl font-bold">Safe & Secure</h3>
                            </div>
                            <p className="text-slate-400 text-sm">
                                Every ApexBank card comes with 24/7 fraud monitoring, zero-liability protection, and the ability to lock your card instantly from our mobile app.
                            </p>
                        </div>
                    </div>

                    <div className="lg:col-span-1">
                        <div className="sticky top-32 bg-slate-50 border border-slate-200 rounded-3xl p-8 shadow-2xl">
                            <h3 className="text-xl font-bold text-navy-950 mb-8 italic">Quick Specs</h3>
                            <div className="space-y-6 mb-10">
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Annual Fee</span>
                                    <span className="font-bold text-navy-950 uppercase">{card.price}</span>
                                </div>
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Purchase APR</span>
                                    <span className="font-bold text-navy-950">{card.apr}</span>
                                </div>
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Credit Needed</span>
                                    <span className="font-bold text-navy-950">{card.eligibility}</span>
                                </div>
                            </div>

                            {/* Main CTA - DAP Hover Target */}
                            <button className="w-full bg-primary-600 text-white py-5 rounded-xl font-black text-lg hover:bg-primary-700 transition-all shadow-xl hover:-translate-y-1 active:scale-95 mb-4">
                                APPLY NOW
                            </button>
                            <p className="text-[10px] text-slate-400 text-center leading-tight">
                                Subject to credit approval. Terms and conditions apply. See full Cardmember Agreement for details.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CardDetailsPage;
