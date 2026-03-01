import React from 'react';
import { Briefcase, MapPin, Search, ArrowRight, Star, Globe, Sparkles } from 'lucide-react';

const CareersPage = () => {
    const jobs = [
        { title: 'Senior Private Banker', location: 'New York, NY', type: 'Full-time', dept: 'Wealth Management' },
        { title: 'FinTech Software Engineer', location: 'Austin, TX', type: 'Remote', dept: 'Digital Banking' },
        { title: 'Security Architect', location: 'Chicago, IL', type: 'Full-time', dept: 'Risk & Strategy' },
        { title: 'Customer Success Advocate', location: 'London, UK', type: 'Hybrid', dept: 'Support' },
    ];

    return (
        <div className="py-20 bg-slate-50 min-h-screen">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h1 className="text-4xl md:text-5xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase">Join the Elite</h1>
                    <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                        Shape the future of global finance. We are looking for innovators, thinkers, and builders to redefine banking.
                    </p>
                </div>

                {/* Search Bar */}
                <div className="bg-white p-4 rounded-2xl shadow-sm border border-slate-200 mb-16 flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
                    <div className="flex-grow relative">
                        <Search className="absolute left-4 top-4 h-5 w-5 text-slate-400" />
                        <input type="text" placeholder="Search roles..." className="w-full pl-12 pr-4 py-3 bg-slate-50 rounded-xl outline-none focus:ring-1 focus:ring-primary-500" />
                    </div>
                    <select className="px-6 py-3 bg-slate-50 rounded-xl outline-none border-none">
                        <option>All Locations</option>
                        <option>Remote</option>
                        <option>New York</option>
                        <option>London</option>
                    </select>
                    <button className="bg-navy-950 text-white px-8 py-3 rounded-xl font-bold hover:bg-gold-500 hover:text-navy-950 transition-all">
                        Find Jobs
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-20">
                    <div className="p-8 bg-white rounded-3xl border border-slate-100 shadow-sm transition-all hover:-translate-y-2">
                        <Star className="h-10 w-10 text-gold-500 mb-6" />
                        <h3 className="font-bold text-lg mb-2">Excellence</h3>
                        <p className="text-sm text-slate-500">We set the standard for premium banking worldwide.</p>
                    </div>
                    <div className="p-8 bg-white rounded-3xl border border-slate-100 shadow-sm transition-all hover:-translate-y-2">
                        <Sparkles className="h-10 w-10 text-primary-500 mb-6" />
                        <h3 className="font-bold text-lg mb-2">Innovation</h3>
                        <p className="text-sm text-slate-500">Building next-gen digital experiences for our members.</p>
                    </div>
                    <div className="p-8 bg-white rounded-3xl border border-slate-100 shadow-sm transition-all hover:-translate-y-2">
                        <Globe className="h-10 w-10 text-emerald-500 mb-6" />
                        <h3 className="font-bold text-lg mb-2">Global Impact</h3>
                        <p className="text-sm text-slate-500">Operating in 40+ countries with a unified mission.</p>
                    </div>
                    <div className="p-8 bg-white rounded-3xl border border-slate-100 shadow-sm transition-all hover:-translate-y-2">
                        <Briefcase className="h-10 w-10 text-indigo-500 mb-6" />
                        <h3 className="font-bold text-lg mb-2">Stability</h3>
                        <p className="text-sm text-slate-500">100 years of heritage and unshakeable trust.</p>
                    </div>
                </div>

                <h2 className="text-3xl font-bold text-navy-950 mb-8 italic">Open Positions</h2>
                <div className="bg-white rounded-[2.5rem] border border-slate-200 overflow-hidden shadow-sm">
                    {jobs.map((job, idx) => (
                        <div key={idx} className={`p-8 flex flex-col md:flex-row md:items-center justify-between hover:bg-slate-50 transition-colors ${idx !== jobs.length - 1 ? 'border-b border-slate-100' : ''}`}>
                            <div className="mb-4 md:mb-0">
                                <h4 className="text-xl font-bold text-navy-950 mb-2">{job.title}</h4>
                                <div className="flex flex-wrap gap-4">
                                    <span className="flex items-center text-sm text-slate-500">
                                        <MapPin className="h-4 w-4 mr-1" /> {job.location}
                                    </span>
                                    <span className="bg-slate-100 text-[10px] font-bold px-2 py-1 rounded text-slate-600 uppercase tracking-tighter">
                                        {job.type}
                                    </span>
                                    <span className="text-sm font-medium text-primary-600">{job.dept}</span>
                                </div>
                            </div>
                            <button className="flex items-center space-x-2 bg-slate-900 text-white px-6 py-3 rounded-xl font-bold hover:bg-gold-500 hover:text-navy-950 transition-all text-center">
                                <span>Apply Now</span>
                                <ArrowRight className="h-4 w-4" />
                            </button>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default CareersPage;
