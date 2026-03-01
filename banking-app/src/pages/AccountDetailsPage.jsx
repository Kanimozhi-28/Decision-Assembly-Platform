import React, { useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ShieldCheck, CheckCircle2, ArrowLeft, Landmark, Star, Trophy, Wallet, PiggyBank } from 'lucide-react';

const accountData = {
    'apex-classic': {
        name: 'Apex Classic Checking',
        description: 'The essential banking solution for your everyday needs. Simple, transparent, and completely free with direct deposit.',
        fee: '$0 Monthly Fee',
        apy: '0.00% APY',
        minOpen: '$0',
        features: [
            'Free with $250+ monthly direct deposit',
            'Over 55,000 fee-free Allpoint® ATMs',
            'Early paycheck access (up to 2 days)',
            'Apex Mobile App suite access'
        ],
        longDesc: 'Apex Classic is designed for those who want straightforward banking without the hidden costs. It provides all the digital tools you need to manage your money on the go, backed by our world-class security infrastructure.',
        color: 'from-slate-700 to-slate-900',
        icon: Wallet
    },
    'apex-silver': {
        name: 'Apex Silver Checking',
        description: 'The perfect balance of liquidity and growth. Earn interest on your daily balance while enjoying expanded benefits.',
        fee: '$12 Monthly Fee',
        apy: '0.15% APY',
        minOpen: '$1,500',
        features: [
            'Fee waived with $1,500 average balance',
            'Interest earned on every dollar',
            '2 Out-of-network ATM rebates monthly',
            'Free personalized standard checks'
        ],
        longDesc: 'Apex Silver is for individuals who maintain a healthy balance and want their money to work harder. With a competitive APY for a checking account and added flexibility for ATM usage, it is the ideal upgrade for your primary banking.',
        color: 'from-silver-500 to-slate-400',
        icon: Star
    },
    'apex-platinum': {
        name: 'Apex Platinum Checking',
        description: 'Our most prestigious checking experience. Exclusive rates, global flexibility, and a dedicated banking team at your service.',
        fee: '$25 Monthly Fee',
        apy: '0.45% APY',
        minOpen: '$25,000',
        features: [
            'Fee waived with $25,000+ total relationship',
            'Unlimited global ATM fee rebates',
            'Dedicated Private Banking representative',
            'Highest interest rate on checking'
        ],
        longDesc: 'The Apex Platinum account is the pinnacle of our retail banking offer. Designed for high-net-worth individuals, it offers unparalleled global access and a personal touch that ensures your complex financial needs are always met.',
        color: 'from-navy-800 to-navy-950',
        icon: Trophy
    },
    'smart-saver': {
        name: 'Smart Saver',
        description: 'Watch your savings soar with our industry-leading high-yield account. Perfect for your emergency fund or long-term goals.',
        fee: '$0 Monthly Fee',
        apy: '4.25% APY',
        minOpen: '$100',
        features: [
            'No monthly maintenance fees',
            'Automatic savings tools and round-ups',
            'Mobile check deposit and easy transfers',
            'No minimum balance after opening'
        ],
        longDesc: 'The Smart Saver account is built for those who value both growth and accessibility. With an APY that significantly outperforms the national average and no monthly fees, it\'s the smartest way to build your financial cushion.',
        color: 'from-emerald-600 to-emerald-800',
        icon: PiggyBank
    },
    'wealth-builder-cd': {
        name: 'Wealth Builder CD',
        description: 'Lock in a guaranteed high rate with our 12-month Certificate of Deposit. Secure growth for your idle cash.',
        fee: 'Early Withdrawal Penalty Applies',
        apy: '5.10% APY',
        minOpen: '$5,000',
        features: [
            'Guaranteed fixed return for 12 months',
            'FDIC insured up to $250,000',
            'Interest compounded daily',
            'Automatic renewal options'
        ],
        longDesc: 'The Wealth Builder CD offers stability in a changing market. By committing your funds for a year, you lock in a premium interest rate that provides reliable, predictable growth for your portfolio.',
        color: 'from-amber-600 to-amber-800',
        icon: Landmark
    },
    'money-market-plus': {
        name: 'Money Market+',
        description: 'Combine the high yield of a savings account with the flexibility of a checking account. Premier rates for premier balances.',
        fee: '$15 Monthly Fee',
        apy: 'Up to 4.50% APY',
        minOpen: '$10,000',
        features: [
            'Tiered interest rates (higher balances earn more)',
            'Limited check-writing capabilities',
            'Fee waived with $10,000 average balance',
            'Instant access to funds'
        ],
        longDesc: 'Money Market+ is designed for clients who want the best of both worlds: high-performance yields and the ability to access their money when they need it most. It\'s the perfect home for large cash reserves.',
        color: 'from-purple-700 to-purple-900',
        icon: Star
    }
};

