# Aave V2 DeFi Credit Scoring

## Overview
This project computes a DeFi credit score for wallets based on Aave V2 transaction data. Scores range from 0 to 1000, where higher values indicate trustworthy behavior.

## Setup
```bash
pip install pandas matplotlib
```

## Run
```bash
python src/run_all.py --input data/user_transactions.json --output output/wallet_scores.csv
```

## Features Used
- Deposit count
- Borrow vs repay balance
- Liquidation events

## Scoring Logic
- Base score: 1000
- +5 per deposit
- -10 for each unmatched borrow
- -100 per liquidation
