import React, { useState } from 'react';
import { Search, ChevronDown, ChevronUp, HelpCircle } from 'lucide-react';

const FAQPage = () => {
    const [search, setSearch] = useState('');
    const [openItems, setOpenItems] = useState([0]);

    const toggle = (idx) => {
        setOpenItems(prev => prev.includes(idx) ? prev.filter(i => i !== idx) : [...prev, idx]);
    };

    const faqs = [
        {
            q: 'How do I open a new checking account?',
            a: 'You can open an account online in less than 5 minutes. Select your preferred account type from the Accounts page and click "Apply Now". You will need your SSN and a valid ID.'
        },
        {
            q: 'What is the current mortgage interest rate?',
            a: 'Rates vary based on loan type and credit history. You can view our current daily market rates on the Rates page or use our Mortgage Calculator for a personalized estimate.'
        },
        {
            q: 'How does the credit card rewards program work?',
            a: 'Rewards are earned on every purchase. For example, our Travel Platinum card earns 5x miles on flights, while Daily Cashback gives you 3% back on groceries. Miles never expire.'
        },
        {
            q: 'Is my money FDIC insured?',
            a: 'Yes, ApexBank is a member of the FDIC. Your deposits are insured up to at least $250,000 per depositor, per ownership category.'
        },
        {
            q: 'Can I lock my card if I lose it?',
            a: 'Absolutely. Use the Security page or our mobile app to instantly "Freeze" your card. This blocks all new transactions while allowing scheduled payments to processed.'
        }
    ];

    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Help Center</h1>
                    <p className="text-xl text-slate-600">
                        Find answers to common questions about your ApexBank experience.
                    </p>
                </div>

                <div className="relative mb-12">
                    <Search className="absolute left-4 top-4 h-6 w-6 text-slate-400" />
                    <input
                        type="text"
                        placeholder="Search for a topic (e.g. 'closing an account')"
                        className="w-full pl-14 pr-6 py-4 rounded-2xl border border-slate-200 shadow-sm focus:border-primary-500 focus:ring-1 focus:ring-primary-500 outline-none text-lg transition-all"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                </div>

                <div className="space-y-4">
                    {faqs.map((faq, idx) => (
                        <div key={idx} className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition-shadow">
                            <button
                                onClick={() => toggle(idx)}
                                className="w-full px-8 py-6 flex justify-between items-center text-left hover:bg-slate-50 transition-colors"
                            >
                                <span className="text-lg font-bold text-navy-950">{faq.q}</span>
                                {openItems.includes(idx) ? <ChevronUp className="h-5 w-5 text-gold-600" /> : <ChevronDown className="h-5 w-5 text-slate-400" />}
                            </button>
                            {openItems.includes(idx) && (
                                <div className="px-8 pb-8 text-slate-600 leading-relaxed border-t border-slate-50 pt-4">
                                    {faq.a}
                                </div>
                            )}
                        </div>
                    ))}
                </div>

                <div className="mt-20 p-10 bg-primary-600 rounded-3xl text-white flex flex-col md:flex-row items-center justify-between shadow-2xl">
                    <div className="flex items-center space-x-4 mb-6 md:mb-0 text-center md:text-left">
                        <HelpCircle className="h-10 w-10 text-gold-400" />
                        <div>
                            <h3 className="text-xl font-bold">Still have questions?</h3>
                            <p className="text-primary-100">Our support team is available 24/7 via live chat or phone.</p>
                        </div>
                    </div>
                    <button className="bg-white text-primary-600 px-8 py-3 rounded-xl font-bold hover:bg-gold-500 hover:text-navy-950 transition-all">
                        Contact Support
                    </button>
                </div>
            </div>
        </div>
    );
};

export default FAQPage;
