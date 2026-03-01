import React from 'react';
import { Landmark, Lock, ArrowRight, User, ShieldCheck } from 'lucide-react';
import { Link } from 'react-router-dom';

const LoginPage = () => {
    return (
        <div className="min-h-screen bg-navy-950 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
            <div className="absolute top-0 right-0 w-96 h-96 bg-primary-600/10 blur-[120px] rounded-full"></div>
            <div className="absolute bottom-0 left-0 w-96 h-96 bg-gold-400/10 blur-[120px] rounded-full"></div>

            <div className="max-w-md w-full space-y-8 relative z-10">
                <div className="text-center">
                    <Link to="/" className="inline-flex items-center space-x-2 text-white mb-8 group">
                        <Landmark className="h-10 w-10 text-gold-500 group-hover:scale-110 transition-transform" />
                        <span className="text-2xl font-bold tracking-tight">ApexBank</span>
                    </Link>
                    <h2 className="text-3xl font-extrabold text-white italic">Welcome Back</h2>
                    <p className="mt-2 text-sm text-slate-400">
                        Securely access your premium assets.
                    </p>
                </div>

                <div className="bg-white/5 backdrop-blur-xl border border-white/10 p-8 rounded-[2.5rem] shadow-2xl">
                    <form className="space-y-6">
                        <div className="space-y-2">
                            <label className="text-xs font-bold text-slate-400 uppercase tracking-widest ml-1">Username / ID</label>
                            <div className="relative">
                                <User className="absolute left-4 top-3.5 h-5 w-5 text-slate-500" />
                                <input
                                    type="text"
                                    className="w-full pl-12 pr-4 py-3.5 bg-navy-900/50 border border-white/10 rounded-2xl text-white outline-none focus:border-gold-500 transition-colors"
                                    placeholder="Enter your ID"
                                />
                            </div>
                        </div>

                        <div className="space-y-2">
                            <label className="text-xs font-bold text-slate-400 uppercase tracking-widest ml-1">Secure Password</label>
                            <div className="relative">
                                <Lock className="absolute left-4 top-3.5 h-5 w-5 text-slate-500" />
                                <input
                                    type="password"
                                    className="w-full pl-12 pr-4 py-3.5 bg-navy-900/50 border border-white/10 rounded-2xl text-white outline-none focus:border-gold-500 transition-colors"
                                    placeholder="••••••••"
                                />
                            </div>
                        </div>

                        <div className="flex items-center justify-between text-xs">
                            <div className="flex items-center text-slate-400">
                                <input type="checkbox" className="h-4 w-4 rounded border-white/10 bg-navy-900 accent-gold-500" />
                                <span className="ml-2">Remember ID</span>
                            </div>
                            <a href="#" className="text-gold-500 font-bold hover:underline tracking-tight">Forgot Password?</a>
                        </div>

                        <button className="w-full bg-gold-600 text-navy-950 py-4 rounded-2xl font-black text-lg hover:bg-gold-500 transition-all shadow-xl hover:-translate-y-1">
                            SECURE LOGIN
                        </button>
                    </form>

                    <div className="mt-8 pt-6 border-t border-white/10 text-center">
                        <div className="flex items-center justify-center space-x-2 text-[10px] text-slate-500 uppercase font-black tracking-[0.2em] mb-4">
                            <ShieldCheck className="h-4 w-4 text-emerald-500" />
                            <span>Encrypted Session</span>
                        </div>
                        <p className="text-sm text-slate-400">
                            New to ApexBank? <Link to="/accounts" className="text-white font-bold hover:text-gold-500 transition-colors underline decoration-gold-500 underline-offset-4">Open an account</Link>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;
