import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Landmark, Menu, X, ChevronDown, Search, User } from 'lucide-react';

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);

    const navLinks = [
        { name: 'Accounts', path: '/accounts' },
        { name: 'Cards', path: '/cards' },
        { name: 'Loans', path: '/loans' },
        { name: 'Rates', path: '/rates' },
        { name: 'About', path: '/about' },
    ];

    return (
        <nav className="bg-navy-950 text-white sticky top-0 z-50 shadow-2xl border-b border-navy-800">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-20">
                    <div className="flex items-center">
                        <Link to="/" className="flex items-center space-x-2 group">
                            <Landmark className="h-8 w-8 text-gold-500 group-hover:scale-110 transition-transform" />
                            <span className="text-xl font-bold tracking-tight text-white">
                                Apex<span className="text-gold-500 underline decoration-2 underline-offset-4">Bank</span>
                            </span>
                        </Link>
                        <div className="hidden md:ml-10 md:flex md:space-x-8">
                            {navLinks.map((link) => (
                                <Link
                                    key={link.name}
                                    to={link.path}
                                    className="text-slate-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1"
                                >
                                    <span>{link.name}</span>
                                    <ChevronDown className="h-3 w-3" />
                                </Link>
                            ))}
                        </div>
                    </div>
                    <div className="hidden md:flex items-center space-x-6">
                        <button className="text-slate-300 hover:text-white">
                            <Search className="h-5 w-5" />
                        </button>
                        <Link
                            to="/login"
                            className="flex items-center space-x-2 bg-navy-800 hover:bg-navy-700 px-4 py-2 rounded-lg border border-navy-700 transition-colors"
                        >
                            <User className="h-4 w-4 text-gold-500" />
                            <span className="text-sm font-semibold">Online Banking</span>
                        </Link>
                    </div>
                    <div className="md:hidden flex items-center">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="inline-flex items-center justify-center p-2 rounded-md text-slate-400 hover:text-white hover:bg-navy-800 focus:outline-none"
                        >
                            {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {isOpen && (
                <div className="md:hidden bg-navy-900 border-t border-navy-800 animate-in slide-in-from-top duration-300">
                    <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                        {navLinks.map((link) => (
                            <Link
                                key={link.name}
                                to={link.path}
                                className="text-slate-300 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
                                onClick={() => setIsOpen(false)}
                            >
                                {link.name}
                            </Link>
                        ))}
                        <Link
                            to="/login"
                            className="block w-full text-center bg-gold-600 hover:bg-gold-700 text-navy-950 px-4 py-3 rounded-lg font-bold mt-4 transition-colors"
                            onClick={() => setIsOpen(false)}
                        >
                            Online Banking Login
                        </Link>
                    </div>
                </div>
            )}
        </nav>
    );
};

export default Navbar;
