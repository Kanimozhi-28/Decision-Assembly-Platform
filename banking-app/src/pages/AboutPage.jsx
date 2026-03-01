import React from 'react';
import { Landmark, Users, Award, ShieldCheck, ArrowRight } from 'lucide-react';

const AboutPage = () => {
    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-20">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Our Heritage</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        A century of financial excellence, built on trust, innovation, and an unwavering commitment to our members.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-24">
                    <div className="relative">
                        <div className="bg-navy-950 rounded-[3rem] p-12 text-white relative z-10 overflow-hidden">
                            <div className="absolute top-0 right-0 w-32 h-32 bg-gold-400/20 blur-3xl"></div>
                            <h2 className="text-3xl font-bold mb-6 italic">The Apex Promise</h2>
                            <p className="text-slate-400 leading-relaxed mb-6">
                                Founded in 1922 during a time of immense global shift, ApexBank was established with a singular vision: to provide a stable, premium financial foundation for those building the future.
                            </p>
                            <p className="text-slate-400 leading-relaxed">
                                Today, we serve over 5 million members globally, managing assets with the same integrity and forward-thinking approach that defined us a hundred years ago.
                            </p>
                        </div>
                        <div className="absolute -bottom-6 -right-6 w-full h-full border-2 border-slate-200 rounded-[3rem] -z-0"></div>
                    </div>

                    <div className="grid grid-cols-2 gap-8">
                        <div className="p-8 bg-white rounded-3xl border border-slate-200 shadow-sm text-center">
                            <Users className="h-10 w-10 text-primary-600 mx-auto mb-4" />
                            <h4 className="text-2xl font-black text-navy-950">5M+</h4>
                            <p className="text-xs text-slate-500 uppercase font-bold tracking-widest mt-2">Active Members</p>
                        </div>
                        <div className="p-8 bg-white rounded-3xl border border-slate-200 shadow-sm text-center">
                            <Landmark className="h-10 w-10 text-gold-600 mx-auto mb-4" />
                            <h4 className="text-2xl font-black text-navy-950">500+</h4>
                            <p className="text-xs text-slate-500 uppercase font-bold tracking-widest mt-2">Global Branches</p>
                        </div>
                        <div className="p-8 bg-white rounded-3xl border border-slate-200 shadow-sm text-center">
                            <Award className="h-10 w-10 text-emerald-600 mx-auto mb-4" />
                            <h4 className="text-2xl font-black text-navy-950">A+</h4>
                            <p className="text-xs text-slate-500 uppercase font-bold tracking-widest mt-2">Credit Rating</p>
                        </div>
                        <div className="p-8 bg-white rounded-3xl border border-slate-200 shadow-sm text-center">
                            <ShieldCheck className="h-10 w-10 text-indigo-600 mx-auto mb-4" />
                            <h4 className="text-2xl font-black text-navy-950">100</h4>
                            <p className="text-xs text-slate-500 uppercase font-bold tracking-widest mt-2">Years of Service</p>
                        </div>
                    </div>
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-sm border border-slate-100 flex flex-col md:flex-row items-center justify-between">
                    <div className="mb-8 md:mb-0 max-w-xl">
                        <h3 className="text-2xl font-bold text-navy-950 mb-4 italic">Work with us</h3>
                        <p className="text-slate-600">We are always looking for visionary talent to join our global banking team.</p>
                    </div>
                    <button className="flex items-center space-x-2 bg-navy-950 text-white px-8 py-4 rounded-2xl font-bold hover:bg-gold-500 hover:text-navy-950 transition-all">
                        <span>View Openings</span>
                        <ArrowRight className="h-5 w-5" />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default AboutPage;