const AccountDetailsPage = () => {
    const { id } = useParams();
    const account = accountData[id];

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [id]);

    if (!account) {
        return (
            <div className="py-20 text-center">
                <h1 className="text-2xl font-bold">Account not found</h1>
                <Link to="/accounts" className="text-primary-600 underline">Back to accounts</Link>
            </div>
        );
    }

    return (
        <div className="bg-white">
            {/* Header Splash */}
            <div className={`bg-gradient-to-r ${account.color} text-white py-24 px-4`}>
                <div className="max-w-7xl mx-auto flex flex-col items-center text-center">
                    <Link to="/accounts" className="flex items-center space-x-2 text-white/70 hover:text-white mb-8 transition-colors self-start">
                        <ArrowLeft className="h-4 w-4" />
                        <span>All Accounts</span>
                    </Link>
                    <account.icon className="h-20 w-20 mb-8 text-gold-500 opacity-90" />
                    <h1 className="text-4xl md:text-6xl font-black mb-6 uppercase tracking-tight">{account.name}</h1>
                    <p className="text-xl text-white/80 max-w-2xl">{account.description}</p>
                </div>
            </div>

            {/* Main Content */}
            <div className="max-w-7xl mx-auto px-4 py-20">
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-16">
                    <div className="lg:col-span-2">
                        <h2 className="text-3xl font-bold text-navy-950 mb-8 italic border-b-2 border-gold-500 pb-4 inline-block">Account Benefits</h2>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
                            {account.features.map((feature, idx) => (
                                <div key={idx} className="flex space-x-4 p-6 bg-slate-50 rounded-2xl border border-slate-100 hover:shadow-md transition-shadow">
                                    <div className="w-10 h-10 rounded-full bg-white flex items-center justify-center shadow-sm flex-shrink-0">
                                        <CheckCircle2 className="h-6 w-6 text-emerald-500" />
                                    </div>
                                    <p className="text-slate-700 font-medium leading-tight pt-1">{feature}</p>
                                </div>
                            ))}
                        </div>

                        <h2 className="text-3xl font-bold text-navy-950 mb-8 italic">At a Glance</h2>
                        <p className="text-lg text-slate-600 leading-relaxed mb-8">
                            {account.longDesc}
                        </p>
                        <div className="p-8 bg-navy-950 text-white rounded-3xl">
                            <div className="flex items-center space-x-4 mb-6">
                                <ShieldCheck className="h-8 w-8 text-gold-500" />
                                <h3 className="text-xl font-bold">Apex Security Guarantee</h3>
                            </div>
                            <p className="text-slate-400 text-sm">
                                Your peace of mind is our priority. Every Apex account includes multi-factor authentication, biometric login, and FDIC insurance up to $250,000.
                            </p>
                        </div>
                    </div>

                    <div className="lg:col-span-1">
                        <div className="sticky top-32 bg-slate-50 border border-slate-200 rounded-3xl p-8 shadow-2xl">
                            <h3 className="text-xl font-bold text-navy-950 mb-8 italic">Account Details</h3>
                            <div className="space-y-6 mb-10">
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Service Fee</span>
                                    <span className="font-bold text-navy-950 uppercase">{account.fee}</span>
                                </div>
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Yield (APY)</span>
                                    <span className="font-bold text-navy-950">{account.apy}</span>
                                </div>
                                <div className="flex justify-between items-center text-sm border-b border-slate-200 pb-4">
                                    <span className="text-slate-500">Min. to Open</span>
                                    <span className="font-bold text-navy-950">{account.minOpen}</span>
                                </div>
                            </div>

                            <button className="w-full bg-primary-600 text-white py-5 rounded-xl font-black text-lg hover:bg-primary-700 transition-all shadow-xl hover:-translate-y-1 active:scale-95 mb-4">
                                OPEN ACCOUNT
                            </button>
                            <p className="text-[10px] text-slate-400 text-center leading-tight">
                                Terms and conditions apply. Overdraft protection available. ApexBank N.A. Member FDIC.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AccountDetailsPage;
