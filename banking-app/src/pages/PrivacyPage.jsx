import React from 'react';
import { Eye, Shield, Lock, FileText, Globe } from 'lucide-react';

const PrivacyPage = () => {
    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Privacy Policy</h1>
                    <p className="text-xl text-slate-600">
                        Transparent disclosure of how we protect and manage your data.
                    </p>
                </div>

                <div className="bg-white rounded-[2.5rem] p-12 shadow-sm border border-slate-200">
                    <div className="space-y-12">
                        <section>
                            <div className="flex items-center space-x-3 mb-6">
                                <Shield className="h-6 w-6 text-primary-600" />
                                <h2 className="text-2xl font-bold text-navy-950">Data Protection</h2>
                            </div>
                            <p className="text-slate-600 leading-relaxed">
                                At ApexBank, our commitment to your privacy is as strong as our commitment to your wealth. We employ military-grade encryption and strict internal protocols to ensure that your personal and financial information remains confidential.
                            </p>
                        </section>

                        <section>
                            <div className="flex items-center space-x-3 mb-6">
                                <Eye className="h-6 w-6 text-emerald-600" />
                                <h2 className="text-2xl font-bold text-navy-950">Information Collection</h2>
                            </div>
                            <p className="text-slate-600 leading-relaxed mb-4">
                                We only collect information that is strictly necessary to provide our premium banking services. This includes:
                            </p>
                            <ul className="list-disc pl-6 space-y-2 text-slate-600">
                                <li>Identity verification data (SSN, ID numbers)</li>
                                <li>Transaction history and balance information</li>
                                <li>Browsing context to improve your digital experience (DAP Integration)</li>
                            </ul>
                        </section>

                        <section>
                            <div className="flex items-center space-x-3 mb-6">
                                <Lock className="h-6 w-6 text-amber-600" />
                                <h2 className="text-2xl font-bold text-navy-950">Your Choices</h2>
                            </div>
                            <p className="text-slate-600 leading-relaxed">
                                You have total control over your data. You can request a full export of your data or deletion of non-essential records at any time through our security portal.
                            </p>
                        </section>

                        <section className="pt-8 border-t border-slate-100">
                            <div className="flex items-center justify-between text-xs font-bold text-slate-400 uppercase tracking-widest">
                                <div className="flex items-center space-x-2">
                                    <FileText className="h-4 w-4" />
                                    <span>Last Updated: February 2026</span>
                                </div>
                                <div className="flex items-center space-x-2">
                                    <Globe className="h-4 w-4" />
                                    <span>Global Standards Compliant</span>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default PrivacyPage;
