import React from 'react';
import { ShieldCheck, Lock, Fingerprint, EyeOff, AlertTriangle, ShieldAlert } from 'lucide-react';

const SecurityPage = () => {
    const securityFeatures = [
        {
            title: 'Biometric Authentication',
            icon: Fingerprint,
            desc: 'Access your accounts using secure fingerprint or facial recognition on supported devices.'
        },
        {
            title: '256-bit Encryption',
            icon: Lock,
            desc: 'All data transmitted between your browser and our servers is protected by industry-leading encryption.'
        },
        {
            title: 'Fraud Monitoring',
            icon: ShieldAlert,
            desc: 'Our AI systems monitor your accounts 24/7 for suspicious activity and alert you instantly.'
        },
        {
            title: 'Privacy Protection',
            icon: EyeOff,
            desc: 'We never sell your data to third parties. Your financial life remains your business.'
        }
    ];

    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Security & Privacy</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Your peace of mind is our highest priority. Learn about the multi-layered defense systems protecting your wealth.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-12 mb-20">
                    {securityFeatures.map((feature) => (
                        <div key={feature.title} className="bg-white p-10 rounded-3xl shadow-sm border border-slate-200 flex space-x-6 hover:shadow-xl transition-all">
                            <div className="w-16 h-16 bg-primary-50 rounded-2xl flex items-center justify-center text-primary-600 flex-shrink-0">
                                <feature.icon className="h-8 w-8" />
                            </div>
                            <div>
                                <h3 className="text-xl font-bold text-navy-950 mb-4">{feature.title}</h3>
                                <p className="text-slate-500 leading-relaxed">{feature.desc}</p>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="bg-navy-950 rounded-[3rem] p-12 md:p-20 text-white relative overflow-hidden">
                    <div className="absolute top-0 left-0 w-full h-full opacity-10">
                        <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                                    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" strokeWidth="1" />
                                </pattern>
                            </defs>
                            <rect width="100%" height="100%" fill="url(#grid)" />
                        </svg>
                    </div>
                    <div className="relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                        <div>
                            <h2 className="text-4xl font-bold mb-8 italic">Apex Security Pro</h2>
                            <p className="text-slate-400 text-lg mb-8">
                                Go beyond standard protection. Apex Security Pro provides identity theft insurance, dark web monitoring, and dedicated fraud recovery specialists for all Platinum members.
                            </p>
                            <div className="flex space-x-4">
                                <div className="flex items-center space-x-2 bg-white/10 px-4 py-2 rounded-lg border border-white/10">
                                    <ShieldCheck className="h-5 w-5 text-gold-500" />
                                    <span className="text-sm font-bold">$1M Insurance</span>
                                </div>
                                <div className="flex items-center space-x-2 bg-white/10 px-4 py-2 rounded-lg border border-white/10">
                                    <ShieldCheck className="h-5 w-5 text-gold-500" />
                                    <span className="text-sm font-bold">24/7 Response</span>
                                </div>
                            </div>
                        </div>
                        <div className="bg-white/5 border border-white/10 p-10 rounded-3xl backdrop-blur-md">
                            <div className="flex items-center space-x-3 mb-8 text-amber-500">
                                <AlertTriangle className="h-6 w-6" />
                                <h3 className="text-lg font-bold">Security Alert</h3>
                            </div>
                            <p className="text-sm text-slate-300 mb-6 font-mono leading-relaxed">
                                Suspicious login attempt detected from unknown device in Singapore.
                                <br />Location: IP 172.67.143.2
                                <br />Status: BLOCKED
                            </p>
                            <button className="w-full bg-gold-500 text-navy-950 py-4 rounded-xl font-bold hover:bg-gold-400 transition-colors">
                                Verify My Identity
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SecurityPage;
