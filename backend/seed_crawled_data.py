import json

# Pre-defined Banking Product Data
# (Normally extracted by the crawler, but hardcoded here to bypass local network issues)

SEED_DATA = [
    {
        "url": "http://localhost:5174/accounts",
        "title": "Apex Premium Checking & Savings",
        "path": "/accounts",
        "content": """
# Apex Premium Checking

Experience banking without boundaries. Our Premium Checking account offers:
- **No monthly fees** with minimum balance of $2,500.
- **ATM fee reimbursement** worldwide.
- **Priority customer support** 24/7.
- **Integration** with Apex Financial Insights dashboard.

# High-Yield Savings

Grow your wealth faster with our industry-leading savings rates.
- **4.50% APY** on all balances.
- **No lock-in period** - access your funds anytime.
- **Automatic transfers** to help you reach your goals.
        """
    },
    {
        "url": "http://localhost:5174/cards/travel-platinum",
        "title": "Apex Travel Platinum Card",
        "path": "/cards/travel-platinum",
        "content": """
# Apex Travel Platinum Card

The ultimate companion for the modern explorer.

## Key Benefits
- **5X Points** on flights booked directly with airlines or through Apex Travel.
- **3X Points** on hotels and dining worldwide.
- **1X Points** on all other purchases.
- **$300 Annual Travel Credit** for incidental fees.
- **Global Lounge Access** to over 1,300 airport lounges.

## Fees & Rates
- **Annual Fee**: $550
- **Foreign Transaction Fee**: None
- **APR**: 19.99% - 26.99% Variable
        """
    },
    {
        "url": "http://localhost:5174/cards/daily-cashback",
        "title": "Apex Daily Cashback Card",
        "path": "/cards/daily-cashback",
        "content": """
# Apex Daily Cashback Card

Simple, rewarding, and transparent. Earn cash back on everything you buy.

## Key Benefits
- **2% Unlimited Cash Back** on every purchase, every day.
- **No categories to track** or enroll in.
- **$200 Welcome Bonus** after spending $1,000 in the first 3 months.
- **0% Intro APR** for 15 months on purchases and balance transfers.

## Fees
- **Annual Fee**: $0
- **Foreign Transaction Fee**: 3%
        """
    },
    {
        "url": "http://localhost:5174/cards/student-learner",
        "title": "Apex Student Learner Card",
        "path": "/cards/student-learner",
        "content": """
# Apex Student Learner Card

Build your credit history while earning rewards for good grades.

## Features
- **Earn 1% Cash Back** on all purchases.
- **Good Grades Reward**: $20 statement credit each year you have a GPA of 3.0 or higher.
- **Credit Education**: Free access to your credit score and educational resources.
- **No Security Deposit** required.

## Fees
- **Annual Fee**: $0
- **APR**: 24.99% Variable
        """
    },
    {
        "url": "http://localhost:5174/loans/home-fixed",
        "title": "Apex 30-Year Fixed Mortgage",
        "path": "/loans/home-fixed",
        "content": """
# 30-Year Fixed Rate Mortgage
Stability for the long term. Lock in your rate for the entire life of your loan.
- **Current Rate**: 6.25% APR
- **Down Payment**: As low as 3%
- **Best for**: Homeowners planning to stay in their home for many years.
        """
    },
    {
        "url": "http://localhost:5174/loans/personal-flex",
        "title": "Apex Personal Flex Loan",
        "path": "/loans/personal-flex",
        "content": """
# Personal Flex Loan
Achieve your dreams with flexible funding options.
- **Rates**: From 7.49% APR
- **Terms**: 24 to 60 months
- **Usage**: Debt consolidation, home improvement, or major purchases.
- **Benefit**: No prepayment penalties.
        """
    },
    {
        "url": "http://localhost:5174/loans/auto-express",
        "title": "Apex Auto Express Loan",
        "path": "/loans/auto-express",
        "content": """
# Auto Express Loan
Get on the road faster with our quick approval auto loans.
- **Rates**: competitive rates for new and used vehicles.
- **Term**: Flexible terms up to 72 months.
- **Benefit**: 0.25% rate discount with automatic payments.
        """
    },
    {
        "url": "http://localhost:5174/security",
        "title": "Security & Fraud Protection",
        "path": "/security",
        "content": """
# Your Security is Our Priority

We use state-of-the-art technology to protect your financial information.

## Features
- **256-bit Encryption**: Bank-level security for all data transmissions.
- **Zero Liability Protection**: You are not responsible for unauthorized charges.
- **Instant Fraud Alerts**: Real-time notifications for suspicious activity.
- **Biometric Login**: Secure access with Face ID or Fingerprint.
- **Card Lock/Unlock**: Instantly freeze your card from the app if it's misplaced.
        """
    }
]

def generate_seed_file():
    output_file = "crawled_content.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(SEED_DATA, f, indent=4)
    print(f"Generated seed content in '{output_file}' with {len(SEED_DATA)} pages.")

if __name__ == "__main__":
    generate_seed_file()
