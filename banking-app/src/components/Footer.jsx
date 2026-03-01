import React from 'react';
import { Landmark, Facebook, Twitter, Instagram, Linkedin } from 'lucide-react';

const Footer = () => {
    return (
        <footer className="bg-navy-950 text-slate-400 py-16 border-t border-navy-800">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 md:grid-cols-4 gap-12">
                    <div className="col-span-1 md:col-span-1">
                        <div className="flex items-center space-x-2 text-white mb-6">
                            <Landmark className="h-8 w-8 text-gold-500" />
                            <span className="text-xl font-bold tracking-tight">ApexBank</span>
                        </div>
                        <p className="text-sm leading-relaxed">
                            Empowering your financial journey with state-of-the-art security and premium services. Established 1922.
                        </p>
                        <div className="flex space-x-4 mt-6">
                            <Facebook className="h-5 w-5 hover:text-gold-500 cursor-pointer transition-colors" />
                            <Twitter className="h-5 w-5 hover:text-gold-500 cursor-pointer transition-colors" />
                            <Instagram className="h-5 w-5 hover:text-gold-500 cursor-pointer transition-colors" />
                            <Linkedin className="h-5 w-5 hover:text-gold-500 cursor-pointer transition-colors" />
                        </div>
                    </div>

                    <div>
                        <h3 className="text-white font-bold mb-6 italic border-l-4 border-gold-500 pl-3">Products</h3>
                        <ul className="space-y-4 text-sm">
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Checking Accounts</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Savings & CDs</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Credit Cards</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Personal Loans</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Mortgages</a></li>
                        </ul>
                    </div>

                    <div>
                        <h3 className="text-white font-bold mb-6 italic border-l-4 border-gold-500 pl-3">Support</h3>
                        <ul className="space-y-4 text-sm">
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Help Center</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Contact Us</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Find a Branch</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Report Fraud</a></li>
                            <li><a href="#" className="hover:text-gold-500 transition-colors">Privacy Policy</a></li>
                        </ul>
                    </div>

                    <div>
                        <h3 className="text-white font-bold mb-6 italic border-l-4 border-gold-500 pl-3">Newsletter</h3>
                        <p className="text-sm mb-4">Get the latest financial insights delivered to your inbox.</p>
                        <div className="flex">
                            <input
                                type="email"
                                placeholder="Email address"
                                className="bg-navy-900 border border-navy-700 rounded-l-lg px-4 py-2 w-full focus:outline-none focus:border-gold-500"
                            />
                            <button className="bg-gold-600 text-navy-950 px-4 py-2 rounded-r-lg font-bold hover:bg-gold-700 transition-colors">
                                Go
                            </button>
                        </div>
                    </div>
                </div>
                <div className="mt-16 pt-8 border-t border-navy-800 text-xs text-center">
                    <p>© 2026 Apex Financial Group. Member FDIC. Equal Housing Lender.</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
