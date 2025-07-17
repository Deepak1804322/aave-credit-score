import argparse
from process_data import load_and_process
from scoring import score_wallets
from visualize import plot_score_distribution
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to user_transactions.json")
    parser.add_argument("--output", required=True, help="Path to save scored wallets CSV")
    args = parser.parse_args()

    df = load_and_process(args.input)
    scored_wallets = score_wallets(df)
    scored_wallets.to_csv(args.output, index=False)
    plot_score_distribution(scored_wallets)
