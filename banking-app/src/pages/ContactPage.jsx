import React from 'react';
import { Phone, Mail, MapPin, MessageSquare, Clock, Globe } from 'lucide-react';

const ContactPage = () => {
    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Get in Touch</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        We are here to help you 24/7. Choose the most convenient way to reach our expert advisors.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
                    {/* Contact Methods */}
                    <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl transition-shadow">
                            <div className="w-12 h-12 bg-primary-100 rounded-xl flex items-center justify-center text-primary-600 mb-6">
                                <Phone className="h-6 w-6" />
                            </div>
                            <h3 className="text-xl font-bold text-navy-950 mb-2">Phone Support</h3>
                            <p className="text-slate-500 text-sm mb-4">Dedicated lines for personal and business banking.</p>
                            <p className="text-primary-600 font-black text-lg">1-800-APEX-BANK</p>
                        </div>

                        <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl transition-shadow">
                            <div className="w-12 h-12 bg-emerald-100 rounded-xl flex items-center justify-center text-emerald-600 mb-6">
                                <MessageSquare className="h-6 w-6" />
                            </div>
                            <h3 className="text-xl font-bold text-navy-950 mb-2">Live Chat</h3>
                            <p className="text-slate-500 text-sm mb-4">Chat with a representative instantly through our app or web portal.</p>
                            <button className="text-emerald-600 font-black text-lg hover:underline">Start Chat Now</button>
                        </div>

                        <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl transition-shadow">
                            <div className="w-12 h-12 bg-amber-100 rounded-xl flex items-center justify-center text-amber-600 mb-6">
                                <Mail className="h-6 w-6" />
                            </div>
                            <h3 className="text-xl font-bold text-navy-950 mb-2">Email Inquiry</h3>
                            <p className="text-slate-500 text-sm mb-4">For non-urgent inquiries, send us a message and we'll reply within 24 hours.</p>
                            <p className="text-amber-600 font-black text-lg">support@apexbank.com</p>
                        </div>

                        <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl transition-shadow">
                            <div className="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center text-indigo-600 mb-6">
                                <MapPin className="h-6 w-6" />
                            </div>
                            <h3 className="text-xl font-bold text-navy-950 mb-2">Find a Branch</h3>
                            <p className="text-slate-500 text-sm mb-4">Visit any of our 500+ premium lounge branches across the country.</p>
                            <button className="text-indigo-600 font-black text-lg hover:underline">Locate Branch</button>
                        </div>
                    </div>

                    {/* Quick Info Sidebar */}
                    <div className="lg:col-span-1 space-y-8">
                        <div className="bg-navy-950 text-white p-10 rounded-[2.5rem] shadow-2xl">
                            <h3 className="text-xl font-bold mb-8 italic border-l-4 border-gold-500 pl-4">Operating Hours</h3>
                            <div className="space-y-6">
                                <div className="flex items-center space-x-4">
                                    <Clock className="h-5 w-5 text-gold-500" />
                                    <div>
                                        <p className="text-xs text-slate-400 uppercase font-bold tracking-widest">Digital Banking</p>
                                        <p className="text-sm font-bold">24 / 7 / 365</p>
                                    </div>
                                </div>
                                <div className="flex items-center space-x-4">
                                    <Globe className="h-5 w-5 text-gold-500" />
                                    <div>
                                        <p className="text-xs text-slate-400 uppercase font-bold tracking-widest">Branch Access</p>
                                        <p className="text-sm font-bold">Mon - Sat: 9am - 8pm</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-white p-10 rounded-[2.5rem] border border-slate-200 shadow-sm text-center">
                            <h3 className="text-lg font-bold text-navy-950 mb-4">Emergency Support</h3>
                            <p className="text-sm text-slate-500 mb-8 leading-relaxed">
                                Lost your card or suspect fraud? Call our emergency line immediately.
                            </p>
                            <button className="w-full bg-red-600 text-white py-4 rounded-xl font-black text-lg hover:bg-red-700 transition-colors shadow-lg">
                                REPORT FRAUD
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ContactPage;
