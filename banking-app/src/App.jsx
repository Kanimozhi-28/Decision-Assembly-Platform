import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CardsPage from './pages/CardsPage';
import CardDetailsPage from './pages/CardDetailsPage';
import MortgageCalculator from './pages/MortgageCalculator';
import AccountsPage from './pages/AccountsPage';
import AccountDetailsPage from './pages/AccountDetailsPage';
import LoansPage from './pages/LoansPage';
import HomeLoanPage from './pages/HomeLoanPage';
import AutoLoanPage from './pages/AutoLoanPage';
import PersonalLoanPage from './pages/PersonalLoanPage';
import RatesPage from './pages/RatesPage';
import SecurityPage from './pages/SecurityPage';
import FAQPage from './pages/FAQPage';
import ContactPage from './pages/ContactPage';
import AboutPage from './pages/AboutPage';
import CareersPage from './pages/CareersPage';
import LoginPage from './pages/LoginPage';
import PrivacyPage from './pages/PrivacyPage';
import DAPLoader from './components/DAPLoader';

// Placeholder components for other pages
const PlaceholderPage = ({ title }) => (
  <div className="min-h-screen flex items-center justify-center p-20">
    <div className="text-center max-w-xl">
      <h1 className="text-4xl font-extrabold text-navy-950 mb-6 italic underline decoration-gold-500 underline-offset-8 uppercase tracking-widest">{title}</h1>
      <p className="text-slate-600 text-lg">Thank you for your interest in ApexBank. This section is currently being optimized for the DAP experience. Please check back shortly.</p>
    </div>
  </div>
);

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-slate-50 flex flex-col">
        <DAPLoader />
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/accounts" element={<AccountsPage />} />
            <Route path="/accounts/:id" element={<AccountDetailsPage />} />
            <Route path="/cards" element={<CardsPage />} />
            <Route path="/cards/:id" element={<CardDetailsPage />} />
            <Route path="/loans" element={<LoansPage />} />
            <Route path="/loans/home" element={<HomeLoanPage />} />
            <Route path="/loans/auto" element={<AutoLoanPage />} />
            <Route path="/loans/personal" element={<PersonalLoanPage />} />
            <Route path="/mortgage-calculator" element={<MortgageCalculator />} />
            <Route path="/rates" element={<RatesPage />} />
            <Route path="/security" element={<SecurityPage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/faq" element={<FAQPage />} />
            <Route path="/contact" element={<ContactPage />} />
            <Route path="/careers" element={<CareersPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/privacy" element={<PrivacyPage />} />
            {/* 404 Route */}
            <Route path="*" element={<PlaceholderPage title="404 - Not Found" />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
