import React from 'react';
import { ShieldCheck, Zap, Globe, ArrowRight, CreditCard, PiggyBank, Briefcase } from 'lucide-react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div className="bg-slate-50">
            {/* Hero Section */}
            <section className="relative bg-navy-950 text-white overflow-hidden py-24 px-4 sm:px-6 lg:px-8">
                <div className="absolute inset-0 opacity-10">
                    <div className="absolute top-0 -left-1/4 w-1/2 h-full bg-gold-400 blur-3xl rounded-full"></div>
                    <div className="absolute bottom-0 -right-1/4 w-1/2 h-full bg-primary-500 blur-3xl rounded-full"></div>
                </div>

                <div className="relative max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    <div>
                        <span className="inline-block bg-navy-800 text-gold-500 px-4 py-1 rounded-full text-xs font-bold uppercase tracking-widest mb-6">
                            Next-Gen Banking
                        </span>
                        <h1 className="text-5xl md:text-7xl font-extrabold leading-tight mb-6">
                            Redefining <br />
                            <span className="text-transparent bg-clip-text bg-gradient-to-r from-gold-400 to-primary-400">
                                Financial Luxury
                            </span>
                        </h1>
                        <p className="text-xl text-slate-300 mb-10 max-w-lg leading-relaxed">
                            Experience personalized banking solutions designed for your lifestyle.
                            Join 5 million members who trust ApexBank for their future.
                        </p>
                        <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                            <Link to="/accounts" className="btn-primary text-center">
                                Open an Account
                            </Link>
                            <Link to="/cards" className="bg-white/10 hover:bg-white/20 text-white px-6 py-3 rounded-lg font-semibold backdrop-blur-md transition-all text-center border border-white/20">
                                Explore Cards
                            </Link>
                        </div>
                    </div>
                    <div className="hidden lg:block relative">
                        <div className="bg-gradient-to-tr from-navy-900 to-navy-800 p-8 rounded-3xl border border-white/10 shadow-2xl transform hover:rotate-2 transition-transform duration-500">
                            <div className="flex justify-between items-start mb-12">
                                <Landmark className="h-10 w-10 text-gold-500" />
                                <div className="text-right">
                                    <p className="text-xs text-slate-400 uppercase tracking-tighter">Current Balance</p>
                                    <p className="text-3xl font-mono font-bold text-white">$42,910.00</p>
                                </div>
                            </div>
                            <div className="space-y-4">
                                {[1, 2, 3].map((i) => (
                                    <div key={i} className="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/5">
                                        <div className="flex items-center space-x-3">
                                            <div className="w-10 h-10 rounded-lg bg-navy-700 flex items-center justify-center">
                                                <Zap className="h-5 w-5 text-gold-500" />
                                            </div>
                                            <div>
                                                <p className="text-sm font-semibold">Wealth Optimizer</p>
                                                <p className="text-xs text-slate-400">Investment Strategy</p>
                                            </div>
                                        </div>
                                        <p className="text-sm font-bold text-emerald-400">+$120.00</p>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Trust Bar */}
            <section className="bg-white py-12 border-b border-slate-200">
                <div className="max-w-7xl mx-auto px-4 flex flex-wrap justify-between items-center opacity-50 contrast-125">
                    <span className="font-black text-2xl text-slate-800">FORBES</span>
                    <span className="font-black text-2xl text-slate-800">REUTERS</span>
                    <span className="font-black text-2xl text-slate-800">FINTECH INSIDER</span>
                    <span className="font-black text-2xl text-slate-800">WALL STREET</span>
                    <span className="font-black text-2xl text-slate-800">MODERN BANKER</span>
                </div>
            </section>

            {/* Quick Access Grid - Multi-intent Target */}
            <section className="dap-trigger-section">
                <div className="text-center mb-16">
                    <h2 className="text-3xl font-bold text-navy-950 mb-4 italic underline decoration-gold-500 underline-offset-8">Tailored for You</h2>
                    <p className="text-slate-600 max-w-2xl mx-auto">Different needs, one premium solution. Select your path to financial freedom.</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div className="card group">
                        <div className="w-14 h-14 bg-blue-50 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-primary-600 transition-colors">
                            <CreditCard className="h-7 w-7 text-primary-600 group-hover:text-white" />
                        </div>
                        <h3 className="text-xl font-bold mb-4">Cards & Rewards</h3>
                        <p className="text-slate-600 text-sm mb-6">Earn up to 4% miles on global travel and 2% on daily essential spending.</p>
                        <Link to="/cards" className="text-primary-600 font-bold flex items-center space-x-2 text-sm">
                            <span>Compare cards</span>
                            <ArrowRight className="h-4 w-4" />
                        </Link>
                    </div>

                    <div className="card group">
                        <div className="w-14 h-14 bg-amber-50 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-gold-500 transition-colors">
                            <PiggyBank className="h-7 w-7 text-gold-600 group-hover:text-white" />
                        </div>
                        <h3 className="text-xl font-bold mb-4">Smart Savings</h3>
                        <p className="text-slate-600 text-sm mb-6">High-yield accounts that grow your wealth automatically at market-leading rates.</p>
                        <Link to="/accounts" className="text-primary-600 font-bold flex items-center space-x-2 text-sm">
                            <span>Explore yields</span>
                            <ArrowRight className="h-4 w-4" />
                        </Link>
                    </div>

                    <div className="card group">
                        <div className="w-14 h-14 bg-indigo-50 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-indigo-600 transition-colors">
                            <Briefcase className="h-7 w-7 text-indigo-600 group-hover:text-white" />
                        </div>
                        <h3 className="text-xl font-bold mb-4">Wealth Management</h3>
                        <p className="text-slate-600 text-sm mb-6">Expert advisory services for portfolios exceeding $250,000 in assets.</p>
                        <Link to="/about" className="text-primary-600 font-bold flex items-center space-x-2 text-sm">
                            <span>View solutions</span>
                            <ArrowRight className="h-4 w-4" />
                        </Link>
                    </div>
                </div>
            </section>

            {/* Featured CTA - Hesitation Target */}
            <section className="bg-primary-900 py-24 relative overflow-hidden">
                <div className="max-w-4xl mx-auto px-4 text-center relative z-10 text-white">
                    <h2 className="text-4xl font-extrabold mb-8 italic">Ready to make the switch?</h2>
                    <p className="text-slate-300 text-lg mb-12">
                        Joining ApexBank takes less than 5 minutes. No paperwork, no hidden fees, just pure banking.
                    </p>
                    <div className="flex justify-center space-x-4">
                        <button className="bg-gold-500 text-navy-950 px-8 py-4 rounded-xl font-bold hover:bg-gold-400 transition-all shadow-xl hover:-translate-y-1">
                            Start Application
                        </button>
                    </div>
                </div>
            </section>
        </div>
    );
};

// Internal icon helper to fix Landmark import in the hero example
function Landmark(props) {
    return (
        <svg
            {...props}
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
        >
            <line x1="3" y1="22" x2="21" y2="22" />
            <line x1="6" y1="18" x2="6" y2="11" />
            <line x1="10" y1="18" x2="10" y2="11" />
            <line x1="14" y1="18" x2="14" y2="11" />
            <line x1="18" y1="18" x2="18" y2="11" />
            <polygon points="12 2 20 7 4 7 12 2" />
        </svg>
    );
}

export default HomePage;
